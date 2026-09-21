```markdown
# Experiment 05: Comprehensive Study of CNN Training and Optimization

Comprehensive study of **CNN training**, **regularization**, **optimization**, **hyperparameter tuning**, **transfer learning**, **fine-tuning**, and **5-Fold Cross-Validation** using the **Oxford-IIIT Pet Dataset** with TensorFlow/Keras.

---

## Objective

To study different CNN training strategies and select a suitable model configuration based on accuracy, consistency, generalization, and computational cost.

---

## Dataset

- **Dataset:** Oxford-IIIT Pet Dataset  
- **Images:** Pet images from 37 cat and dog breeds  
- **Image Size:** 224 × 224 × 3  
- **Number of Classes:** 37  

---

## Folder Structure

```text
Experiment-05-Comprehensive-CNN-Study
│
├── notebook
│   └── 001_LAB5.ipynb
│
├── Experiment_5_Results
│   ├── 01_initialization
│   ├── 02_regularization
│   ├── 03_batch_normalization
│   ├── 04_optimizers
│   ├── 05_hyperparameter_tuning
│   ├── 06_transfer_learning
│   ├── 07_cross_validation
│   └── 08_final_model
│
├── report
│   └── Experiment_05_Report.pdf
│
└── README.md

```

---

## Contents

This experiment includes:

* MobileNetV2 Architecture & Weight Initialization
* Regularization & Batch Normalization
* Optimizer Comparison (SGD, Momentum, RMSProp, Adam)
* Hyperparameter Tuning & Transfer Learning
* 5-Fold Cross-Validation & Final Model Evaluation

---

## Weight Initialization

The following initialization methods were compared: **Zero**, **Random**, **Xavier/Glorot**, and **He Initialization**. Training loss and validation accuracy were analyzed across epochs to evaluate convergence speed and stability.

---

## Optimization Algorithms

| Optimizer | Final Loss | Best Validation Accuracy | Best Epoch | Time (s) |
| --- | --- | --- | --- | --- |
| **SGD** | 0.3530 | 88.99% | 8 | 47.93 |
| **Momentum** | 0.0566 | 90.63% | 7 | 48.55 |
| **RMSProp** | 0.0341 | 90.63% | 4 | 48.69 |
| **Adam** | 0.0495 | 90.63% | 7 | 48.20 |

---

## Hyperparameter Tuning

| Hyperparameter | Values Tested |
| --- | --- |
| **Learning Rate** | 0.001, 0.0001 |
| **Batch Size** | 16, 32, 64 |
| **Dropout** | 0, 0.25, 0.5 |
| **Optimizer** | SGD, Adam |
| **Fine-Tuning LR** | $10^{-4}, 10^{-5}$ |

---

## Transfer Learning

MobileNetV2 pretrained on ImageNet was evaluated using the following pipeline:

```text
Pretrained MobileNetV2 ➔ Freeze Backbone ➔ Train Classifier ➔ Fine-Tuning ➔ Evaluate Model

```

---

## 5-Fold Cross-Validation

| Configuration | Description | Mean Accuracy | SD |
| --- | --- | --- | --- |
| **C1** | Baseline | **91.41%** | **0.61%** |
| **C2** | Best Hyperparameters | 90.96% | 1.02% |
| **C3** | Feature Extraction | 91.34% | 0.55% |
| **C4** | Fine-Tuned | 88.69% | 1.14% |

*The **C1 Baseline** achieved the highest mean cross-validation accuracy.*

---

## Final Model Results

Selected Configuration: **C1 Baseline**

| Metric | Result |
| --- | --- |
| **Mean CV Accuracy** | 91.41% |
| **CV Standard Deviation** | 0.61% |
| **Test Accuracy** | 90.32% |
| **Precision** | 90.55% |
| **Recall** | 90.28% |
| **F1-Score** | 90.26% |
| **Training Time** | 57.37 s |
| **Total Parameters** | 2,305,381 |
| **Trainable Parameters** | 47,397 |

---

## Additional Exercise

| Configuration | Mean Accuracy | SD | Training Time (s) |
| --- | --- | --- | --- |
| **New-A** | 88.69% | 0.84% | 62.63 |
| **New-B** | 91.00% | 0.50% | 43.15 |
| **C1 Baseline** | **91.41%** | **0.61%** | **43.96** |

---

## Key Observations

* **RMSProp** achieved the lowest overall training loss among all optimizers.
* **Learning rate** had the most significant impact on validation performance, whereas batch size and dropout showed minor variance.
* **C1 Baseline** proved to be the most robust and consistent configuration across cross-validation folds.

---

## How to Run

1. Install dependencies:
```bash
pip install -r ../../requirements.txt

```


2. Open and run `notebook/001_LAB5.ipynb` sequentially.
3. Figures and output plots are automatically saved in `Experiment_5_Results/`.

---

## Author

**A. Priyankaa**

B.Tech Artificial Intelligence & Data Science

Shiv Nadar University Chennai

```

<FollowUp label="Want to adjust any formatting or table styles to fit your repo theme?" query="I'd like to adjust the table formatting and markdown styling for the README."/>

```