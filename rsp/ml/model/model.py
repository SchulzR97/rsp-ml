from pathlib import Path
from googledriver import download_folder
import zipfile
import importlib
import sys
import rsp.common.console as console
import torch

TUC_ActionPrediction_model004 = 'TUC/ActionPrediction/Model4'
TUC_ActionPrediction_model005 = 'TUC/ActionPrediction/Model5'

URL = 'https://drive.google.com/drive/folders/1ulNnPqg-5wvenRl2CuJMxMMcaiYfHjQ9?usp=share_link'

def __download_model_folder__():
    download_folder(URL)
    pass

def load_model(model_id:str, force_reload:bool = False) -> torch.nn.Module:
    zip_file = Path(f'Model/{model_id}.zip')
    class_name = model_id.split('/')[-1]
    model_def_py = zip_file.parent.joinpath(class_name).joinpath('model.py')
    model_state_dict_file = zip_file.parent.joinpath(class_name).joinpath('state_dict.pt')

    if not zip_file.exists() or force_reload:
        __download_model_folder__()
        console.success(f'Downloaded models from {URL}.')

    assert zip_file.exists(), f'File {zip_file} does not exist.'

    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(zip_file.parent)

    spec = importlib.util.spec_from_file_location("model", model_def_py)
    foo = importlib.util.module_from_spec(spec)
    sys.modules["module.name"] = foo
    spec.loader.exec_module(foo)
    model:torch.nn.Module = foo.__dict__[class_name]()
    
    with open(model_state_dict_file, 'rb') as f:
        model.load_state_dict(torch.load(f))

    return model

if __name__ == '__main__':
    model = load_model(TUC_ActionPrediction_model005)