import rsp.ml.run
import rsp.ml.metrics as m
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
import torchvision.datasets as datasets
from torch.utils.data import DataLoader

NUM_EPOCHS = 100
BATCH_SIZE = 32
LEARNING_RATE = 1e-4

if __name__ == '__main__':
    transform = torchvision.transforms.ToTensor()
    target_transform = torchvision.transforms.Compose([
                            lambda x:torch.LongTensor([x]),
                            lambda x:F.one_hot(x,10).float().squeeze()])

    ds_train = datasets.MNIST(
        root = './data',
        train = True,
        download = True,
        transform = transform,
        target_transform = target_transform)
    ds_val = datasets.MNIST(
        root = './data',
        train = True,
        download = True,
        transform = transform,
        target_transform = target_transform)
    dl_train = DataLoader(ds_train, batch_size = BATCH_SIZE)
    dl_val = DataLoader(ds_val, batch_size = BATCH_SIZE)

    model = nn.Sequential(
        nn.Conv2d(1, 32, kernel_size=5, stride=2),
        nn.MaxPool2d(kernel_size=3, stride=2),
        nn.ReLU(),
        nn.Conv2d(32, 64, kernel_size=3, stride=2),
        nn.MaxPool2d(kernel_size=2, stride=2),
        nn.ReLU(),
        nn.Flatten(),
        nn.Linear(64, 10),
        nn.Softmax(dim = 1)
    )
    model.to('mps')

    criterion = torch.nn.functional.binary_cross_entropy
    optimizer = torch.optim.Adam(model.parameters(), lr = LEARNING_RATE)

    run = rsp.ml.run.Run('testrun', metrics=[m.top_1_accuracy], moving_average_epochs=0)
    run.recalculate_moving_average()
    run.plot()
    run.load_best_state_dict(model)

    for epoch in range(NUM_EPOCHS):
        results_train = run.train_epoch(dl_train, model, optimizer, criterion)
        results_val = run.validate_epoch(dl_val, model, optimizer, criterion)

        run.plot()
        run.save_best_state_dict(model.state_dict(), results_val[m.top_1_accuracy.__name__], epoch)
        run.save_state_dict(optimizer.state_dict(), 'state_dict_optimizer.pt')
        run.save()

        acc_train = run.get_avg(m.top_1_accuracy.__name__, 'train')
        acc_val = run.get_avg(m.top_1_accuracy.__name__, 'val')
        print(f'Epoch {epoch} acc_train {acc_train:0.6f} acc_val {acc_val:0.6f}')
        pass

    