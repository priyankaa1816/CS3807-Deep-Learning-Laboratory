# Experiment 03: Implementation of CNNs for Image Classification

Implementation of a **Convolutional Neural Network (CNN)** for image classification using the **CIFAR-10 Dataset** with TensorFlow/Keras.

---

## Objective

To understand and implement the working of Convolutional Neural Networks by studying convolution, feature maps, kernel size, stride, padding, pooling, parameter calculation, CNN construction, training, and evaluation.

---

## Dataset

**Dataset:** CIFAR-10

**Source:** TensorFlow/Keras Dataset

**Images:** 60,000

**Training Images:** 50,000

**Testing Images:** 10,000

**Image Size:** 32 × 32

**Channels:** 3 (RGB)

**Number of Classes:** 10

### Classes

- 0 → Airplane
- 1 → Automobile
- 2 → Bird
- 3 → Cat
- 4 → Deer
- 5 → Dog
- 6 → Frog
- 7 → Horse
- 8 → Ship
- 9 → Truck

---

## Folder Structure

```text
Experiment-03-CNN
│
├── notebook
│   └── 001_LAB3.ipynb
│
├── figures
│   ├── Figure_1_...
│   ├── Figure_2_...
│   ├── ...
│
├── report
│   └── Experiment_03_Report.pdf
│
└── README.md
```

---

## Contents

This experiment includes:

- Dataset Exploration
- Sample Image Visualization
- Class Distribution Analysis
- Effect of Kernel Size
- Effect of Stride and Padding
- Output Dimension Calculation
- Feature Map Visualization
- Max Pooling vs Average Pooling
- CNN Architecture Construction
- Parameter Calculation
- Model Training
- Model Evaluation
- Classification Report
- Performance Analysis
- Overfitting Analysis

---

## CNN Architecture

The CNN used in this experiment consists of:

```text
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
```

### Training Configuration

- **Optimizer:** Adam
- **Epochs:** 20
- **Batch Size:** 32

### Total Parameters

**545,098 trainable parameters**

---

## Experimental Analysis

The experiment studies:

### Kernel Size

Compared:

- 3 × 3 kernel
- 5 × 5 kernel
- 7 × 7 kernel

Using stride 1 and VALID padding, the resulting feature map sizes were:

| Kernel Size | Feature Map Size |
|---|---|
| 3 × 3 | 30 × 30 |
| 5 × 5 | 28 × 28 |
| 7 × 7 | 26 × 26 |

### Stride and Padding

The effect of stride and padding on feature map dimensions was studied using:

```text
Output = floor((N - F + 2P) / S) + 1
```

### Pooling Comparison

Max Pooling and Average Pooling were compared using the same CNN structure.

| Pooling Method | Test Accuracy |
|---|---:|
| Max Pooling | 58.51% |
| Average Pooling | 57.80% |

Max Pooling performed slightly better in this experiment.

---

## Performance Metrics

The trained CNN was evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- Classification Report

### Overall Results

| Metric | Result |
|---|---:|
| Accuracy | 68.28% |
| Precision | 0.6876 |
| Recall | 0.6828 |
| F1-Score | 0.6834 |

### Best Performing Class

**Automobile**

- Precision: 0.81
- Recall: 0.83
- F1-Score: 0.82

### Most Difficult Class

**Cat**

- Precision: 0.47
- Recall: 0.54
- F1-Score: 0.50

---

## Training Results

- **Training Accuracy:** 96.94%
- **Best Validation Accuracy:** 70.86%
- **Test Accuracy:** 68.28%

The training accuracy continued increasing while validation accuracy stopped improving and validation loss increased. This indicates that the model was **overfitting** the training data.

---

## Key Observations

- Smaller convolution kernels preserve more spatial information.
- Increasing the stride reduces the spatial dimensions of the feature map.
- SAME padding helps preserve spatial dimensions.
- VALID padding reduces the spatial dimensions.
- Different filters learn different visual patterns and produce different feature maps.
- Max Pooling performed slightly better than Average Pooling.
- The model achieved high training accuracy but lower validation and test accuracy.
- The difference between training and validation performance indicates overfitting.
- The model performed best on the Automobile class.
- The Cat class was the most difficult class for the model.

---

## How to Run

1. Install the required dependencies.

```bash
pip install -r ../../requirements.txt
```

2. Open the notebook located in the **notebook/** folder.

3. Run all cells sequentially.

---

## Author

**A. Priyankaa**

B.Tech Artificial Intelligence & Data Science

Shiv Nadar University Chennai
