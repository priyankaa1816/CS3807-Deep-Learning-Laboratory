# Experiment 06: Sequence Learning and Video Understanding

Implementation and comparison of **RNN, LSTM and GRU models for sequence learning**, along with **CNN-LSTM and CNN-GRU models for video classification** and a **Seq2Seq model for sequence reversal**.

---

## Objective

- Study how recurrent neural networks learn temporal patterns and compare **RNN, LSTM and GRU** models for sequence classification.
- Extend sequence learning to video classification using a **pretrained MobileNetV2 feature extractor** with LSTM and GRU models.
- Implement a **Seq2Seq encoder-decoder model** for sequence reversal and study token-level and sequence-level accuracy.

---

## Datasets

### Part 1: UCI Human Activity Recognition

- **Dataset:** UCI Human Activity Recognition Using Smartphones Dataset
- **Classes:**
  - WALKING
  - WALKING_UPSTAIRS
  - WALKING_DOWNSTAIRS
  - SITTING
  - STANDING
  - LAYING
- **Input Shape:** `(128, 9)`
- **Number of Classes:** 6
- **Train / Validation / Test Split:** 70% / 15% / 15%

---

### Part 2: UCF101

A small subset of the **UCF101 video dataset** was used for video classification.

- **Classes:**
  - Basketball
  - Biking
  - TennisSwing
  - WalkingWithDog
- **Total Videos:** 120
- **Train / Validation / Test:** 84 / 18 / 18
- **Frames per Video:** 10

A pretrained **MobileNetV2** was used as a frozen CNN feature extractor. Each frame was converted into a **1280-dimensional feature vector**, giving a sequence of shape `(10, 1280)` for each video.

---

### Part 3: Synthetic Sequence-to-Sequence Task

A synthetic dataset was created to study sequence reversal. The model was trained to reverse input sequences and was also tested with a different output sequence length.

---

## Folder Structure

```text
Experiment-06-Sequence-Learning
│
├── notebook
│   └── Experiment_06_Sequence_Learning.ipynb
│
├── figures
│   ├── Part1_Figures
│   ├── Part2_Figures
│   └── Part3_Figures
│
├── report
│   └── Experiment_06_Report.pdf
│
└── README.md
```

---

## Contents

This experiment includes:

- UCI HAR Dataset Preparation
- Temporal Sensor Signal Visualization
- Data Normalization
- Manual RNN Forward Pass
- RNN Implementation
- LSTM Implementation
- GRU Implementation
- Model Comparison
- Confusion Matrix Analysis
- Sequence Length Comparison
- UCF101 Video Classification
- MobileNetV2 Feature Extraction
- CNN-LSTM and CNN-GRU Models
- Seq2Seq Encoder-Decoder
- Sequence Reversal
- Different Input and Output Sequence Lengths
- Performance Analysis

---

## Models

### Sequence Classification
- Vanilla RNN
- LSTM
- GRU

### Video Classification
- MobileNetV2 + LSTM
- MobileNetV2 + GRU

### Sequence-to-Sequence
- Encoder-Decoder Seq2Seq model

---

## Performance Metrics

The models are evaluated using:

- Accuracy
- Precision
- Recall
- Macro F1-Score
- Confusion Matrix
- Training Time
- Number of Parameters

For the Seq2Seq models:
- Token Accuracy
- Sequence Accuracy
- Training Loss
- Validation Loss

---

## Results

### UCI HAR Classification

| Model | Accuracy | Macro F1-Score | Parameters |
| :--- | :---: | :---: | :---: |
| **RNN** | 77.78% | 77.86% | 1,974 |
| **LSTM** | 90.83% | 90.80% | 6,006 |
| **GRU** | 91.67% | 91.61% | 4,758 |

### UCF101 Video Classification

Both CNN-LSTM and CNN-GRU achieved:
- **Accuracy:** 100%
- **Macro F1-Score:** 100%

*CNN-GRU used fewer parameters and had a shorter training time than CNN-LSTM.*

### Seq2Seq

**For the 5-to-5 sequence reversal task:**
- **Token Accuracy:** 99.82%
- **Sequence Accuracy:** 99.42%

**For the different-length sequence task:**
- **Token Accuracy:** 99.94%
- **Sequence Accuracy:** 99.75%

---

## How to Run

1. Install the required dependencies:
   ```bash
   pip install -r ../../requirements.txt
   ```
2. Open the notebook located in the `notebook/` folder.
3. Run all cells sequentially.

---

## Author

**A. Priyankaa**  
B.Tech Artificial Intelligence & Data Science  
Shiv Nadar University Chennai
