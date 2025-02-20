# RSProduction MachineLearning

This project provides some usefull machine learning functionality.

# Table of Contents

- [1 dataset](#1-dataset)
  - [1.1 TUC\_AR : torch.utils.data.dataset.IterableDataset](#11-tuc\_ar--torchutilsdatadatasetiterabledataset)
    - [1.1.1 \_\_init\_\_](#111-\_\_init\_\_)
- [2 metrics](#2-metrics)
  - [2.1 AUROC](#21-auroc)
  - [2.2 F1\_Score](#22-f1\_score)
  - [2.3 FN](#23-fn)
  - [2.4 FP](#24-fp)
  - [2.5 FPR](#25-fpr)
  - [2.6 ROC](#26-roc)
  - [2.7 TN](#27-tn)
  - [2.8 TP](#28-tp)
  - [2.9 TPR](#29-tpr)
  - [2.10 confusion\_matrix](#210-confusion\_matrix)
  - [2.11 plot\_ROC](#211-plot\_roc)
  - [2.12 plot\_confusion\_matrix](#212-plot\_confusion\_matrix)
  - [2.13 precision](#213-precision)
  - [2.14 recall](#214-recall)
  - [2.15 top\_10\_accuracy](#215-top\_10\_accuracy)
  - [2.16 top\_1\_accuracy](#216-top\_1\_accuracy)
  - [2.17 top\_2\_accuracy](#217-top\_2\_accuracy)
  - [2.18 top\_3\_accuracy](#218-top\_3\_accuracy)
  - [2.19 top\_5\_accuracy](#219-top\_5\_accuracy)
  - [2.20 top\_k\_accuracy](#220-top\_k\_accuracy)
- [3 model](#3-model)
  - [3.1 MODELS : enum.Enum](#31-models--enumenum)
  - [3.2 WEIGHTS : enum.Enum](#32-weights--enumenum)
  - [3.3 list\_model\_weights](#33-list\_model\_weights)
  - [3.4 load\_model](#34-load\_model)
  - [3.5 publish\_model](#35-publish\_model)
- [4 multi\_transforms](#4-multi\_transforms)
  - [4.1 BGR2GRAY : MultiTransform](#41-bgr2gray--multitransform)
    - [4.1.1 \_\_call\_\_](#411-\_\_call\_\_)
    - [4.1.2 \_\_init\_\_](#412-\_\_init\_\_)
  - [4.2 BGR2RGB : MultiTransform](#42-bgr2rgb--multitransform)
    - [4.2.1 \_\_call\_\_](#421-\_\_call\_\_)
    - [4.2.2 \_\_init\_\_](#422-\_\_init\_\_)
  - [4.3 Brightness : MultiTransform](#43-brightness--multitransform)
    - [4.3.1 \_\_call\_\_](#431-\_\_call\_\_)
    - [4.3.2 \_\_init\_\_](#432-\_\_init\_\_)
  - [4.4 CenterCrop : MultiTransform](#44-centercrop--multitransform)
    - [4.4.1 \_\_call\_\_](#441-\_\_call\_\_)
    - [4.4.2 \_\_init\_\_](#442-\_\_init\_\_)
  - [4.5 Color : MultiTransform](#45-color--multitransform)
    - [4.5.1 \_\_call\_\_](#451-\_\_call\_\_)
    - [4.5.2 \_\_init\_\_](#452-\_\_init\_\_)
  - [4.6 Compose : builtins.object](#46-compose--builtinsobject)
    - [4.6.1 \_\_call\_\_](#461-\_\_call\_\_)
    - [4.6.2 \_\_init\_\_](#462-\_\_init\_\_)
  - [4.7 GaussianNoise : MultiTransform](#47-gaussiannoise--multitransform)
    - [4.7.1 \_\_call\_\_](#471-\_\_call\_\_)
    - [4.7.2 \_\_init\_\_](#472-\_\_init\_\_)
  - [4.8 MultiTransform : builtins.object](#48-multitransform--builtinsobject)
    - [4.8.1 \_\_call\_\_](#481-\_\_call\_\_)
    - [4.8.2 \_\_init\_\_](#482-\_\_init\_\_)
  - [4.9 Normalize : MultiTransform](#49-normalize--multitransform)
    - [4.9.1 \_\_call\_\_](#491-\_\_call\_\_)
    - [4.9.2 \_\_init\_\_](#492-\_\_init\_\_)
  - [4.10 RGB2BGR : BGR2RGB](#410-rgb2bgr--bgr2rgb)
    - [4.10.1 \_\_call\_\_](#4101-\_\_call\_\_)
    - [4.10.2 \_\_init\_\_](#4102-\_\_init\_\_)
  - [4.11 RandomCrop : MultiTransform](#411-randomcrop--multitransform)
    - [4.11.1 \_\_call\_\_](#4111-\_\_call\_\_)
    - [4.11.2 \_\_init\_\_](#4112-\_\_init\_\_)
  - [4.12 RandomHorizontalFlip : MultiTransform](#412-randomhorizontalflip--multitransform)
    - [4.12.1 \_\_call\_\_](#4121-\_\_call\_\_)
    - [4.12.2 \_\_init\_\_](#4122-\_\_init\_\_)
  - [4.13 RandomVerticalFlip : MultiTransform](#413-randomverticalflip--multitransform)
    - [4.13.1 \_\_call\_\_](#4131-\_\_call\_\_)
    - [4.13.2 \_\_init\_\_](#4132-\_\_init\_\_)
  - [4.14 Resize : MultiTransform](#414-resize--multitransform)
    - [4.14.1 \_\_call\_\_](#4141-\_\_call\_\_)
    - [4.14.2 \_\_init\_\_](#4142-\_\_init\_\_)
  - [4.15 Rotate : MultiTransform](#415-rotate--multitransform)
    - [4.15.1 \_\_call\_\_](#4151-\_\_call\_\_)
    - [4.15.2 \_\_init\_\_](#4152-\_\_init\_\_)
  - [4.16 Satturation : MultiTransform](#416-satturation--multitransform)
    - [4.16.1 \_\_call\_\_](#4161-\_\_call\_\_)
    - [4.16.2 \_\_init\_\_](#4162-\_\_init\_\_)
  - [4.17 Scale : MultiTransform](#417-scale--multitransform)
    - [4.17.1 \_\_call\_\_](#4171-\_\_call\_\_)
    - [4.17.2 \_\_init\_\_](#4172-\_\_init\_\_)
  - [4.18 Stack : MultiTransform](#418-stack--multitransform)
    - [4.18.1 \_\_call\_\_](#4181-\_\_call\_\_)
    - [4.18.2 \_\_init\_\_](#4182-\_\_init\_\_)
  - [4.19 ToCVImage : MultiTransform](#419-tocvimage--multitransform)
    - [4.19.1 \_\_call\_\_](#4191-\_\_call\_\_)
    - [4.19.2 \_\_init\_\_](#4192-\_\_init\_\_)
  - [4.20 ToNumpy : MultiTransform](#420-tonumpy--multitransform)
    - [4.20.1 \_\_call\_\_](#4201-\_\_call\_\_)
    - [4.20.2 \_\_init\_\_](#4202-\_\_init\_\_)
  - [4.21 ToPILImage : MultiTransform](#421-topilimage--multitransform)
    - [4.21.1 \_\_call\_\_](#4211-\_\_call\_\_)
    - [4.21.2 \_\_init\_\_](#4212-\_\_init\_\_)
  - [4.22 ToTensor : MultiTransform](#422-totensor--multitransform)
    - [4.22.1 \_\_call\_\_](#4221-\_\_call\_\_)
    - [4.22.2 \_\_init\_\_](#4222-\_\_init\_\_)
- [5 run](#5-run)
  - [5.1 Run : builtins.object](#51-run--builtinsobject)
    - [5.1.1 \_\_init\_\_](#511-\_\_init\_\_)
    - [5.1.2 append](#512-append)
    - [5.1.3 get\_avg](#513-get\_avg)
    - [5.1.4 get\_val](#514-get\_val)
    - [5.1.5 len](#515-len)
    - [5.1.6 load\_best\_state\_dict](#516-load\_best\_state\_dict)
    - [5.1.7 load\_state\_dict](#517-load\_state\_dict)
    - [5.1.8 pickle\_dump](#518-pickle\_dump)
    - [5.1.9 pickle\_load](#519-pickle\_load)
    - [5.1.10 plot](#5110-plot)
    - [5.1.11 recalculate\_moving\_average](#5111-recalculate\_moving\_average)
    - [5.1.12 save](#5112-save)
    - [5.1.13 save\_best\_state\_dict](#5113-save\_best\_state\_dict)
    - [5.1.14 save\_state\_dict](#5114-save\_state\_dict)
    - [5.1.15 train\_epoch](#5115-train\_epoch)
    - [5.1.16 validate\_epoch](#5116-validate\_epoch)




# 1 dataset

[TOC](#table-of-contents)



## 1.1 TUC\_AR : torch.utils.data.dataset.IterableDataset

[TOC](#table-of-contents)

**Description**

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

**Example**

```python
 from rsp.ml.dataset import TUC_AR
 
 transforms = multi_transforms.Compose([multi_transforms.Resize((400, 400))])
 tuc_ar_ds = TUC_AR(
               split='val',
               depth_channel=True,
               transforms=transforms,
               num_actions=10,
               streaming=True)
```
### 1.1.1 \_\_init\_\_

[TOC](#table-of-contents)

**Description**

Initializes a new instance.

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| split | str | Dataset split [train|val] |
| depth_channel | bool | Load depth channel. If set to `True`, the generated input tensor will have 4 channels instead of 3. (batch_size, sequence_length, __channels__, width, height) |
| num_actions | int, default = 7 | Number of action classes -> shape[1] of target tensor (batch_size, **num_actions**) |
| streaming | bool, default = False | If set to `True`, don't download the data files. Instead, it streams the data progressively while iterating on the dataset. |
| sequence_length | int, default = 30 | Length of each sequence. -> shape[1] of the generated input tensor. (batch_size, **sequence_length**, channels, width, height) |
| transforms | rsp.ml.multi_transforms.Compose = default = rsp.ml.multi_transforms.Compose([]) | Transformations, that will be applied to each input sequence. See documentation of `rsp.ml.multi_transforms` for more details. |
# 2 metrics

[TOC](#table-of-contents)

The module `rsp.ml.metrics` provides some functionality to quantify the quality of predictions.

## 2.1 AUROC

[TOC](#table-of-contents)

**Description**

Calculates the Area under the Receiver Operation Chracteristic Curve.

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| Y | torch.Tensor | Prediction |
| T | torch.Tensor | True values |
| num_thresholds | int, default = 100 | Number of thresholds to compute. |

**Returns**

Receiver Operation Chracteristic Area under the Curve : float

## 2.2 F1\_Score

[TOC](#table-of-contents)

**Description**

F1 Score. Expected input shape: (batch_size, num_classes)

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| Y | torch.Tensor | Prediction |
| T | torch.Tensor | True values |
| threshold | float | All values that are greater than or equal to the threshold are considered a positive class. |

**Returns**

F1 Score : float

**Equations**

$precision = \frac{TP}{TP + FP}$

$recall = \frac{TP}{TP + FN}$

$F_1 = \frac{2 \cdot precision \cdot recall}{precision + recall} = \frac{2 \cdot TP}{2 \cdot TP + FP + FN}$



**Example**

```python
import rsp.ml.metrics as m

Y = torch.tensor([
  [0.1, 0.1, 0.8],
  [0.03, 0.95, 0.02],
  [0.05, 0.9, 0.05],
  [0.01, 0.87, 0.12],
  [0.04, 0.03, 0.93],
  [0.94, 0.02, 0.06]
])
T = torch.tensor([
  [0, 0, 1],
  [1, 0, 0],
  [0, 1, 0],
  [0, 1, 0],
  [0, 0, 1],
  [1, 0, 0]
])

f1score = m.F1_Score(Y, T)

print(f1score) --> 0.5
```

## 2.3 FN

[TOC](#table-of-contents)

**Description**

False negatives. Expected input shape: (batch_size, num_classes)

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| Y | torch.Tensor | Prediction |
| T | torch.Tensor | True values |
| threshold | float | All values that are greater than or equal to the threshold are considered a positive class. |

**Returns**

False negatives : int

**Example**

```python
import rsp.ml.metrics as m
import torch

Y = torch.tensor([
  [0.1, 0.1, 0.8],
  [0.03, 0.95, 0.02],
  [0.05, 0.9, 0.05],
  [0.01, 0.87, 0.12],
  [0.04, 0.03, 0.93],
  [0.94, 0.02, 0.06]
])
T = torch.tensor([
  [0, 0, 1],
  [1, 0, 0],
  [0, 1, 0],
  [0, 1, 0],
  [0, 0, 1],
  [1, 0, 0]
])

fn = m.FN(Y, T)
print(fn) -> 1
```

## 2.4 FP

[TOC](#table-of-contents)

**Description**

False positives. Expected input shape: (batch_size, num_classes)

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| Y | torch.Tensor | Prediction |
| T | torch.Tensor | True values |
| threshold | float | All values that are greater than or equal to the threshold are considered a positive class. |

**Returns**

False positives : int

**Example**

```python
import rsp.ml.metrics as m
import torch

Y = torch.tensor([
  [0.1, 0.1, 0.8],
  [0.03, 0.95, 0.02],
  [0.05, 0.9, 0.05],
  [0.01, 0.87, 0.12],
  [0.04, 0.03, 0.93],
  [0.94, 0.02, 0.06]
])
T = torch.tensor([
  [0, 0, 1],
  [1, 0, 0],
  [0, 1, 0],
  [0, 1, 0],
  [0, 0, 1],
  [1, 0, 0]
])

fp = m.FP(Y, T)
print(fp) -> 1
```

## 2.5 FPR

[TOC](#table-of-contents)

**Description**

False positive rate. Expected input shape: (batch_size, num_classes)

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| Y | torch.Tensor | Prediction |
| T | torch.Tensor | True values |
| threshold | float | All values that are greater than or equal to the threshold are considered a positive class. |

**Returns**

False positive rate : float

**Example**

```python
import rsp.ml.metrics as m
import torch

Y = torch.tensor([
  [0.1, 0.1, 0.8],
  [0.03, 0.95, 0.02],
  [0.05, 0.9, 0.05],
  [0.01, 0.87, 0.12],
  [0.04, 0.03, 0.93],
  [0.94, 0.02, 0.06]
])
T = torch.tensor([
  [0, 0, 1],
  [1, 0, 0],
  [0, 1, 0],
  [0, 1, 0],
  [0, 0, 1],
  [1, 0, 0]
])

fpr = m.FPR(Y, T)
print(fpr) -> 0.08333333333333333
```

## 2.6 ROC

[TOC](#table-of-contents)

**Description**

Calculates the receiver operating characteristic: computes False Positive Rates and True positive Rates for `num_thresholds` aligned between 0 and 1

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| Y | torch.Tensor | Prediction |
| T | torch.Tensor | True values |
| num_thresholds | int, default = 100 | Number of thresholds to compute. |

**Returns**

(False Positive Rates, True Positive Rates) for 100 different thresholds : (List[float], List[float])

**Example**

```python
import rsp.ml.metrics as m
import torch
import torch.nn.functional as F

num_elements = 100000
num_classes = 7

T = []
for i in range(num_elements):
  true_class = torch.randint(0, num_classes, (1,))
  t = F.one_hot(true_class, num_classes=num_classes)
  T.append(t)
T = torch.cat(T)

dist = torch.normal(T.float(), 1.5)
Y = F.softmax(dist, dim = 1)
FPRs, TPRs = m.ROC(Y, T)
```

## 2.7 TN

[TOC](#table-of-contents)

**Description**

True negatives. Expected input shape: (batch_size, num_classes)

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| Y | torch.Tensor | Prediction |
| T | torch.Tensor | True values |
| threshold | float | All values that are greater than or equal to the threshold are considered a positive class. |

**Returns**

True negatives : int

**Example**

```python
import rsp.ml.metrics as m
import torch

Y = torch.tensor([
  [0.1, 0.1, 0.8],
  [0.03, 0.95, 0.02],
  [0.05, 0.9, 0.05],
  [0.01, 0.87, 0.12],
  [0.04, 0.03, 0.93],
  [0.94, 0.02, 0.06]
])
T = torch.tensor([
  [0, 0, 1],
  [1, 0, 0],
  [0, 1, 0],
  [0, 1, 0],
  [0, 0, 1],
  [1, 0, 0]
])

tn = m.TN(Y, T)
print(tn) -> 11
```

## 2.8 TP

[TOC](#table-of-contents)

**Description**

True positives. Expected input shape: (batch_size, num_classes)

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| Y | torch.Tensor | Prediction |
| T | torch.Tensor | True values |
| threshold | float | All values that are greater than or equal to the threshold are considered a positive class. |

**Returns**

True positives : int

**Example**

```python
import rsp.ml.metrics as m
import torch

Y = torch.tensor([
  [0.1, 0.1, 0.8],
  [0.03, 0.95, 0.02],
  [0.05, 0.9, 0.05],
  [0.01, 0.87, 0.12],
  [0.04, 0.03, 0.93],
  [0.94, 0.02, 0.06]
])
T = torch.tensor([
  [0, 0, 1],
  [1, 0, 0],
  [0, 1, 0],
  [0, 1, 0],
  [0, 0, 1],
  [1, 0, 0]
])

tp = m.TP(Y, T)
print(tp) -> 5
```

## 2.9 TPR

[TOC](#table-of-contents)

**Description**

True positive rate. Expected input shape: (batch_size, num_classes)

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| Y | torch.Tensor | Prediction |
| T | torch.Tensor | True values |
| threshold | float | All values that are greater than or equal to the threshold are considered a positive class. |

**Returns**

True positive rate : float

**Example**

```python
import rsp.ml.metrics as m
import torch

Y = torch.tensor([
  [0.1, 0.1, 0.8],
  [0.03, 0.95, 0.02],
  [0.05, 0.9, 0.05],
  [0.01, 0.87, 0.12],
  [0.04, 0.03, 0.93],
  [0.94, 0.02, 0.06]
])
T = torch.tensor([
  [0, 0, 1],
  [1, 0, 0],
  [0, 1, 0],
  [0, 1, 0],
  [0, 0, 1],
  [1, 0, 0]
])

tpr = m.TPR(Y, T)
print(tpr) -> 0.8333333333333334
```

## 2.10 confusion\_matrix

[TOC](#table-of-contents)

**Description**

Calculates the confusion matrix. Expected input shape: (batch_size, num_classes)

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| Y | torch.Tensor | Prediction |
| T | torch.Tensor | True values |

**Returns**

Confusion matrix : torch.Tensor

**Example**

```python
import rsp.ml.metrics as m
import torch

Y = torch.tensor([
  [0.1, 0.1, 0.8],
  [0.03, 0.95, 0.02],
  [0.05, 0.9, 0.05],
  [0.01, 0.87, 0.12],
  [0.04, 0.03, 0.93],
  [0.94, 0.02, 0.06]
])
T = torch.tensor([
  [0, 0, 1],
  [1, 0, 0],
  [0, 1, 0],
  [0, 1, 0],
  [0, 0, 1],
  [1, 0, 0]
])

conf_mat = m.confusion_matrix(Y, T)
print(conf_mat) -> tensor([
  [1, 1, 0],
  [0, 2, 0],
  [0, 0, 2]
])
```

## 2.11 plot\_ROC

[TOC](#table-of-contents)

**Description**

Plot the receiver operating characteristic.

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| Y | torch.Tensor | Prediction |
| T | torch.Tensor | True values |
| num_thresholds | int, default = 100 | Number of thresholds to compute. |
| title | str, optional, default = 'Confusion Matrix' | Title of the plot |
| class_curves | bool, default = False | Plot ROC curve for each class |
| labels | str, optional, default = None | Class labels -> automatic labeling C000, ..., CXXX if labels is None |
| plt_show | bool, optional, default = False | Set to True to show the plot |
| save_file_name | str, optional, default = None | If not None, the plot is saved under the specified save_file_name. |

**Returns**

Image of the confusion matrix : np.array

![](documentation/image/ROC_AUC.jpg)
## 2.12 plot\_confusion\_matrix

[TOC](#table-of-contents)

**Description**

Plot the confusion matrix

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| confusion_matrix | torch.Tensor | Confusion matrix |
| labels | str, optional, default = None | Class labels -> automatic labeling C000, ..., CXXX if labels is None |
| cmap | str, optional, default = 'Blues' | Seaborn cmap, see https://r02b.github.io/seaborn_palettes/ |
| xlabel | str, optional, default = 'Predicted label' | X-Axis label |
| ylabel | str, optional, default = 'True label' | Y-Axis label |
| title | str, optional, default = 'Confusion Matrix' | Title of the plot |
| plt_show | bool, optional, default = False | Set to True to show the plot |
| save_file_name | str, optional, default = None | If not None, the plot is saved under the specified save_file_name. |

**Returns**

Image of the confusion matrix : np.array

![](documentation/image/confusion_matrix.jpg)
## 2.13 precision

[TOC](#table-of-contents)

**Description**

Precision. Expected input shape: (batch_size, num_classes)

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| Y | torch.Tensor | Prediction |
| T | torch.Tensor | True values |
| threshold | float | All values that are greater than or equal to the threshold are considered a positive class. |

**Returns**

Precision : float

**Equations**

$precision = \frac{TP}{TP + FP}$



**Example**

```python
import rsp.ml.metrics as m
import torch

Y = torch.tensor([
  [0.1, 0.1, 0.8],
  [0.03, 0.95, 0.02],
  [0.05, 0.9, 0.05],
  [0.01, 0.87, 0.12],
  [0.04, 0.03, 0.93],
  [0.94, 0.02, 0.06]
])
T = torch.tensor([
  [0, 0, 1],
  [1, 0, 0],
  [0, 1, 0],
  [0, 1, 0],
  [0, 0, 1],
  [1, 0, 0]
])

precision = m.precision(Y, T)
print(precision) -> 0.8333333333333334
```

## 2.14 recall

[TOC](#table-of-contents)

**Description**

Recall. Expected input shape: (batch_size, num_classes)

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| Y | torch.Tensor | Prediction |
| T | torch.Tensor | True values |
| threshold | float | All values that are greater than or equal to the threshold are considered a positive class. |

**Returns**

Recall : float

**Equations**

$recall = \frac{TP}{TP + FN}$



**Example**

```python
import rsp.ml.metrics as m
import torch

Y = torch.tensor([
  [0.1, 0.1, 0.8],
  [0.03, 0.95, 0.02],
  [0.05, 0.9, 0.05],
  [0.01, 0.87, 0.12],
  [0.04, 0.03, 0.93],
  [0.94, 0.02, 0.06]
])
T = torch.tensor([
  [0, 0, 1],
  [1, 0, 0],
  [0, 1, 0],
  [0, 1, 0],
  [0, 0, 1],
  [1, 0, 0]
])

recall = m.recall(Y, T)
print(recall) -> 0.8333333333333334
```

## 2.15 top\_10\_accuracy

[TOC](#table-of-contents)

**Description**

Top 10 accuracy. Expected input shape: (batch_size, num_classes)

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| Y | torch.Tensor | Prediction |
| T | torch.Tensor | True values |

**Returns**

Top 10 accuracy -> top k accuracy | k = 10 : float

**Example**

```python
import rsp.ml.metrics as m

Y = torch.tensor([
  [0.1, 0.1, 0.8],
  [0.03, 0.95, 0.02],
  [0.05, 0.9, 0.05],
  [0.01, 0.87, 0.12],
  [0.04, 0.03, 0.93],
  [0.94, 0.02, 0.06]
])
T = torch.tensor([
  [0, 0, 1],
  [1, 0, 0],
  [0, 1, 0],
  [0, 1, 0],
  [0, 0, 1],
  [1, 0, 0]
])

top_10_accuracy = m.top_10_accuracy(Y, T, k = 3)

print(top_10_accuracy) --> 1.0
```

## 2.16 top\_1\_accuracy

[TOC](#table-of-contents)

**Description**

Top 1 accuracy. Expected input shape: (batch_size, num_classes)

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| Y | torch.Tensor | Prediction |
| T | torch.Tensor | True values |

**Returns**

Top 1 accuracy -> top k accuracy | k = 1 : float

**Example**

```python
import rsp.ml.metrics as m

Y = torch.tensor([
  [0.1, 0.1, 0.8],
  [0.03, 0.95, 0.02],
  [0.05, 0.9, 0.05],
  [0.01, 0.87, 0.12],
  [0.04, 0.03, 0.93],
  [0.94, 0.02, 0.06]
])
T = torch.tensor([
  [0, 0, 1],
  [1, 0, 0],
  [0, 1, 0],
  [0, 1, 0],
  [0, 0, 1],
  [1, 0, 0]
])

top_1_accuracy = m.top_1_accuracy(Y, T, k = 3)

print(top_1_accuracy) --> 0.8333333333333334
```

## 2.17 top\_2\_accuracy

[TOC](#table-of-contents)

**Description**

Top 2 accuracy. Expected input shape: (batch_size, num_classes)

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| Y | torch.Tensor | Prediction |
| T | torch.Tensor | True values |

**Returns**

Top 2 accuracy -> top k accuracy | k = 2 : float

**Example**

```python
import rsp.ml.metrics as m

Y = torch.tensor([
  [0.1, 0.1, 0.8],
  [0.03, 0.95, 0.02],
  [0.05, 0.9, 0.05],
  [0.01, 0.87, 0.12],
  [0.04, 0.03, 0.93],
  [0.94, 0.02, 0.06]
])
T = torch.tensor([
  [0, 0, 1],
  [1, 0, 0],
  [0, 1, 0],
  [0, 1, 0],
  [0, 0, 1],
  [1, 0, 0]
])

top_2_accuracy = m.top_2_accuracy(Y, T, k = 3)

print(top_2_accuracy) --> 1.0
```

## 2.18 top\_3\_accuracy

[TOC](#table-of-contents)

**Description**

Top 3 accuracy. Expected input shape: (batch_size, num_classes)

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| Y | torch.Tensor | Prediction |
| T | torch.Tensor | True values |

**Returns**

Top 3 accuracy -> top k accuracy | k = 3 : float

**Example**

```python
import rsp.ml.metrics as m

Y = torch.tensor([
  [0.1, 0.1, 0.8],
  [0.03, 0.95, 0.02],
  [0.05, 0.9, 0.05],
  [0.01, 0.87, 0.12],
  [0.04, 0.03, 0.93],
  [0.94, 0.02, 0.06]
])
T = torch.tensor([
  [0, 0, 1],
  [1, 0, 0],
  [0, 1, 0],
  [0, 1, 0],
  [0, 0, 1],
  [1, 0, 0]
])

top_3_accuracy = m.top_3_accuracy(Y, T, k = 3)

print(top_3_accuracy) --> 1.0
```

## 2.19 top\_5\_accuracy

[TOC](#table-of-contents)

**Description**

Top 5 accuracy. Expected input shape: (batch_size, num_classes)

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| Y | torch.Tensor | Prediction |
| T | torch.Tensor | True values |

**Returns**

Top 5 accuracy -> top k accuracy | k = 5 : float

**Example**

```python
import rsp.ml.metrics as m

Y = torch.tensor([
  [0.1, 0.1, 0.8],
  [0.03, 0.95, 0.02],
  [0.05, 0.9, 0.05],
  [0.01, 0.87, 0.12],
  [0.04, 0.03, 0.93],
  [0.94, 0.02, 0.06]
])
T = torch.tensor([
  [0, 0, 1],
  [1, 0, 0],
  [0, 1, 0],
  [0, 1, 0],
  [0, 0, 1],
  [1, 0, 0]
])

top_5_accuracy = m.top_5_accuracy(Y, T, k = 3)

print(top_5_accuracy) --> 1.0
```

## 2.20 top\_k\_accuracy

[TOC](#table-of-contents)

**Description**

Top k accuracy. Expected input shape: (batch_size, num_classes)

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| Y | torch.Tensor | Prediction |
| T | torch.Tensor | True values |

**Returns**

Top k accuracy : float

**Example**

```python
import rsp.ml.metrics as m

Y = torch.tensor([
  [0.1, 0.1, 0.8],
  [0.03, 0.95, 0.02],
  [0.05, 0.9, 0.05],
  [0.01, 0.87, 0.12],
  [0.04, 0.03, 0.93],
  [0.94, 0.02, 0.06]
])
T = torch.tensor([
  [0, 0, 1],
  [1, 0, 0],
  [0, 1, 0],
  [0, 1, 0],
  [0, 0, 1],
  [1, 0, 0]
])

top_k_accuracy = m.top_k_accuracy(Y, T, k = 3)

print(top_k_accuracy) --> 1.0
```

# 3 model

[TOC](#table-of-contents)

The module `rsp.ml.model` provides some usefull functionality to store and load pytorch models.

## 3.1 MODELS : enum.Enum

[TOC](#table-of-contents)

**Description**

Create a collection of name/value pairs.

Example enumeration:

>>> class Color(Enum):
...     RED = 1
...     BLUE = 2
...     GREEN = 3

Access them by:

- attribute access::

>>> Color.RED
<Color.RED: 1>

- value lookup:

>>> Color(1)
<Color.RED: 1>

- name lookup:

>>> Color['RED']
<Color.RED: 1>

Enumerations can be iterated over, and know how many members they have:

>>> len(Color)
3

>>> list(Color)
[<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]

Methods can be added to enumerations, and members can have their own
attributes -- see the documentation for details.


## 3.2 WEIGHTS : enum.Enum

[TOC](#table-of-contents)

**Description**

Create a collection of name/value pairs.

Example enumeration:

>>> class Color(Enum):
...     RED = 1
...     BLUE = 2
...     GREEN = 3

Access them by:

- attribute access::

>>> Color.RED
<Color.RED: 1>

- value lookup:

>>> Color(1)
<Color.RED: 1>

- name lookup:

>>> Color['RED']
<Color.RED: 1>

Enumerations can be iterated over, and know how many members they have:

>>> len(Color)
3

>>> list(Color)
[<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]

Methods can be added to enumerations, and members can have their own
attributes -- see the documentation for details.


## 3.3 list\_model\_weights

[TOC](#table-of-contents)

**Description**

Lists all available weight files.


**Returns**

List of (MODEL:str, WEIGHT:str) : List[Tuple(str, str)]

**Example**

```python
import rsp.ml.model as model

model_weight_files = model.list_model_weights()
```

## 3.4 load\_model

[TOC](#table-of-contents)

**Description**

Loads a pretrained PyTorch model from HuggingFace.

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| model | MODELS | ID of the model |
| weights | WEIGHTS | ID of the weights |

**Returns**

Pretrained PyTorch model : torch.nn.Module

**Example**

```python
import rsp.ml.model as model

action_recognition_model = model.load_model(MODEL.TUCARC3D, WEIGHTS.TUCAR)
```

## 3.5 publish\_model

[TOC](#table-of-contents)

# 4 multi\_transforms

[TOC](#table-of-contents)

The module `rsp.ml.multi_transforms` is based on `torchvision.transforms`, which is made for single images. `rsp.ml.multi_transforms` extends this functionality by providing transformations for sequences of images, which could be usefull for video augmentation.

## 4.1 BGR2GRAY : MultiTransform

[TOC](#table-of-contents)

**Description**

Converts a sequence of BGR images to grayscale images.


### 4.1.1 \_\_call\_\_

[TOC](#table-of-contents)

**Description**

Call self as a function.

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| input | torch.Tensor<br>List[PIL.Image]<br>List[numpy.array] | Sequence of images |
### 4.1.2 \_\_init\_\_

[TOC](#table-of-contents)

**Description**

Initializes a new instance.

## 4.2 BGR2RGB : MultiTransform

[TOC](#table-of-contents)

**Description**

Converts sequence of BGR images to RGB images.


### 4.2.1 \_\_call\_\_

[TOC](#table-of-contents)

**Description**

Call self as a function.

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| input | torch.Tensor<br>List[PIL.Image]<br>List[numpy.array] | Sequence of images |
### 4.2.2 \_\_init\_\_

[TOC](#table-of-contents)

**Description**

Initializes a new instance.

## 4.3 Brightness : MultiTransform

[TOC](#table-of-contents)

**Description**

MultiTransform is an extension to keep the same transformation over a sequence of images instead of initializing a new transformation for every single image. It is inspired by `torchvision.transforms` and could be used for video augmentation. Use `rsp.ml.multi_transforms.Compose`to combine multiple image sequence transformations.

> **Note** `rsp.ml.multi_transforms.MultiTransform` is a base class and should be inherited.


### 4.3.1 \_\_call\_\_

[TOC](#table-of-contents)

**Description**

Call self as a function.

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| input | torch.Tensor<br>List[PIL.Image]<br>List[numpy.array] | Sequence of images |
### 4.3.2 \_\_init\_\_

[TOC](#table-of-contents)

**Description**

Initializes a new instance.

## 4.4 CenterCrop : MultiTransform

[TOC](#table-of-contents)

**Description**

Crops Images at the center after upscaling them. Dimensions kept the same.

![](documentation/image/multi_transforms.CenterCrop.png)


### 4.4.1 \_\_call\_\_

[TOC](#table-of-contents)

**Description**

Call self as a function.

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| input | torch.Tensor<br>List[PIL.Image]<br>List[numpy.array] | Sequence of images |
### 4.4.2 \_\_init\_\_

[TOC](#table-of-contents)

**Description**

Initializes a new instance.

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| max_scale | float | Images are scaled randomly between 1. and max_scale before cropping to original size. |
## 4.5 Color : MultiTransform

[TOC](#table-of-contents)

**Description**

MultiTransform is an extension to keep the same transformation over a sequence of images instead of initializing a new transformation for every single image. It is inspired by `torchvision.transforms` and could be used for video augmentation. Use `rsp.ml.multi_transforms.Compose`to combine multiple image sequence transformations.

> **Note** `rsp.ml.multi_transforms.MultiTransform` is a base class and should be inherited.


### 4.5.1 \_\_call\_\_

[TOC](#table-of-contents)

**Description**

Call self as a function.

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| input | torch.Tensor<br>List[PIL.Image]<br>List[numpy.array] | Sequence of images |
### 4.5.2 \_\_init\_\_

[TOC](#table-of-contents)

**Description**

Initializes a new instance.

## 4.6 Compose : builtins.object

[TOC](#table-of-contents)

**Description**

Composes several MultiTransforms together.

**Example**

```python
import rsp.ml.multi_transforms as t

transforms = t.Compose([
  t.BGR2GRAY(),
  t.Scale(0.5)
])
```
### 4.6.1 \_\_call\_\_

[TOC](#table-of-contents)

**Description**

Call self as a function.

### 4.6.2 \_\_init\_\_

[TOC](#table-of-contents)

**Description**

Initializes a new instance.

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| children | List[MultiTransform] | List of MultiTransforms to compose. |
## 4.7 GaussianNoise : MultiTransform

[TOC](#table-of-contents)

**Description**

MultiTransform is an extension to keep the same transformation over a sequence of images instead of initializing a new transformation for every single image. It is inspired by `torchvision.transforms` and could be used for video augmentation. Use `rsp.ml.multi_transforms.Compose`to combine multiple image sequence transformations.

> **Note** `rsp.ml.multi_transforms.MultiTransform` is a base class and should be inherited.


### 4.7.1 \_\_call\_\_

[TOC](#table-of-contents)

**Description**

Call self as a function.

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| input | torch.Tensor<br>List[PIL.Image]<br>List[numpy.array] | Sequence of images |
### 4.7.2 \_\_init\_\_

[TOC](#table-of-contents)

**Description**

Initializes a new instance.

## 4.8 MultiTransform : builtins.object

[TOC](#table-of-contents)

**Description**

MultiTransform is an extension to keep the same transformation over a sequence of images instead of initializing a new transformation for every single image. It is inspired by `torchvision.transforms` and could be used for video augmentation. Use `rsp.ml.multi_transforms.Compose`to combine multiple image sequence transformations.

> **Note** `rsp.ml.multi_transforms.MultiTransform` is a base class and should be inherited.


### 4.8.1 \_\_call\_\_

[TOC](#table-of-contents)

**Description**

Call self as a function.

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| input | torch.Tensor<br>List[PIL.Image]<br>List[numpy.array] | Sequence of images |
### 4.8.2 \_\_init\_\_

[TOC](#table-of-contents)

**Description**

Initializes a new instance.

## 4.9 Normalize : MultiTransform

[TOC](#table-of-contents)

**Description**

Normalize images with mean and standard deviation. Given mean: (mean[1],...,mean[n]) and std: (std[1],..,std[n]) for n channels, this transform will normalize each channel of the input torch.*Tensor i.e., output[channel] = (input[channel] - mean[channel]) / std[channel]

> Based on torchvision.transforms.Normalize


### 4.9.1 \_\_call\_\_

[TOC](#table-of-contents)

**Description**

Call self as a function.

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| input | torch.Tensor<br>List[PIL.Image]<br>List[numpy.array] | Sequence of images |
### 4.9.2 \_\_init\_\_

[TOC](#table-of-contents)

**Description**

Initializes a new instance.

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| mean | List[float] | Sequence of means for each channel. |
| std | List[float] | Sequence of standard deviations for each channel. |
| inplace | bool | Set to True make this operation in-place. |
## 4.10 RGB2BGR : BGR2RGB

[TOC](#table-of-contents)

**Description**

Converts sequence of RGB images to BGR images.


### 4.10.1 \_\_call\_\_

[TOC](#table-of-contents)

**Description**

Call self as a function.

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| input | torch.Tensor<br>List[PIL.Image]<br>List[numpy.array] | Sequence of images |
### 4.10.2 \_\_init\_\_

[TOC](#table-of-contents)

**Description**

Initializes a new instance.

## 4.11 RandomCrop : MultiTransform

[TOC](#table-of-contents)

**Description**

Crops Images at a random location after upscaling them. Dimensions kept the same.

![](documentation/image/multi_transforms.RandomCrop.png)


### 4.11.1 \_\_call\_\_

[TOC](#table-of-contents)

**Description**

Call self as a function.

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| input | torch.Tensor<br>List[PIL.Image]<br>List[numpy.array] | Sequence of images |
### 4.11.2 \_\_init\_\_

[TOC](#table-of-contents)

**Description**

Initializes a new instance.

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| max_scale | float | Images are scaled randomly between 1. and max_scale before cropping to original size. |
## 4.12 RandomHorizontalFlip : MultiTransform

[TOC](#table-of-contents)

**Description**

MultiTransform is an extension to keep the same transformation over a sequence of images instead of initializing a new transformation for every single image. It is inspired by `torchvision.transforms` and could be used for video augmentation. Use `rsp.ml.multi_transforms.Compose`to combine multiple image sequence transformations.

> **Note** `rsp.ml.multi_transforms.MultiTransform` is a base class and should be inherited.


### 4.12.1 \_\_call\_\_

[TOC](#table-of-contents)

**Description**

Call self as a function.

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| input | torch.Tensor<br>List[PIL.Image]<br>List[numpy.array] | Sequence of images |
### 4.12.2 \_\_init\_\_

[TOC](#table-of-contents)

**Description**

Initializes a new instance.

## 4.13 RandomVerticalFlip : MultiTransform

[TOC](#table-of-contents)

**Description**

MultiTransform is an extension to keep the same transformation over a sequence of images instead of initializing a new transformation for every single image. It is inspired by `torchvision.transforms` and could be used for video augmentation. Use `rsp.ml.multi_transforms.Compose`to combine multiple image sequence transformations.

> **Note** `rsp.ml.multi_transforms.MultiTransform` is a base class and should be inherited.


### 4.13.1 \_\_call\_\_

[TOC](#table-of-contents)

**Description**

Call self as a function.

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| input | torch.Tensor<br>List[PIL.Image]<br>List[numpy.array] | Sequence of images |
### 4.13.2 \_\_init\_\_

[TOC](#table-of-contents)

**Description**

Initializes a new instance.

## 4.14 Resize : MultiTransform

[TOC](#table-of-contents)

**Description**

MultiTransform is an extension to keep the same transformation over a sequence of images instead of initializing a new transformation for every single image. It is inspired by `torchvision.transforms` and could be used for video augmentation. Use `rsp.ml.multi_transforms.Compose`to combine multiple image sequence transformations.

> **Note** `rsp.ml.multi_transforms.MultiTransform` is a base class and should be inherited.


### 4.14.1 \_\_call\_\_

[TOC](#table-of-contents)

**Description**

Call self as a function.

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| input | torch.Tensor<br>List[PIL.Image]<br>List[numpy.array] | Sequence of images |
### 4.14.2 \_\_init\_\_

[TOC](#table-of-contents)

**Description**

Initializes a new instance.

## 4.15 Rotate : MultiTransform

[TOC](#table-of-contents)

**Description**

Randomly rotates images.

**Equations**

$angle = -max\_angle + 2 \cdot random() \cdot max\_angle$

![](documentation/image/multi_transforms.Rotate.png)


### 4.15.1 \_\_call\_\_

[TOC](#table-of-contents)

**Description**

Call self as a function.

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| input | torch.Tensor<br>List[PIL.Image]<br>List[numpy.array] | Sequence of images |
### 4.15.2 \_\_init\_\_

[TOC](#table-of-contents)

**Description**

Iitializes a new instance.

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| max_angle | float | Maximal rotation in degrees | -max_angle <= rotate <= max_angle |
| auto_scale | bool, default = True | Image will be resized when auto scale is activated to avoid black margins. |
## 4.16 Satturation : MultiTransform

[TOC](#table-of-contents)

**Description**

MultiTransform is an extension to keep the same transformation over a sequence of images instead of initializing a new transformation for every single image. It is inspired by `torchvision.transforms` and could be used for video augmentation. Use `rsp.ml.multi_transforms.Compose`to combine multiple image sequence transformations.

> **Note** `rsp.ml.multi_transforms.MultiTransform` is a base class and should be inherited.


### 4.16.1 \_\_call\_\_

[TOC](#table-of-contents)

**Description**

Call self as a function.

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| input | torch.Tensor<br>List[PIL.Image]<br>List[numpy.array] | Sequence of images |
### 4.16.2 \_\_init\_\_

[TOC](#table-of-contents)

**Description**

Initializes a new instance.

## 4.17 Scale : MultiTransform

[TOC](#table-of-contents)

**Description**

MultiTransform is an extension to keep the same transformation over a sequence of images instead of initializing a new transformation for every single image. It is inspired by `torchvision.transforms` and could be used for video augmentation. Use `rsp.ml.multi_transforms.Compose`to combine multiple image sequence transformations.

> **Note** `rsp.ml.multi_transforms.MultiTransform` is a base class and should be inherited.


### 4.17.1 \_\_call\_\_

[TOC](#table-of-contents)

**Description**

Call self as a function.

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| input | torch.Tensor<br>List[PIL.Image]<br>List[numpy.array] | Sequence of images |
### 4.17.2 \_\_init\_\_

[TOC](#table-of-contents)

**Description**

Initializes a new instance.

## 4.18 Stack : MultiTransform

[TOC](#table-of-contents)

**Description**

MultiTransform is an extension to keep the same transformation over a sequence of images instead of initializing a new transformation for every single image. It is inspired by `torchvision.transforms` and could be used for video augmentation. Use `rsp.ml.multi_transforms.Compose`to combine multiple image sequence transformations.

> **Note** `rsp.ml.multi_transforms.MultiTransform` is a base class and should be inherited.


### 4.18.1 \_\_call\_\_

[TOC](#table-of-contents)

**Description**

Call self as a function.

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| input | torch.Tensor<br>List[PIL.Image]<br>List[numpy.array] | Sequence of images |
### 4.18.2 \_\_init\_\_

[TOC](#table-of-contents)

**Description**

Initializes a new instance.

## 4.19 ToCVImage : MultiTransform

[TOC](#table-of-contents)

**Description**

Converts a `torch.Tensor`to Open CV image by changing dimensions (d0, d1, d2) -> (d1, d2, d0) and converting `torch.Tensor` to `numpy`.


### 4.19.1 \_\_call\_\_

[TOC](#table-of-contents)

**Description**

Call self as a function.

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| input | torch.Tensor<br>List[PIL.Image]<br>List[numpy.array] | Sequence of images |
### 4.19.2 \_\_init\_\_

[TOC](#table-of-contents)

**Description**

Initializes a new instance.

## 4.20 ToNumpy : MultiTransform

[TOC](#table-of-contents)

**Description**

Converts a `torch.Tensor`to `numpy`


### 4.20.1 \_\_call\_\_

[TOC](#table-of-contents)

**Description**

Call self as a function.

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| input | torch.Tensor<br>List[PIL.Image]<br>List[numpy.array] | Sequence of images |
### 4.20.2 \_\_init\_\_

[TOC](#table-of-contents)

**Description**

Initializes a new instance.

## 4.21 ToPILImage : MultiTransform

[TOC](#table-of-contents)

**Description**

Converts sequence of images to sequence of `PIL.Image`.


### 4.21.1 \_\_call\_\_

[TOC](#table-of-contents)

**Description**

Call self as a function.

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| input | torch.Tensor<br>List[PIL.Image]<br>List[numpy.array] | Sequence of images |
### 4.21.2 \_\_init\_\_

[TOC](#table-of-contents)

**Description**

Initializes a new instance.

## 4.22 ToTensor : MultiTransform

[TOC](#table-of-contents)

**Description**

Converts a sequence of images to torch.Tensor.


### 4.22.1 \_\_call\_\_

[TOC](#table-of-contents)

**Description**

Call self as a function.

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| input | torch.Tensor<br>List[PIL.Image]<br>List[numpy.array] | Sequence of images |
### 4.22.2 \_\_init\_\_

[TOC](#table-of-contents)

**Description**

Initializes a new instance.

# 5 run

[TOC](#table-of-contents)

The module `rsp.ml.run` provides some tools for storing, loading and visualizing data during training of models using PyTorch. 

## 5.1 Run : builtins.object

[TOC](#table-of-contents)


### 5.1.1 \_\_init\_\_

[TOC](#table-of-contents)

**Description**

Initialize self.  See help(type(self)) for accurate signature.

### 5.1.2 append

[TOC](#table-of-contents)

### 5.1.3 get\_avg

[TOC](#table-of-contents)

### 5.1.4 get\_val

[TOC](#table-of-contents)

### 5.1.5 len

[TOC](#table-of-contents)

### 5.1.6 load\_best\_state\_dict

[TOC](#table-of-contents)

### 5.1.7 load\_state\_dict

[TOC](#table-of-contents)

### 5.1.8 pickle\_dump

[TOC](#table-of-contents)

### 5.1.9 pickle\_load

[TOC](#table-of-contents)

### 5.1.10 plot

[TOC](#table-of-contents)

### 5.1.11 recalculate\_moving\_average

[TOC](#table-of-contents)

### 5.1.12 save

[TOC](#table-of-contents)

### 5.1.13 save\_best\_state\_dict

[TOC](#table-of-contents)

### 5.1.14 save\_state\_dict

[TOC](#table-of-contents)

### 5.1.15 train\_epoch

[TOC](#table-of-contents)

### 5.1.16 validate\_epoch

[TOC](#table-of-contents)

