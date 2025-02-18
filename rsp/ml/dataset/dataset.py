from enum import Enum
from torch.utils.data import IterableDataset, Dataset
from datasets import load_dataset
import numpy as np
import os
from pathlib import Path
import pkg_resources
from platformdirs import user_cache_dir
import urllib
import tarfile
import cv2 as cv
import csv
import torch
import rsp.ml.multi_transforms.multi_transforms as multi_transforms
from tqdm import tqdm
from glob import glob
from threading import Thread
import time
import pandas as pd
import rsp.common.console as console

# __example__ from rsp.ml.dataset import TUC_AR
# __example__ 
# __example__ transforms = multi_transforms.Compose([multi_transforms.Resize((400, 400))])
# __example__ tuc_ar_ds = TUC_AR(
# __example__               split='val',
# __example__               depth_channel=True,
# __example__               transforms=transforms,
# __example__               num_actions=10,
# __example__               streaming=True)
class TUC_AR(IterableDataset):
    """
    Small-scale action recognition dataset.

    Wrapper class for loading [SchulzR97/TUC-AR](https://huggingface.co/datasets/SchulzR97/TUC-AR) HuggingFace dataset as `torch.util.data.IterableDataset`.

    TUC-AR is a small scale action recognition dataset, containing 6(+1) action categories for human machine interaction. 

    **Facts**
    - RGB and depth input recorded by Intel RealSense D435 depth camera
    - 8 subjects
    - 11,031 sequences (train 8,893/ val 2,138)
    - 3 perspectives per scene
    - 6(+1) action classes<br>

    **Action Classes**
    | Action | Label    |
    |--------|----------|
    | A000   | None     |
    | A001   | Waving   |
    | A002   | Pointing |
    | A003   | Clapping |
    | A004   | Follow   |
    | A005   | Walking  |
    | A006   | Stop     |
    """
    def __init__(
            self,
            split:str,
            depth_channel:bool,
            num_actions:int = 7,
            streaming:bool = False,
            sequence_length:int = 30,
            transforms:multi_transforms.Compose = multi_transforms.Compose([])
    ):
        """
        Initializes a new instance.
        
        Parameters
        ----------
        split : str
            Dataset split [train|val]
        depth_channel : bool
            Load depth channel. If set to `True`, the generated input tensor will have 4 channels instead of 3. (batch_size, sequence_length, __channels__, width, height)
        num_actions : int, default = 7
            Number of action classes -> shape[1] of target tensor (batch_size, **num_actions**)
        streaming : bool, default = False
            If set to `True`, don't download the data files. Instead, it streams the data progressively while iterating on the dataset.
        sequence_length : int, default = 30
            Length of each sequence. -> shape[1] of the generated input tensor. (batch_size, **sequence_length**, channels, width, height)
        transforms : rsp.ml.multi_transforms.Compose = default = rsp.ml.multi_transforms.Compose([])
            Transformations, that will be applied to each input sequence. See documentation of `rsp.ml.multi_transforms` for more details.
        """
        super().__init__()

        assert split in ['train', 'val']

        self.split = split
        self.depth_channel = depth_channel
        self.num_actions = num_actions
        self.streaming = streaming
        self.sequence_length = sequence_length
        self.transforms = transforms

        self.__dataset__ = load_dataset('SchulzR97/TUC-AR', streaming=self.streaming, split=self.split)
        self.__image_size__ = (500, 375)
        self.__toTensor__ = multi_transforms.ToTensor()
        self.__stack__ = multi_transforms.Stack()

        self.i = 0

    def __iter__(self):
        self.__iterator__ = iter(self.__dataset__)

        sequence_id = None
        images_rgb, images_d = [], []
        while True:
            try:
                item = next(self.__iterator__)
                start_new_sequence = item['sequence_id'] != sequence_id and sequence_id is not None
            except:
                return

            # new sequence
            if start_new_sequence:
                if self.depth_channel:
                    images_rgb = torch.stack(self.__toTensor__(images_rgb))
                    images_d = torch.stack(self.__toTensor__(images_d))
                    X = torch.cat([images_rgb, images_d], dim=1)
                else:
                    images_rgb = torch.stack(self.__toTensor__(images_rgb))
                    X = images_rgb

                if X.shape[0] > self.sequence_length:
                    start_idx = np.random.randint(0, X.shape[0]-self.sequence_length)
                    end_idx = start_idx + self.sequence_length
                    X = X[start_idx:end_idx]

                X = self.__stack__(self.transforms(X))
                
                action = int(sequence_id[1:4])
                T = torch.zeros((self.num_actions))
                T[action] = 1

                images_rgb = [item['image_rgb']]
                images_d = [item['image_d']]
                
                yield X, T
            else:
                images_rgb.append(item['image_rgb'])
                images_d.append(item['image_d'])
            sequence_id = item['sequence_id']
            pass

class Kinetics(Dataset):
    def __init__(
        self,
        split:str,
        type:int = 400,
        frame_size = (400, 400),
        transforms:multi_transforms.Compose = multi_transforms.Compose([]),
        cache_dir:str = None,
        num_threads:int = 0
    ):
        """
        Initializes a new instance.
        
        Parameters
        ----------
        split : str
            Dataset split [train|val]
        type : int, default = 400
            Type of the kineticts dataset. Currently only 400 is supported.
        frame_size : (int, int), default = (400, 400)
            Size of the frames. The frames will be resized to this size.
        transforms : rsp.ml.multi_transforms.Compose = default = rsp.ml.multi_transforms.Compose([])
            Transformations, that will be applied to each input sequence. See documentation of `rsp.ml.multi_transforms` for more details.
        cache_dir : str, default = None
            Directory to store the downloaded files. If set to `None`, the default cache directory will be used
        num_threads : int, default = 0
            Number of threads to use for downloading the files.
        """
        super().__init__()

        assert split in ['train', 'val'], f'{split} is not a valid split.'
        assert type in [400], f'{type} is not a valid type.'

        self.split = split
        self.type = type
        self.frame_size = frame_size
        self.sequence_length = 10
        self.transforms = transforms
        self.num_threads = num_threads

        if cache_dir is None:
            self.__cache_dir__ = Path(user_cache_dir("rsp-ml", "Robert Schulz")).joinpath('dataset', 'kinetics')
        else:
            self.__cache_dir__ = Path(cache_dir)
        self.__cache_dir__.mkdir(parents=True, exist_ok=True)

        self.__toTensor__ = multi_transforms.ToTensor()
        self.__stack__ = multi_transforms.Stack()

        self.__download__()
        self.__annotations__, self.action_labels = self.__load_annotations_labels__()
        #self.__labels__ = self.__get_labels__()
        self.__files__ = self.__list_files__()

    def __getitem__(self, index):
        youtube_id, fname = self.__files__[index]

        annotation = self.__annotations__[youtube_id]

        if annotation['time_end'] - annotation['time_start'] > self.sequence_length:
            start_idx = np.random.randint(annotation['time_start'], annotation['time_end']-self.sequence_length)
            end_idx = start_idx + self.sequence_length
        else:
            start_idx = annotation['time_start']
            end_idx = annotation['time_end']

        cap = cv.VideoCapture(fname)
        cap.set(cv.CAP_PROP_POS_FRAMES, start_idx)

        frames = []
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frame = cv.resize(frame, self.frame_size)
            frames.append(frame)
            if len(frames) >= end_idx - start_idx:
                break
        frames = np.array(frames) / 255

        if len(frames) == 0:
            X = torch.zeros((self.sequence_length, 3, *self.frame_size), dtype=torch.float32)
            console.warning(f'No frames found for {youtube_id}.')
        else:
            X = torch.tensor(frames).permute(0, 3, 1, 2)
        T = torch.zeros((len(self.action_labels)))
        cls = self.action_labels.index(annotation['label'])
        T[cls] = 1

        return X, T

    def __len__(self):
        return len(self.__files__)
    
    def __get_labels__(self):
        labels = {}
        df = pd.DataFrame(self.__annotations__)
        for i, (key, _) in enumerate(df.groupby('label')):
            key = key.replace('"', '')
            labels[key] = i
        return labels

    def __download__(self):
        def get_fname_resource(resource_name):
            fname = pkg_resources.resource_filename('rsp', resource_name)
            return Path(fname)
        
        def download_file(link, fname, retries = 10):
            attempt = 0
            while attempt < retries:
                try:
                    urllib.request.urlretrieve(link, fname)
                    break
                except urllib.error.ContentTooShortError as e:
                    attempt += 1
                except Exception as e:
                    attempt += 1

        def unpack(src, dest, remove = True):
            with tarfile.open(src, "r:gz") as tar:
                tar.extractall(path=dest)
            if remove:
                os.remove(src)

        anno_link_file = get_fname_resource(f'ml/dataset/links/kinetics/annotations/k{self.type}_annotations.txt')
        with open(anno_link_file, 'r') as file:
            links = file.read().split('\n')
            cache_anno_dir = Path(self.__cache_dir__).joinpath('annotations')
            cache_anno_dir.mkdir(parents=True, exist_ok=True)
            for link in links:
                fname = link.split('/')[-1]
                fname = cache_anno_dir.joinpath(f'k{self.type}_{fname}')
                if fname.exists():
                    continue
                download_file(link, fname)

        path_link_files = [
            get_fname_resource(f'ml/dataset/links/kinetics/paths/k{self.type}_train_path.txt'),
            get_fname_resource(f'ml/dataset/links/kinetics/paths/k{self.type}_test_path.txt'),
            get_fname_resource(f'ml/dataset/links/kinetics/paths/k{self.type}_val_path.txt')
        ]

        cache_archives_dir = self.__cache_dir__.joinpath('archives')
        cache_archives_dir.mkdir(parents=True, exist_ok=True)

        cache_videos_dir = self.__cache_dir__.joinpath('videos')
        cache_videos_dir.mkdir(parents=True, exist_ok=True)

        threads = []

        prog1 = tqdm(path_link_files)
        for link_file in prog1:
            prog1.set_description(f'Downloading {link_file.stem}')

            with open(link_file, 'r') as file:
                links = file.read().split('\n')
            prog2 = tqdm(links)
            for link in prog2:
                prog2.set_description(link)

                def process_link(link):
                    split, fname = link.split('/')[-2:]

                    video_dir = cache_videos_dir.joinpath(split, 'k' + str(self.type) + '_' + fname.split(".")[0])
                    if video_dir.exists():
                        #continue
                        return

                    archive_file = cache_archives_dir.joinpath(split, f'k{self.type}_{fname}')
                    archive_file.parent.mkdir(parents=True, exist_ok=True)
                    if not archive_file.exists():
                        download_file(link, archive_file)

                    video_dir.mkdir(parents=True, exist_ok=True)
                    try:
                        unpack(archive_file, video_dir, remove=True)
                    except Exception as e:
                        video_dir.rmdir()
                        os.remove(archive_file)
                        download_file(link, archive_file)
                        unpack(archive_file, video_dir, remove=True)

                if self.num_threads == 0:
                    process_link(link)
                else:
                    thread = Thread(target=process_link, args=(link,))
                    while len(threads) >= self.num_threads:
                        threads = [t for t in threads if t.is_alive()]
                        time.sleep(0.1)
                    thread.start()
                    threads.append(thread)

    def __load_annotations_labels__(self):
        annotations_file = self.__cache_dir__.joinpath('annotations', f'k{self.type}_{self.split}.csv')
        annotations = {}
        labels = []
        with open(annotations_file, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for i, row in enumerate(spamreader):
                if i == 0:
                    continue
                label, youtube_id, time_start, time_end, split, is_cc = row[0], row[1], int(row[2]), int(row[3]), row[4], int(row[5])
                label = label.replace('"', '')
                annotations[youtube_id] = {
                    'label': label,
                    #'youtube_id': youtube_id,
                    'time_start': time_start,
                    'time_end': time_end,
                    'split': split,
                    'is_cc': is_cc
                }
                if label not in labels:
                    labels.append(label)
        return annotations, sorted(labels)

    def __list_files__(self):
        videos_dir = self.__cache_dir__.joinpath('videos', self.split)
        links = glob(f'{videos_dir}/k{self.type}*/*.mp4')
        files = []#{}
        for link in links:
            youtube_id = Path(link).name[:-18]
            #files[youtube_id] = link
            files.append((youtube_id, link))
        return files

if __name__ == '__main__':
    k400 = Kinetics('train', num_threads=2, cache_dir='/Volumes/USB-Freigabe/KINETICS400')#cache_dir='/Volumes/ROBERT512GB/KINETICS400')

    for i, (X, T) in enumerate(k400):
        print(i)
        pass