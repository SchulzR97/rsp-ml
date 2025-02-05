from enum import Enum
from torch.utils.data import IterableDataset
from datasets import load_dataset
import numpy as np
from pathlib import Path
import cv2 as cv
import torch
import rsp.ml.multi_transforms.multi_transforms as multi_transforms

class TUC_AR(IterableDataset):
    """
    Small-scal action recognition dataset.
    
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
            seqence_length:int = 30,
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
        self.sequence_length = seqence_length
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
                    X = torch.stack(images_rgb)

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
