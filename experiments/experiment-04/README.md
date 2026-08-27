# Experiment 04: Comparative Study of Deep CNN Architectures Using Transfer Learning

Comparative study of different **CNN architectures** and implementation of **Transfer Learning** for image classification using the **CIFAR-10 Dataset** with TensorFlow/Keras.

---

## Objective

To study different CNN architectures and understand transfer learning, fine-tuning, and their effect on image classification performance.

---

## Dataset

**Dataset:** CIFAR-10  
**Source:** TensorFlow/Keras Dataset  
**Images:** 60,000  
**Training Images:** 50,000  
**Testing Images:** 10,000  
**Image Size:** 32 × 32 × 3  
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
Experiment-04-Transfer-Learning
│
├── notebook
│   └── 001_LAB4.ipynb
│
├── figures
│   ├── sample_images.jpg
│   ├── training_accuracy.jpg
│   ├── validation_accuracy.jpg
│   ├── training_loss.jpg
│   ├── validation_loss.jpg
│   └── confusion_matrix.jpg
│
├── report
│   └── Experiment_04_Report.pdf
│
└── README.md
```

---

## Contents

This experiment includes:

* Evolution of CNN Architectures
* LeNet-5
* AlexNet
* VGG16
* GoogleNet
* ResNet50
* Dilated Convolution
* Transpose Convolution
* Transfer Learning
* Fine-Tuning
* Hyperparameter Study
* CNN Architecture Comparison
* Model Evaluation
* Performance Analysis

---

## Transfer Learning

Transfer learning was performed using pretrained CNN models. The pretrained layers were initially frozen and a new classifier was trained for CIFAR-10. Fine-tuning was then performed to allow the model to adapt better to the new dataset.

```text
Pretrained Model
       ↓
Freeze Layers
       ↓
Train Classifier
       ↓
Fine-Tuning
       ↓
Evaluate Model
```

---

## Model Comparison

| Model | Parameters | Best Validation Accuracy | Training Time |
| :--- | ---: | ---: | ---: |
| LeNet-5 | 83,126 | 51.86% | 0.54 min |
| AlexNet | 36,925,322 | 10.00% | 2.72 min |
| VGG16 | 14,781,642 | 65.34% | 1.12 min |
| ResNet50 | 23,851,274 | 66.20% | 1.54 min |

*Note: GoogleNet was studied theoretically but was not experimentally evaluated.*

---

## Fine-Tuning Results

| Metric | Result |
| :--- | ---: |
| Best Training Accuracy | 83.75% |
| Validation Accuracy Before Fine-Tuning | 64.96% |
| Validation Accuracy After Fine-Tuning | 69.82% |
| Testing Accuracy | 69.76% |
| Precision | 69.75% |
| Recall | 69.76% |
| F1-Score | 69.70% |
| Total Parameters | 14,781,642 |

---

## Key Observations

* ResNet50 achieved the highest validation accuracy among the tested architectures.
* Fine-tuning improved validation accuracy from **64.96% to 69.82%**.
* Adam performed better than SGD in the tested configurations.
* Transfer learning provided useful pretrained features for CIFAR-10 classification.
* The final model achieved a **69.76% testing accuracy**.

---

## How to Run

1. Install the required dependencies:
   ```bash
   pip install -r ../../requirements.txt
   ```
2. Open the notebook in the **notebook/** folder.
3. Run all cells sequentially.

---

## Author

**A. Priyankaa**  
B.Tech Artificial Intelligence & Data Science  
Shiv Nadar University Chennai