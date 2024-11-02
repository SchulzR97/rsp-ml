import torch
import torch.nn.functional as F
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sn
import pandas as pd
import cv2 as cv
from typing import List

def confusion_matrix(Y:torch.Tensor, T:torch.Tensor) -> torch.Tensor:
    """
    Calculates the confusion matrix. Expected input shape: (batch_size, num_classes)
    
    Parameters
    ----------
    Y : torch.Tensor
        Prediction
    T : torch.Tensor
        True values

    Returns
    -------
    torch.Tensor
        Confusion matrix
    """
    assert Y.shape == T.shape, f'Expected Y and T to have the same shape.'
    assert torch.all(Y >= 0) and torch.all(Y <= 1), f'Expected 0 <= Y <= 1'
    assert torch.all(T >= 0) and torch.all(T <= 1), f'Expected 0 <= T <= 1'
    assert len(T.shape) == 2, f'Expected shape (batch_size, num_classes), but got shape of {T.shape}'

    num_classes = T.shape[1]
    classes_Y = torch.argmax(Y, dim=1)
    classes_T = torch.argmax(T, dim=1)

    cm = torch.zeros((num_classes, num_classes), dtype=torch.int64)

    for cy, ct in zip(classes_Y, classes_T):
        cm[ct, cy] += 1

    return cm

def confusion(Y, T):
    """ Returns the confusion matrix for the values in the `prediction` and `truth`
        tensors, i.e. the amount of positions where the values of `prediction`
        and `truth` are
        - 1 and 1 (True Positive)
        - 1 and 0 (False Positive)
        - 0 and 0 (True Negative)
        - 0 and 1 (False Negative)
        """
    confusion_vector = Y / T
    # Element-wise division of the 2 tensors returns a new tensor which holds a
    # unique value for each case:
    #   1     where prediction and truth are 1 (True Positive)
    #   inf   where prediction is 1 and truth is 0 (False Positive)
    #   nan   where prediction and truth are 0 (True Negative)
    #   0     where prediction is 0 and truth is 1 (False Negative)
    true_positives = torch.sum(confusion_vector == 1).item()
    false_positives = torch.sum(confusion_vector == float('inf')).item()
    true_negatives = torch.sum(torch.isnan(confusion_vector)).item()
    false_negatives = torch.sum(confusion_vector == 0).item()
    return true_positives, false_positives, true_negatives, false_negatives

def TP(Y:torch.Tensor, T:torch.Tensor) -> int:
    """
    True positives. Expected input shape: (batch_size, num_classes)
    
    Parameters
    ----------
    Y : torch.Tensor
        Prediction
    T : torch.Tensor
        True values

    Returns
    -------
    int
        True positives
    """
    assert Y.shape == T.shape, f'Expected Y and T to have the same shape.'
    assert torch.all(Y >= 0) and torch.all(Y <= 1), f'Expected 0 <= Y <= 1'
    assert torch.all(T >= 0) and torch.all(T <= 1), f'Expected 0 <= T <= 1'
    assert len(T.shape) == 2, f'Expected shape (batch_size, num_classes), but got shape of {T.shape}'
    
    Y_pos = Y >= 0.5
    T_pos = T >= 0.5

    mask = torch.bitwise_and(Y_pos, T_pos)
    tp = mask.sum().item()
    return tp

def TN(Y:torch.Tensor, T:torch.Tensor) -> int:
    """
    True negatives. Expected input shape: (batch_size, num_classes)
    
    Parameters
    ----------
    Y : torch.Tensor
        Prediction
    T : torch.Tensor
        True values

    Returns
    -------
    int
        True negatives
    """
    assert Y.shape == T.shape, f'Expected Y and T to have the same shape.'
    assert torch.all(Y >= 0) and torch.all(Y <= 1), f'Expected 0 <= Y <= 1'
    assert torch.all(T >= 0) and torch.all(T <= 1), f'Expected 0 <= T <= 1'
    assert len(T.shape) == 2, f'Expected shape (batch_size, num_classes), but got shape of {T.shape}'
    
    Y_neg = Y < 0.5
    T_neg = T < 0.5

    mask = torch.bitwise_and(Y_neg, T_neg)
    tn = mask.sum().item()
    return tn

def FP(Y:torch.Tensor, T:torch.Tensor) -> int:
    """
    False positives. Expected input shape: (batch_size, num_classes)
    
    Parameters
    ----------
    Y : torch.Tensor
        Prediction
    T : torch.Tensor
        True values

    Returns
    -------
    int
        False positives
    """
    assert Y.shape == T.shape, f'Expected Y and T to have the same shape.'
    assert torch.all(Y >= 0) and torch.all(Y <= 1), f'Expected 0 <= Y <= 1'
    assert torch.all(T >= 0) and torch.all(T <= 1), f'Expected 0 <= T <= 1'
    assert len(T.shape) == 2, f'Expected shape (batch_size, num_classes), but got shape of {T.shape}'
    
    Y_pos = Y >= 0.5
    T_neg = T < 0.5

    mask = torch.bitwise_and(Y_pos, T_neg)
    fp = mask.sum().item()
    return fp

def FN(Y:torch.Tensor, T:torch.Tensor) -> int:
    """
    False negatives. Expected input shape: (batch_size, num_classes)
    
    Parameters
    ----------
    Y : torch.Tensor
        Prediction
    T : torch.Tensor
        True values

    Returns
    -------
    int
        False negatives
    """
    assert Y.shape == T.shape, f'Expected Y and T to have the same shape.'
    assert torch.all(Y >= 0) and torch.all(Y <= 1), f'Expected 0 <= Y <= 1'
    assert torch.all(T >= 0) and torch.all(T <= 1), f'Expected 0 <= T <= 1'
    assert len(T.shape) == 2, f'Expected shape (batch_size, num_classes), but got shape of {T.shape}'
    
    Y_neg = Y < 0.5
    T_pos = T >= 0.5

    mask = torch.bitwise_and(Y_neg, T_pos)
    fn = mask.sum().item()
    return fn

def FPR(Y:torch.Tensor, T:torch.Tensor) -> float:
    """
    False positive rate. Expected input shape: (batch_size, num_classes)
    
    Parameters
    ----------
    Y : torch.Tensor
        Prediction
    T : torch.Tensor
        True values

    Returns
    -------
    float
        False positive rate
    """
    assert Y.shape == T.shape, f'Expected Y and T to have the same shape.'
    assert torch.all(Y >= 0) and torch.all(Y <= 1), f'Expected 0 <= Y <= 1'
    assert torch.all(T >= 0) and torch.all(T <= 1), f'Expected 0 <= T <= 1'
    assert len(T.shape) == 2, f'Expected shape (batch_size, num_classes), but got shape of {T.shape}'

    fp = FP(Y, T)
    tn = TN(Y, T)
    if fp + tn == 0:
        return np.nan
    fpr = fp / (fp + tn)
    return fpr

def TPR(Y:torch.Tensor, T:torch.Tensor) -> float:
    """
    True positive rate. Expected input shape: (batch_size, num_classes)
    
    Parameters
    ----------
    Y : torch.Tensor
        Prediction
    T : torch.Tensor
        True values

    Returns
    -------
    float
        True positive rate
    """
    assert Y.shape == T.shape, f'Expected Y and T to have the same shape.'
    assert torch.all(Y >= 0) and torch.all(Y <= 1), f'Expected 0 <= Y <= 1'
    assert torch.all(T >= 0) and torch.all(T <= 1), f'Expected 0 <= T <= 1'
    assert len(T.shape) == 2, f'Expected shape (batch_size, num_classes), but got shape of {T.shape}'

    tp = TP(Y, T)
    fn = FN(Y, T)
    if tp + fn == 0:
        return np.nan
    tpr = tp / (tp + fn)
    return tpr

#__equation__ $precision = \frac{TP}{TP + FP}$
def precision(Y:torch.Tensor, T:torch.Tensor) -> float:
    """
    Precision. Expected input shape: (batch_size, num_classes)

    Parameters
    ----------
    Y : torch.Tensor
        Prediction
    T : torch.Tensor
        True values

    Returns
    -------
    float
        Precision
    """
    assert Y.shape == T.shape, f'Expected Y and T to have the same shape.'
    assert torch.all(Y >= 0) and torch.all(Y <= 1), f'Expected 0 <= Y <= 1'
    assert torch.all(T >= 0) and torch.all(T <= 1), f'Expected 0 <= T <= 1'
    assert len(T.shape) == 2, f'Expected shape (batch_size, num_classes), but got shape of {T.shape}'

    tp = TP(Y, T)
    fp = FP(Y, T)
    if tp + fp == 0:
        return np.nan
    prec = tp / (tp + fp)
    return prec

#__equation__ $recall = \frac{TP}{TP + FN}$
def recall(Y:torch.Tensor, T:torch.Tensor) -> float:
    """
    Recall. Expected input shape: (batch_size, num_classes)

    Parameters
    ----------
    Y : torch.Tensor
        Prediction
    T : torch.Tensor
        True values

    Returns
    -------
    float
        Recall
    """
    assert Y.shape == T.shape, f'Expected Y and T to have the same shape.'
    assert torch.all(Y >= 0) and torch.all(Y <= 1), f'Expected 0 <= Y <= 1'
    assert torch.all(T >= 0) and torch.all(T <= 1), f'Expected 0 <= T <= 1'
    assert len(T.shape) == 2, f'Expected shape (batch_size, num_classes), but got shape of {T.shape}'

    tp = TP(Y, T)
    fn = FN(Y, T)
    if tp + fn == 0:
        return np.nan
    rec = tp / (tp + fn)
    return rec

#__equation__ $precision = \frac{TP}{TP + FP}$
#__equation__ $recall = \frac{TP}{TP + FN}$
#__equation__ $F_1 = \frac{2 \cdot precision \cdot recall}{precision + recall} = \frac{2 \cdot TP}{2 \cdot TP + FP + FN}$
#__example__ import rsp.ml.metrics as m\n
#__example__ Y = torch.tensor([\n\t\t[0.87, 0.01, 0.05, 0.07],
#__example__ \t\t[0.02, 0.09, 0.86, 0.03]
#__example__ \t])
#__example__ T = torch.tensor([\n\t\t[1., 0., 0., 0.],\n\t\t[0., 1., 0., 0.]\n\t])
#__example__ \nf1score = m.F1_Score(Y, T)
#__example__ \nprint(f1score) --> 0.5
def F1_Score(Y:torch.Tensor, T:torch.Tensor) -> float:
    """
    F1 Score. Expected input shape: (batch_size, num_classes)

    Parameters
    ----------
    Y : torch.Tensor
        Prediction
    T : torch.Tensor
        True values

    Returns
    -------
    float
        F1 Score
    """
    # Formular

    assert Y.shape == T.shape, f'Expected Y and T to have the same shape.'
    assert torch.all(Y >= 0) and torch.all(Y <= 1), f'Expected 0 <= Y <= 1'
    assert torch.all(T >= 0) and torch.all(T <= 1), f'Expected 0 <= T <= 1'
    assert len(T.shape) == 2, f'Expected shape (batch_size, num_classes), but got shape of {T.shape}'

    tp = TP(Y, T)
    fp = FP(Y, T)
    fn = FN(Y, T)
    if tp + fp + fn == 0:
        return np.nan
    f1score = 2 * tp / (2 * tp + fp + fn)
    return f1score

def top_k_accuracy(Y:torch.Tensor, T:torch.Tensor, k:int) -> float:
    """
    Top k accuracy. Expected input shape: (batch_size, num_classes)
    
    Parameters
    ----------
    Y : torch.Tensor
        Prediction
    T : torch.Tensor
        True values

    Returns
    -------
    float
        Top k accuracy
    """
    assert Y.shape == T.shape, f'Expected Y and T to have the same shape.'
    assert torch.all(Y >= 0) and torch.all(Y <= 1), f'Expected 0 <= Y <= 1'
    assert torch.all(T >= 0) and torch.all(T <= 1), f'Expected 0 <= T <= 1'
    assert len(T.shape) == 2, f'Expected shape (batch_size, num_classes), but got shape of {T.shape}'

    top_k_prediction = torch.argsort(Y, dim=1, descending=True)[:, :k]
    top_1_target = torch.argmax(T, dim=1)

    tp = 0
    for y, t in zip(top_k_prediction, top_1_target):
        if t in y:
            tp += 1
        pass

    acc = tp / T[:, 0].numel()
    return acc

def top_1_accuracy(Y:torch.Tensor, T:torch.Tensor) -> float:
    """
    Top 1 accuracy. Expected input shape: (batch_size, num_classes)
    
    Parameters
    ----------
    Y : torch.Tensor
        Prediction
    T : torch.Tensor
        True values

    Returns
    -------
    float
        Top 1 accuracy -> top k accuracy | k = 1
    """
    assert Y.shape == T.shape, f'Expected Y and T to have the same shape.'
    assert torch.all(Y >= 0) and torch.all(Y <= 1), f'Expected 0 <= Y <= 1'
    assert torch.all(T >= 0) and torch.all(T <= 1), f'Expected 0 <= T <= 1'
    assert len(T.shape) == 2, f'Expected shape (batch_size, num_classes), but got shape of {T.shape}'

    return top_k_accuracy(Y, T, 1)

def top_2_accuracy(Y:torch.Tensor, T:torch.Tensor) -> float:
    """
    Top 2 accuracy. Expected input shape: (batch_size, num_classes)
    
    Parameters
    ----------
    Y : torch.Tensor
        Prediction
    T : torch.Tensor
        True values

    Returns
    -------
    float
        Top 2 accuracy -> top k accuracy | k = 2
    """
    assert Y.shape == T.shape, f'Expected Y and T to have the same shape.'
    assert torch.all(Y >= 0) and torch.all(Y <= 1), f'Expected 0 <= Y <= 1'
    assert torch.all(T >= 0) and torch.all(T <= 1), f'Expected 0 <= T <= 1'
    assert len(T.shape) == 2, f'Expected shape (batch_size, num_classes), but got shape of {T.shape}'

    return top_k_accuracy(Y, T, 2)

def top_3_accuracy(Y:torch.Tensor, T:torch.Tensor) -> float:
    """
    Top 3 accuracy. Expected input shape: (batch_size, num_classes)
    
    Parameters
    ----------
    Y : torch.Tensor
        Prediction
    T : torch.Tensor
        True values

    Returns
    -------
    float
        Top 3 accuracy -> top k accuracy | k = 3
    """
    assert Y.shape == T.shape, f'Expected Y and T to have the same shape.'
    assert torch.all(Y >= 0) and torch.all(Y <= 1), f'Expected 0 <= Y <= 1'
    assert torch.all(T >= 0) and torch.all(T <= 1), f'Expected 0 <= T <= 1'
    assert len(T.shape) == 2, f'Expected shape (batch_size, num_classes), but got shape of {T.shape}'

    return top_k_accuracy(Y, T, 3)

def top_5_accuracy(Y:torch.Tensor, T:torch.Tensor) -> float:
    """
    Top 5 accuracy. Expected input shape: (batch_size, num_classes)
    
    Parameters
    ----------
    Y : torch.Tensor
        Prediction
    T : torch.Tensor
        True values

    Returns
    -------
    float
        Top 5 accuracy -> top k accuracy | k = 5
    """
    assert Y.shape == T.shape, f'Expected Y and T to have the same shape.'
    assert torch.all(Y >= 0) and torch.all(Y <= 1), f'Expected 0 <= Y <= 1'
    assert torch.all(T >= 0) and torch.all(T <= 1), f'Expected 0 <= T <= 1'
    assert len(T.shape) == 2, f'Expected shape (batch_size, num_classes), but got shape of {T.shape}'

    return top_k_accuracy(Y, T, 5)

def top_10_accuracy(Y:torch.Tensor, T:torch.Tensor) -> float:
    """
    Top 10 accuracy. Expected input shape: (batch_size, num_classes)
    
    Parameters
    ----------
    Y : torch.Tensor
        Prediction
    T : torch.Tensor
        True values

    Returns
    -------
    float
        Top 10 accuracy -> top k accuracy | k = 10
    """
    assert Y.shape == T.shape, f'Expected Y and T to have the same shape.'
    assert torch.all(Y >= 0) and torch.all(Y <= 1), f'Expected 0 <= Y <= 1'
    assert torch.all(T >= 0) and torch.all(T <= 1), f'Expected 0 <= T <= 1'
    assert len(T.shape) == 2, f'Expected shape (batch_size, num_classes), but got shape of {T.shape}'

    return top_k_accuracy(Y, T, 10)

#__image__ ![](documentation/image/confusion_matrix.jpg)
def plot_confusion_matrix(
        confusion_matrix:torch.Tensor,
        labels:List[str] = None,
        cmap:str = 'Blues',
        xlabel:str = 'Predicted label',
        ylabel:str = 'True label',
        title:str = 'Confusion Matrix',
        plt_show:bool = False,
        save_file_name:str = None) -> np.array:
    """
    Plot the confusion matrix
    
    Parameters
    ----------
    confusion_matrix : torch.Tensor
        Confusion matrix
    labels : str, optional, default = None
        Class labels -> automatic labeling C000, ..., CXXX if labels is None
    cmap : str, optional, default = 'Blues'
        Seaborn cmap, see https://r02b.github.io/seaborn_palettes/
    xlabel : str, optional, default = 'Predicted label'
        X-Axis label
    ylabel : str, optional, default = 'True label'
        Y-Axis label
    title : str, optional, default = 'Confusion Matrix'
        Title of the plot
    plt_show : bool, optional, default = False
        Set to True to show the plot
    save_file_name : str, optional, default = None
        If not None, the plot is saved under the specified save_file_name.

    Returns
    -------
    np.array
        Image of the confusion matrix
    """
    # test
    if labels is None:
        labels = [f'Class {i+1}' for i in range(confusion_matrix.shape[0])]

    df_cm = pd.DataFrame(confusion_matrix, index = [i for i in labels],
                  columns = [i for i in labels])
    fig = plt.figure(figsize = (10,7))

    sn.heatmap(df_cm, annot=True, cmap=cmap, fmt='g')
    plt.xticks(rotation=45, ha="right")
    plt.yticks(rotation=0, ha="right")
    if title is not None:
        plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    if plt_show:
        plt.show()

    fig.canvas.draw()

    s, (width, height) = fig.canvas.print_to_buffer()

    # Option 2a: Convert to a NumPy array.
    img = np.fromstring(s, np.uint8).reshape((height, width, 4))
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    if save_file_name is not None:
        cv.imwrite(save_file_name, img)

    plt.close()

    return img

if __name__ == '__main__':
    Y = torch.tensor([
        [0.1, 0.1, 0.8],
        [0.03, 0.95, 0.02],
        [0.05, 0.9, 0.05]
    ])
    T = torch.tensor([
        [0, 0, 1],
        [1, 0, 0],
        [0, 1, 0]
    ])

    tp = TP(Y, T)
    tn = TN(Y, T)
    fp = FP(Y, T)
    fn = FN(Y, T)

    f1 = F1_Score(Y, T)

    epsilon = 0.2
    num_elements = 10000
    num_classes = 7

    T = []
    for i in range(num_elements):
        true_class = torch.randint(0, num_classes, (1,))
        t = F.one_hot(true_class, num_classes=num_classes)
        T.append(t)
    T = torch.cat(T)

    dist = torch.normal(T.float(), 0.5)
    Y = torch.argmax(dist, dim=1)
    Y = F.one_hot(Y, num_classes=num_classes)

    conf_m = confusion_matrix(Y, T)
    print(conf_m)

    labels = []
    for a in range(num_classes):
        a_str = str(a)
        while len(a_str) < 3:
            a_str = '0' + a_str
        a_str = 'A' + a_str
        labels.append(a_str)

    img = plot_confusion_matrix(conf_m, labels=labels, plt_show=True)
    cv.imwrite('documentation/image/confusion_matrix.jpg', img)