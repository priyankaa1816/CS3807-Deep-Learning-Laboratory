# CS3807 – Deep Learning Laboratory

## Experiment 3: Implementation of CNNs for Image Classification

Implementation of a Convolutional Neural Network (CNN) for image classification using the CIFAR-10 dataset with TensorFlow/Keras.

---

## Objective

To understand and implement the working of Convolutional Neural Networks by studying convolution, feature maps, stride, padding, pooling, parameter calculation, CNN construction, training, and evaluation.

---

## Dataset – CIFAR-10

CIFAR-10 contains 60,000 RGB images belonging to 10 classes.

- Training Images: 50,000
- Testing Images: 10,000
- Number of Classes: 10
- Image Size: 32 × 32
- Channels: 3 (RGB)
- Images per Test Class: 1,000

### Classes

1. Airplane
2. Automobile
3. Bird
4. Cat
5. Deer
6. Dog
7. Frog
8. Horse
9. Ship
10. Truck

---

## Task 1 – Dataset Exploration

- Loaded the CIFAR-10 dataset.
- Displayed ten sample images.
- Printed the dataset dimensions.
- Plotted the class distribution.

Training data shape:

`(50000, 32, 32, 3)`

Testing data shape:

`(10000, 32, 32, 3)`

The class distribution is balanced, with 5,000 training images and 1,000 test images per class.

---

## Task 2 – Effect of Kernel Size

Compared convolution using:

- 3 × 3 kernel
- 5 × 5 kernel
- 7 × 7 kernel

Using stride 1 and valid padding:

| Kernel Size | Feature Map Size |
|-------------|------------------|
| 3 × 3 | 30 × 30 |
| 5 × 5 | 28 × 28 |
| 7 × 7 | 26 × 26 |

Eight filters were used to visualize the feature maps.

---

## Task 3 – Effect of Stride and Padding

Studied the effect of different stride and padding values on the output feature map.

- **Stride** determines how far the filter moves during convolution.
- **SAME padding** adds padding to preserve the spatial dimensions when stride is 1.
- **VALID padding** does not add padding, so the output dimensions become smaller.

### Output Dimension Formula

```text
Output = floor((N - F + 2P) / S) + 1

where:
- N = Input size
- F = Filter size
- P = Padding
- S = Stride

Task 4 – Feature Map Visualization

Visualized eight feature maps after the first convolution layer.

A feature map represents the activation produced by a particular filter. It shows where and how strongly the pattern learned by that filter is present in the image.

Different filters learn different visual patterns, so each filter produces a different feature map.

Task 5 – Max Pooling vs Average Pooling

Compared Max Pooling and Average Pooling using the same CNN structure.

Max Pooling

Selects the maximum value from each pooling window and preserves the strongest activation.

Average Pooling

Calculates the average value of each pooling window.

Both produced the same output size:

16 × 16 × 16

Results
Pooling Method	Test Accuracy
Max Pooling	58.51%
Average Pooling	57.80%

Max Pooling performed slightly better in this experiment.

Task 6 – CNN Construction and Training

The CNN architecture used was:

Input (32 × 32 × 3)
        ↓
Conv2D (32 filters, 3 × 3)
        ↓
ReLU
        ↓
Max Pooling (2 × 2)
        ↓
Conv2D (64 filters, 3 × 3)
        ↓
ReLU
        ↓
Max Pooling (2 × 2)
        ↓
Flatten
        ↓
Dense (128 neurons)
        ↓
Dense (10 neurons)
        ↓
Softmax
Layer Output Sizes
Input       : 32 × 32 × 3
Conv2D      : 32 × 32 × 32
Max Pooling : 16 × 16 × 32
Conv2D      : 16 × 16 × 64
Max Pooling : 8 × 8 × 64
Flatten     : 4096
Dense       : 128
Output      : 10
Training Configuration
Optimizer: Adam
Epochs: 20
Batch Size: 32
Parameter Calculation

First convolution layer:

(3 × 3 × 3 + 1) × 32 = 896

Second convolution layer:

(3 × 3 × 32 + 1) × 64 = 18,496

Dense layer:

4096 × 128 + 128 = 524,416

Output layer:

128 × 10 + 10 = 1,290

Total parameters:

896 + 18,496 + 524,416 + 1,290
= 545,098
Training Results

The model achieved approximately 96.94% training accuracy by the final epoch.

The best validation accuracy was approximately 70.86% around epoch 8.

The training accuracy continued increasing while validation accuracy stopped improving and validation loss increased. This indicates that the model was overfitting the training data.

Task 7 – Model Evaluation

The trained CNN was evaluated using the CIFAR-10 test dataset.

Overall Results
Metric	Result
Accuracy	68.28%
Precision	0.6876
Recall	0.6828
F1-Score	0.6834
Classification Report
Class	Precision	Recall	F1-Score
Airplane	0.69	0.77	0.73
Automobile	0.81	0.83	0.82
Bird	0.55	0.56	0.56
Cat	0.47	0.54	0.50
Deer	0.69	0.55	0.61
Dog	0.58	0.58	0.58
Frog	0.79	0.71	0.74
Horse	0.77	0.68	0.72
Ship	0.79	0.80	0.80
Truck	0.75	0.81	0.77

The model performed best on the Automobile class with an F1-score of 0.82 and had the most difficulty with the Cat class, which had an F1-score of 0.50.

Conclusion

A CNN was successfully implemented for CIFAR-10 image classification. The experiment demonstrated convolution, feature extraction, pooling, CNN architecture, parameter calculation, training, and evaluation. The final model achieved 68.28% test accuracy and showed clear signs of overfitting.