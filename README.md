# Table of Contents

- [1 metrics](#1-metrics)
  - [1.1 F1\_Score](#11-f1\_score)
  - [1.2 FN](#12-fn)
  - [1.3 FP](#13-fp)
  - [1.4 FPR](#14-fpr)
  - [1.5 TN](#15-tn)
  - [1.6 TP](#16-tp)
  - [1.7 TPR](#17-tpr)
  - [1.8 confusion](#18-confusion)
  - [1.9 confusion\_matrix](#19-confusion\_matrix)
  - [1.10 plot\_confusion\_matrix](#110-plot\_confusion\_matrix)
  - [1.11 precision](#111-precision)
  - [1.12 recall](#112-recall)
  - [1.13 top\_10\_accuracy](#113-top\_10\_accuracy)
  - [1.14 top\_1\_accuracy](#114-top\_1\_accuracy)
  - [1.15 top\_2\_accuracy](#115-top\_2\_accuracy)
  - [1.16 top\_3\_accuracy](#116-top\_3\_accuracy)
  - [1.17 top\_5\_accuracy](#117-top\_5\_accuracy)
  - [1.18 top\_k\_accuracy](#118-top\_k\_accuracy)
- [2 model](#2-model)
  - [2.2 Constants](#22-constants)
  - [2.1 load\_model](#21-load\_model)
- [3 multi\_transforms](#3-multi\_transforms)
  - [3.1 BGR2GRAY](#31-bgr2gray)
    - [3.1.1 \_\_call\_\_](#311-\_\_call\_\_)
    - [3.1.2 \_\_init\_\_](#312-\_\_init\_\_)
  - [3.2 BGR2RGB](#32-bgr2rgb)
    - [3.2.1 \_\_call\_\_](#321-\_\_call\_\_)
    - [3.2.2 \_\_init\_\_](#322-\_\_init\_\_)
  - [3.3 Brightness](#33-brightness)
    - [3.3.1 \_\_call\_\_](#331-\_\_call\_\_)
    - [3.3.2 \_\_init\_\_](#332-\_\_init\_\_)
  - [3.4 CenterCrop](#34-centercrop)
    - [3.4.1 \_\_call\_\_](#341-\_\_call\_\_)
    - [3.4.2 \_\_init\_\_](#342-\_\_init\_\_)
  - [3.5 Color](#35-color)
    - [3.5.1 \_\_call\_\_](#351-\_\_call\_\_)
    - [3.5.2 \_\_init\_\_](#352-\_\_init\_\_)
  - [3.6 Compose](#36-compose)
    - [3.6.1 \_\_call\_\_](#361-\_\_call\_\_)
    - [3.6.2 \_\_init\_\_](#362-\_\_init\_\_)
  - [3.7 GaussianNoise](#37-gaussiannoise)
    - [3.7.1 \_\_call\_\_](#371-\_\_call\_\_)
    - [3.7.2 \_\_init\_\_](#372-\_\_init\_\_)
  - [3.8 MultiTransform](#38-multitransform)
    - [3.8.1 \_\_call\_\_](#381-\_\_call\_\_)
    - [3.8.2 \_\_init\_\_](#382-\_\_init\_\_)
  - [3.9 Normalize](#39-normalize)
    - [3.9.1 \_\_call\_\_](#391-\_\_call\_\_)
    - [3.9.2 \_\_init\_\_](#392-\_\_init\_\_)
  - [3.10 RGB2BGR](#310-rgb2bgr)
    - [3.10.1 \_\_call\_\_](#3101-\_\_call\_\_)
    - [3.10.2 \_\_init\_\_](#3102-\_\_init\_\_)
  - [3.11 RandomCrop](#311-randomcrop)
    - [3.11.1 \_\_call\_\_](#3111-\_\_call\_\_)
    - [3.11.2 \_\_init\_\_](#3112-\_\_init\_\_)
  - [3.12 RandomHorizontalFlip](#312-randomhorizontalflip)
    - [3.12.1 \_\_call\_\_](#3121-\_\_call\_\_)
    - [3.12.2 \_\_init\_\_](#3122-\_\_init\_\_)
  - [3.13 RandomVerticalFlip](#313-randomverticalflip)
    - [3.13.1 \_\_call\_\_](#3131-\_\_call\_\_)
    - [3.13.2 \_\_init\_\_](#3132-\_\_init\_\_)
  - [3.14 Resize](#314-resize)
    - [3.14.1 \_\_call\_\_](#3141-\_\_call\_\_)
    - [3.14.2 \_\_init\_\_](#3142-\_\_init\_\_)
  - [3.15 Rotate](#315-rotate)
    - [3.15.1 \_\_call\_\_](#3151-\_\_call\_\_)
    - [3.15.2 \_\_init\_\_](#3152-\_\_init\_\_)
  - [3.16 Satturation](#316-satturation)
    - [3.16.1 \_\_call\_\_](#3161-\_\_call\_\_)
    - [3.16.2 \_\_init\_\_](#3162-\_\_init\_\_)
  - [3.17 Scale](#317-scale)
    - [3.17.1 \_\_call\_\_](#3171-\_\_call\_\_)
    - [3.17.2 \_\_init\_\_](#3172-\_\_init\_\_)
  - [3.18 Stack](#318-stack)
    - [3.18.1 \_\_call\_\_](#3181-\_\_call\_\_)
    - [3.18.2 \_\_init\_\_](#3182-\_\_init\_\_)
  - [3.19 ToCVImage](#319-tocvimage)
    - [3.19.1 \_\_call\_\_](#3191-\_\_call\_\_)
    - [3.19.2 \_\_init\_\_](#3192-\_\_init\_\_)
  - [3.20 ToNumpy](#320-tonumpy)
    - [3.20.1 \_\_call\_\_](#3201-\_\_call\_\_)
    - [3.20.2 \_\_init\_\_](#3202-\_\_init\_\_)
  - [3.21 ToPILImage](#321-topilimage)
    - [3.21.1 \_\_call\_\_](#3211-\_\_call\_\_)
    - [3.21.2 \_\_init\_\_](#3212-\_\_init\_\_)
  - [3.22 ToTensor](#322-totensor)
    - [3.22.1 \_\_call\_\_](#3221-\_\_call\_\_)
    - [3.22.2 \_\_init\_\_](#3222-\_\_init\_\_)
- [4 run](#4-run)
  - [4.1 Run](#41-run)
    - [4.1.1 \_\_init\_\_](#411-\_\_init\_\_)
    - [4.1.2 append](#412-append)
    - [4.1.3 get\_avg](#413-get\_avg)
    - [4.1.4 get\_val](#414-get\_val)
    - [4.1.5 len](#415-len)
    - [4.1.6 load\_best\_state\_dict](#416-load\_best\_state\_dict)
    - [4.1.7 load\_state\_dict](#417-load\_state\_dict)
    - [4.1.8 pickle\_dump](#418-pickle\_dump)
    - [4.1.9 pickle\_load](#419-pickle\_load)
    - [4.1.10 plot](#4110-plot)
    - [4.1.11 recalculate\_moving\_average](#4111-recalculate\_moving\_average)
    - [4.1.12 save](#4112-save)
    - [4.1.13 save\_best\_state\_dict](#4113-save\_best\_state\_dict)
    - [4.1.14 save\_state\_dict](#4114-save\_state\_dict)


# 1 metrics

[TOC](#table-of-contents)

## 1.1 F1\_Score

[TOC](#table-of-contents)

**Description**

F1 Score. Expected input shape: (batch_size, num_classes)

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| Y | torch.Tensor | Prediction |
| T | torch.Tensor | True values |

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
    [0.87, 0.01, 0.05, 0.07],
    [0.02, 0.09, 0.86, 0.03]
  ])
T = torch.tensor([
    [1., 0., 0., 0.],
    [0., 1., 0., 0.]
  ])

f1score = m.F1_Score(Y, T)

print(f1score) --> 0.5
```

## 1.2 FN

[TOC](#table-of-contents)

**Description**

False negatives. Expected input shape: (batch_size, num_classes)

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| Y | torch.Tensor | Prediction |
| T | torch.Tensor | True values |

**Returns**

False negatives : int

## 1.3 FP

[TOC](#table-of-contents)

**Description**

False positives. Expected input shape: (batch_size, num_classes)

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| Y | torch.Tensor | Prediction |
| T | torch.Tensor | True values |

**Returns**

False positives : int

## 1.4 FPR

[TOC](#table-of-contents)

**Description**

False positive rate. Expected input shape: (batch_size, num_classes)

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| Y | torch.Tensor | Prediction |
| T | torch.Tensor | True values |

**Returns**

False positive rate : float

## 1.5 TN

[TOC](#table-of-contents)

**Description**

True negatives. Expected input shape: (batch_size, num_classes)

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| Y | torch.Tensor | Prediction |
| T | torch.Tensor | True values |

**Returns**

True negatives : int

## 1.6 TP

[TOC](#table-of-contents)

**Description**

True positives. Expected input shape: (batch_size, num_classes)

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| Y | torch.Tensor | Prediction |
| T | torch.Tensor | True values |

**Returns**

True positives : int

## 1.7 TPR

[TOC](#table-of-contents)

**Description**

True positive rate. Expected input shape: (batch_size, num_classes)

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| Y | torch.Tensor | Prediction |
| T | torch.Tensor | True values |

**Returns**

True positive rate : float

## 1.8 confusion

[TOC](#table-of-contents)

**Description**

Returns the confusion matrix for the values in the `prediction` and `truth`

tensors, i.e. the amount of positions where the values of `prediction`

and `truth` are

- 1 and 1 (True Positive)

- 1 and 0 (False Positive)

- 0 and 0 (True Negative)

- 0 and 1 (False Negative)

## 1.9 confusion\_matrix

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

## 1.10 plot\_confusion\_matrix

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
## 1.11 precision

[TOC](#table-of-contents)

**Description**

Precision. Expected input shape: (batch_size, num_classes)

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| Y | torch.Tensor | Prediction |
| T | torch.Tensor | True values |

**Returns**

Precision : float

**Equations**

$precision = \frac{TP}{TP + FP}$



## 1.12 recall

[TOC](#table-of-contents)

**Description**

Recall. Expected input shape: (batch_size, num_classes)

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| Y | torch.Tensor | Prediction |
| T | torch.Tensor | True values |

**Returns**

Recall : float

**Equations**

$recall = \frac{TP}{TP + FN}$



## 1.13 top\_10\_accuracy

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

## 1.14 top\_1\_accuracy

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

## 1.15 top\_2\_accuracy

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

## 1.16 top\_3\_accuracy

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

## 1.17 top\_5\_accuracy

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

## 1.18 top\_k\_accuracy

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

# 2 model

[TOC](#table-of-contents)

## 2.2 Constants

[TOC](#table-of-contents)

| Name | Value | Description |
| -----|-------|------------ |
| TUC_ActionPrediction_model004 | TUC/ActionPrediction/Model4 | **TUC Action prediction model 4**<br>CNN with Multihead-Self-Attention<br>**Input**<br>- batch size<br>- sequence length = 30<br>- channels = 3<br>- width = 200<br>- height = 200<br>**Output**<br>- batch size<br>- number of classes = 10 |
| TUC_ActionPrediction_model005 | TUC/ActionPrediction/Model5 | **TUC Action prediction model 5**<br>CNN with Multihead-Self-Attention<br>**Input**<br>- batch size<br>- sequence length = 30<br>- channels = 3<br>- width = 300<br>- height = 300<br>**Output**<br>- batch size<br>- number of classes = 10 |
| URL | https://drive.google.com/drive/folders/1ulNnPqg-5wvenRl2CuJMxMMcaiYfHjQ9?usp=share_link | Google Drive URL |


## 2.1 load\_model

[TOC](#table-of-contents)

**Description**

# 3 multi\_transforms

[TOC](#table-of-contents)

## 3.1 BGR2GRAY

[TOC](#table-of-contents)

**Description**

Test Description

### 3.1.1 \_\_call\_\_

[TOC](#table-of-contents)

**Description**

        

        

### 3.1.2 \_\_init\_\_

[TOC](#table-of-contents)

**Description**

Initializes a new instance

## 3.2 BGR2RGB

[TOC](#table-of-contents)

**Description**

MultiTransform is an extension to keep the same transformation over a sequence of images instead of initializing a new transformation for every single image. It is inspired by `torchvision.transforms` and could be used for video augmentation. Use `rsp.ml.multi_transforms.Compose`to combine multiple image sequence transformations.

> **Note** `rsp.ml.multi_transforms.MultiTransform` is a base class and should be inherited.

### 3.2.1 \_\_call\_\_

[TOC](#table-of-contents)

**Description**

        

        

### 3.2.2 \_\_init\_\_

[TOC](#table-of-contents)

**Description**

Initializes a new instance

## 3.3 Brightness

[TOC](#table-of-contents)

**Description**

MultiTransform is an extension to keep the same transformation over a sequence of images instead of initializing a new transformation for every single image. It is inspired by `torchvision.transforms` and could be used for video augmentation. Use `rsp.ml.multi_transforms.Compose`to combine multiple image sequence transformations.

> **Note** `rsp.ml.multi_transforms.MultiTransform` is a base class and should be inherited.

### 3.3.1 \_\_call\_\_

[TOC](#table-of-contents)

**Description**

        

        

### 3.3.2 \_\_init\_\_

[TOC](#table-of-contents)

**Description**

Initializes a new instance

## 3.4 CenterCrop

[TOC](#table-of-contents)

**Description**

MultiTransform is an extension to keep the same transformation over a sequence of images instead of initializing a new transformation for every single image. It is inspired by `torchvision.transforms` and could be used for video augmentation. Use `rsp.ml.multi_transforms.Compose`to combine multiple image sequence transformations.

> **Note** `rsp.ml.multi_transforms.MultiTransform` is a base class and should be inherited.

### 3.4.1 \_\_call\_\_

[TOC](#table-of-contents)

**Description**

        

        

### 3.4.2 \_\_init\_\_

[TOC](#table-of-contents)

**Description**

Initializes a new instance

## 3.5 Color

[TOC](#table-of-contents)

**Description**

MultiTransform is an extension to keep the same transformation over a sequence of images instead of initializing a new transformation for every single image. It is inspired by `torchvision.transforms` and could be used for video augmentation. Use `rsp.ml.multi_transforms.Compose`to combine multiple image sequence transformations.

> **Note** `rsp.ml.multi_transforms.MultiTransform` is a base class and should be inherited.

### 3.5.1 \_\_call\_\_

[TOC](#table-of-contents)

**Description**

        

        

### 3.5.2 \_\_init\_\_

[TOC](#table-of-contents)

**Description**

Initializes a new instance

## 3.6 Compose

[TOC](#table-of-contents)

### 3.6.1 \_\_call\_\_

[TOC](#table-of-contents)

**Description**

Call self as a function.

### 3.6.2 \_\_init\_\_

[TOC](#table-of-contents)

**Description**

Initialize self.  See help(type(self)) for accurate signature.

## 3.7 GaussianNoise

[TOC](#table-of-contents)

**Description**

MultiTransform is an extension to keep the same transformation over a sequence of images instead of initializing a new transformation for every single image. It is inspired by `torchvision.transforms` and could be used for video augmentation. Use `rsp.ml.multi_transforms.Compose`to combine multiple image sequence transformations.

> **Note** `rsp.ml.multi_transforms.MultiTransform` is a base class and should be inherited.

### 3.7.1 \_\_call\_\_

[TOC](#table-of-contents)

**Description**

        

        

### 3.7.2 \_\_init\_\_

[TOC](#table-of-contents)

**Description**

Initializes a new instance

## 3.8 MultiTransform

[TOC](#table-of-contents)

**Description**

MultiTransform is an extension to keep the same transformation over a sequence of images instead of initializing a new transformation for every single image. It is inspired by `torchvision.transforms` and could be used for video augmentation. Use `rsp.ml.multi_transforms.Compose`to combine multiple image sequence transformations.

> **Note** `rsp.ml.multi_transforms.MultiTransform` is a base class and should be inherited.

### 3.8.1 \_\_call\_\_

[TOC](#table-of-contents)

**Description**

        

        

### 3.8.2 \_\_init\_\_

[TOC](#table-of-contents)

**Description**

Initializes a new instance

## 3.9 Normalize

[TOC](#table-of-contents)

**Description**

MultiTransform is an extension to keep the same transformation over a sequence of images instead of initializing a new transformation for every single image. It is inspired by `torchvision.transforms` and could be used for video augmentation. Use `rsp.ml.multi_transforms.Compose`to combine multiple image sequence transformations.

> **Note** `rsp.ml.multi_transforms.MultiTransform` is a base class and should be inherited.

### 3.9.1 \_\_call\_\_

[TOC](#table-of-contents)

**Description**

        

        

### 3.9.2 \_\_init\_\_

[TOC](#table-of-contents)

**Description**

Initializes a new instance

## 3.10 RGB2BGR

[TOC](#table-of-contents)

**Description**

MultiTransform is an extension to keep the same transformation over a sequence of images instead of initializing a new transformation for every single image. It is inspired by `torchvision.transforms` and could be used for video augmentation. Use `rsp.ml.multi_transforms.Compose`to combine multiple image sequence transformations.

> **Note** `rsp.ml.multi_transforms.MultiTransform` is a base class and should be inherited.

### 3.10.1 \_\_call\_\_

[TOC](#table-of-contents)

**Description**

        

        

### 3.10.2 \_\_init\_\_

[TOC](#table-of-contents)

**Description**

Initializes a new instance

## 3.11 RandomCrop

[TOC](#table-of-contents)

**Description**

MultiTransform is an extension to keep the same transformation over a sequence of images instead of initializing a new transformation for every single image. It is inspired by `torchvision.transforms` and could be used for video augmentation. Use `rsp.ml.multi_transforms.Compose`to combine multiple image sequence transformations.

> **Note** `rsp.ml.multi_transforms.MultiTransform` is a base class and should be inherited.

### 3.11.1 \_\_call\_\_

[TOC](#table-of-contents)

**Description**

        

        

### 3.11.2 \_\_init\_\_

[TOC](#table-of-contents)

**Description**

Test

## 3.12 RandomHorizontalFlip

[TOC](#table-of-contents)

**Description**

MultiTransform is an extension to keep the same transformation over a sequence of images instead of initializing a new transformation for every single image. It is inspired by `torchvision.transforms` and could be used for video augmentation. Use `rsp.ml.multi_transforms.Compose`to combine multiple image sequence transformations.

> **Note** `rsp.ml.multi_transforms.MultiTransform` is a base class and should be inherited.

### 3.12.1 \_\_call\_\_

[TOC](#table-of-contents)

**Description**

        

        

### 3.12.2 \_\_init\_\_

[TOC](#table-of-contents)

**Description**

Initializes a new instance

## 3.13 RandomVerticalFlip

[TOC](#table-of-contents)

**Description**

MultiTransform is an extension to keep the same transformation over a sequence of images instead of initializing a new transformation for every single image. It is inspired by `torchvision.transforms` and could be used for video augmentation. Use `rsp.ml.multi_transforms.Compose`to combine multiple image sequence transformations.

> **Note** `rsp.ml.multi_transforms.MultiTransform` is a base class and should be inherited.

### 3.13.1 \_\_call\_\_

[TOC](#table-of-contents)

**Description**

        

        

### 3.13.2 \_\_init\_\_

[TOC](#table-of-contents)

**Description**

Initializes a new instance

## 3.14 Resize

[TOC](#table-of-contents)

**Description**

MultiTransform is an extension to keep the same transformation over a sequence of images instead of initializing a new transformation for every single image. It is inspired by `torchvision.transforms` and could be used for video augmentation. Use `rsp.ml.multi_transforms.Compose`to combine multiple image sequence transformations.

> **Note** `rsp.ml.multi_transforms.MultiTransform` is a base class and should be inherited.

### 3.14.1 \_\_call\_\_

[TOC](#table-of-contents)

**Description**

        

        

### 3.14.2 \_\_init\_\_

[TOC](#table-of-contents)

**Description**

Initializes a new instance

## 3.15 Rotate

[TOC](#table-of-contents)

**Description**

MultiTransform is an extension to keep the same transformation over a sequence of images instead of initializing a new transformation for every single image. It is inspired by `torchvision.transforms` and could be used for video augmentation. Use `rsp.ml.multi_transforms.Compose`to combine multiple image sequence transformations.

> **Note** `rsp.ml.multi_transforms.MultiTransform` is a base class and should be inherited.

### 3.15.1 \_\_call\_\_

[TOC](#table-of-contents)

**Description**

        

        

### 3.15.2 \_\_init\_\_

[TOC](#table-of-contents)

**Description**

Initializes a new instance

## 3.16 Satturation

[TOC](#table-of-contents)

**Description**

MultiTransform is an extension to keep the same transformation over a sequence of images instead of initializing a new transformation for every single image. It is inspired by `torchvision.transforms` and could be used for video augmentation. Use `rsp.ml.multi_transforms.Compose`to combine multiple image sequence transformations.

> **Note** `rsp.ml.multi_transforms.MultiTransform` is a base class and should be inherited.

### 3.16.1 \_\_call\_\_

[TOC](#table-of-contents)

**Description**

        

        

### 3.16.2 \_\_init\_\_

[TOC](#table-of-contents)

**Description**

Initializes a new instance

## 3.17 Scale

[TOC](#table-of-contents)

**Description**

MultiTransform is an extension to keep the same transformation over a sequence of images instead of initializing a new transformation for every single image. It is inspired by `torchvision.transforms` and could be used for video augmentation. Use `rsp.ml.multi_transforms.Compose`to combine multiple image sequence transformations.

> **Note** `rsp.ml.multi_transforms.MultiTransform` is a base class and should be inherited.

### 3.17.1 \_\_call\_\_

[TOC](#table-of-contents)

**Description**

        

        

### 3.17.2 \_\_init\_\_

[TOC](#table-of-contents)

**Description**

Initializes a new instance

## 3.18 Stack

[TOC](#table-of-contents)

**Description**

MultiTransform is an extension to keep the same transformation over a sequence of images instead of initializing a new transformation for every single image. It is inspired by `torchvision.transforms` and could be used for video augmentation. Use `rsp.ml.multi_transforms.Compose`to combine multiple image sequence transformations.

> **Note** `rsp.ml.multi_transforms.MultiTransform` is a base class and should be inherited.

### 3.18.1 \_\_call\_\_

[TOC](#table-of-contents)

**Description**

        

        

### 3.18.2 \_\_init\_\_

[TOC](#table-of-contents)

**Description**

Initializes a new instance

## 3.19 ToCVImage

[TOC](#table-of-contents)

**Description**

MultiTransform is an extension to keep the same transformation over a sequence of images instead of initializing a new transformation for every single image. It is inspired by `torchvision.transforms` and could be used for video augmentation. Use `rsp.ml.multi_transforms.Compose`to combine multiple image sequence transformations.

> **Note** `rsp.ml.multi_transforms.MultiTransform` is a base class and should be inherited.

### 3.19.1 \_\_call\_\_

[TOC](#table-of-contents)

**Description**

        

        

### 3.19.2 \_\_init\_\_

[TOC](#table-of-contents)

**Description**

Initializes a new instance

## 3.20 ToNumpy

[TOC](#table-of-contents)

**Description**

MultiTransform is an extension to keep the same transformation over a sequence of images instead of initializing a new transformation for every single image. It is inspired by `torchvision.transforms` and could be used for video augmentation. Use `rsp.ml.multi_transforms.Compose`to combine multiple image sequence transformations.

> **Note** `rsp.ml.multi_transforms.MultiTransform` is a base class and should be inherited.

### 3.20.1 \_\_call\_\_

[TOC](#table-of-contents)

**Description**

        

        

### 3.20.2 \_\_init\_\_

[TOC](#table-of-contents)

**Description**

Initializes a new instance

## 3.21 ToPILImage

[TOC](#table-of-contents)

**Description**

MultiTransform is an extension to keep the same transformation over a sequence of images instead of initializing a new transformation for every single image. It is inspired by `torchvision.transforms` and could be used for video augmentation. Use `rsp.ml.multi_transforms.Compose`to combine multiple image sequence transformations.

> **Note** `rsp.ml.multi_transforms.MultiTransform` is a base class and should be inherited.

### 3.21.1 \_\_call\_\_

[TOC](#table-of-contents)

**Description**

        

        

### 3.21.2 \_\_init\_\_

[TOC](#table-of-contents)

**Description**

Initializes a new instance

## 3.22 ToTensor

[TOC](#table-of-contents)

**Description**

MultiTransform is an extension to keep the same transformation over a sequence of images instead of initializing a new transformation for every single image. It is inspired by `torchvision.transforms` and could be used for video augmentation. Use `rsp.ml.multi_transforms.Compose`to combine multiple image sequence transformations.

> **Note** `rsp.ml.multi_transforms.MultiTransform` is a base class and should be inherited.

### 3.22.1 \_\_call\_\_

[TOC](#table-of-contents)

**Description**

        

        

### 3.22.2 \_\_init\_\_

[TOC](#table-of-contents)

**Description**

Initializes a new instance

# 4 run

[TOC](#table-of-contents)

## 4.1 Run

[TOC](#table-of-contents)

### 4.1.1 \_\_init\_\_

[TOC](#table-of-contents)

**Description**

Initialize self.  See help(type(self)) for accurate signature.

### 4.1.2 append

[TOC](#table-of-contents)

**Description**

### 4.1.3 get\_avg

[TOC](#table-of-contents)

**Description**

### 4.1.4 get\_val

[TOC](#table-of-contents)

**Description**

### 4.1.5 len

[TOC](#table-of-contents)

**Description**

### 4.1.6 load\_best\_state\_dict

[TOC](#table-of-contents)

**Description**

### 4.1.7 load\_state\_dict

[TOC](#table-of-contents)

**Description**

### 4.1.8 pickle\_dump

[TOC](#table-of-contents)

**Description**

### 4.1.9 pickle\_load

[TOC](#table-of-contents)

**Description**

### 4.1.10 plot

[TOC](#table-of-contents)

**Description**

### 4.1.11 recalculate\_moving\_average

[TOC](#table-of-contents)

**Description**

### 4.1.12 save

[TOC](#table-of-contents)

**Description**

### 4.1.13 save\_best\_state\_dict

[TOC](#table-of-contents)

**Description**

### 4.1.14 save\_state\_dict

[TOC](#table-of-contents)

**Description**

