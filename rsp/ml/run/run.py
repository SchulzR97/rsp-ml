import os
from datetime import datetime
import numpy as np
import json
import matplotlib.pyplot as plt
import torch
import rsp.common.console as console
import pickle as pkl
import copy
from glob import glob
from pathlib import Path

class Run():
    def __init__(self, id = None, moving_average_epochs = 1000):
        if id is None:
            self.id = datetime.now().strftime('%Y%m%d%H%M%S%f')
            self.data = {}
        else:
            self.id = id
            
        self.moving_average_epochs = moving_average_epochs
        self.__init_run_dir__()
        self.__load__()
    
    def append(self, key:str, phase:str, value):
        if not key in self.data:
            self.data[key] = {}
        if not phase in self.data[key]:
            self.data[key][phase] = {
                'val': [],
                'avg': []
            }
        if np.isnan(value):
            if len(self.data[key][phase]['val']) > 0:
                value = self.data[key][phase]['val'][-1]
            else:
                value = 0.

        self.data[key][phase]['val'].append(value)
        self.data[key][phase]['avg'].append(np.average(self.data[key][phase]['val'][-self.moving_average_epochs:]))

    def plot(self):
        self.__init_run_dir__()

        for key in self.data:
            key_str = key.replace('_', ' ')
            plot_file = self.directory_plot.joinpath(f'{key}.jpg')

            cmap = plt.get_cmap('tab20b')
            colors = cmap(np.linspace(0, 1, len(self.data[key])))

            for i, phase in enumerate(self.data[key]):
                if len(self.data[key][phase]['val']) == 0:
                    continue
                plt.plot(self.data[key][phase]['val'], color=colors[i], alpha=0.3)
                plt.plot(self.data[key][phase]['avg'], label=phase, color=colors[i])

            plt.title(key_str)
            plt.xlabel('episode')
            plt.ylabel(key_str)
            plt.minorticks_on()
            plt.grid(which='minor', color='lightgray', linewidth=0.2)
            plt.grid(which='major', linewidth=.6)
            plt.legend()
            plt.savefig(plot_file)
            plt.close()

    def recalculate_moving_average(self):
        for key in self.data:
            for phase in self.data[key]:
                for i in range(len(self.data[key][phase]['val'])):
                    s_i = 0 if i - self.moving_average_epochs < 0 else i - self.moving_average_epochs
                    e_i = i + 1
                    self.data[key][phase]['avg'][i] = np.average(self.data[key][phase]['val'][s_i:e_i])
                self.data[key][phase]['avg'] = self.data[key][phase]['avg'][:len(self.data[key][phase]['val'])]

    def save(self):
        self.__init_run_dir__()
        with open(f'runs/{self.id}/data.json', 'w') as f:
            json.dump(self.data, f)

    def get_val(self, key:str, phase:str):
        return self.data[key][phase]['val'][-1]
    
    def get_avg(self, key:str, phase:str):
        return self.data[key][phase]['avg'][-1]
    
    def len(self):
        l = 0
        for key in self.data:
            for phase in self.data[key]:
                l_temp = len(self.data[key][phase]['val'])
                if l_temp > l:
                    l = l_temp
        return l

    def __init_run_dir__(self):
        self.__directory_runs__ = Path('runs')
        self.__directory_runs__.mkdir(parents=True, exist_ok=True)

        self.directory = self.__directory_runs__.joinpath(self.id)
        self.directory.mkdir(parents=True, exist_ok=True)

        self.directory_plot = self.directory.joinpath('plot')
        self.directory_plot.mkdir(parents=True, exist_ok=True)

        self.file_data = self.directory.joinpath('data.json')

    def __load__(self):
        if self.file_data.exists():
            self.data = json.load(self.file_data.open('r'))
        else:
            self.data = {}

    def __best_state_dict__(self, fname:str, id:str, suffix:str):
        sd_files = glob(f'{self.directory}/*{id}*{suffix}')

        best_acc = 0, None
        for sd_file in sd_files:
            if not '_acc' in sd_file:
                continue
            s_i = sd_file[:-len(suffix)].find('_acc') + 4
            acc = float(sd_file[s_i:-len(suffix)])
            if acc > best_acc[0]:
                best_acc = acc, Path(sd_file).name
        return best_acc

    def save_state_dict(self, state_dict, fname = 'state_dict.pt'):
        self.__init_run_dir__()
        sd = copy.deepcopy(state_dict)
        for k, v in sd.items():
            if hasattr(v, 'cpu'):
                sd[k] = v.cpu()

        file_state_dict = self.directory.joinpath(fname)
        with file_state_dict.open('wb') as f:
            torch.save(sd, f)

    def save_best_state_dict(self, state_dict, new_acc:float, epoch = None, fname = 'state_dict.pt'):
        file_state_dict = self.directory.joinpath(fname)
        suffix = file_state_dict.suffix
        id = file_state_dict.name[:-len(suffix)]
        
        best_acc, best_file = self.__best_state_dict__(fname, id, suffix)

        if new_acc > best_acc:
            epoch_str = '' if epoch is None else f'_e{epoch}'
            fname = f'{id}{epoch_str}_acc{new_acc}{suffix}'
            self.save_state_dict(state_dict, fname)

    def load_state_dict(self, model:torch.nn.Module, fname = 'state_dict.pt'):
        file_state_dict = self.directory.joinpath(fname)
        if file_state_dict is not None and file_state_dict.exists():
            with file_state_dict.open('rb') as f:
                model.load_state_dict(torch.load(f))
        else:
            console.warn(f'File runs/{self.id}/{fname} not found.')
            return
        
    def load_best_state_dict(self, model:torch.nn.Module, fname = 'state_dict.pt'):
        file_state_dict = self.directory.joinpath(fname)
        suffix = file_state_dict.suffix
        id = file_state_dict.name[:-len(suffix)]
        
        best_acc, best_file = self.__best_state_dict__(fname, id, suffix)
        self.load_state_dict(model, best_file)
        console.success(f'Loaded {best_file}')

    def pickle_dump(self, model:torch.nn.Module, fname = 'model.pkl'):
        self.__init_run_dir__()

        file_pkl = self.directory.joinpath(fname)
        with file_pkl.open('wb') as f:
            pkl.dump(model, f)

    def pickle_load(self, fname = 'model.pkl'):
        file_pkl = self.directory.joinpath(fname)
        if file_pkl.exists():
            with open(file_pkl, 'rb') as f:
                model = pkl.load(f)
        else:
            console.warn(f'File runs/{self.id}/{fname} not found.')
            return
        return model
    
if __name__ == '__main__':
    run = Run('test')
    run.save_best_state_dict(torch.nn.Linear(10, 10).state_dict(), 0.919342, 80)
    run.save_best_state_dict(torch.nn.Linear(10, 10).state_dict(), 0.899342, 81)
    run.save_best_state_dict(torch.nn.Linear(10, 10).state_dict(), 0.999342, 82)

    run.load_best_state_dict(torch.nn.Linear(10, 10))
    pass