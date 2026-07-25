# Additional Tasks – Experiments 1 & 2

This folder contains the additional programming tasks completed for **Experiment 1** and **Experiment 2** of the **CS3807 – Deep Learning Laboratory** course.

These tasks were implemented to gain a better understanding of the **Perceptron Learning Algorithm**, its learning process on linearly separable problems, and its limitations on non-linearly separable data.

---

## Folder Structure

```text
additional-tasks-exp-01-02/
│
├── figures/
│   ├── basic_gates/
│   │   ├── and_gate.eps
│   │   ├── or_gate.eps
│   │   └── not_gate.eps
│   │
│   └── xor_gates/
│       └── xor_gate.eps
│
├── notebook/
│   └── Additional_Tasks_Gates.ipynb
│
└── README.md
```

---

## Tasks Included

### Experiment 1 – Basic Logic Gates

Implemented the Perceptron Learning Algorithm from scratch for:

- AND Gate
- OR Gate
- NOT Gate

Each implementation includes:

- Weight updates after each misclassification
- Decision boundary visualization after every weight update
- Final predictions
- Learning inference

---

### Experiment 2 – XOR Gate

Implemented the Perceptron Learning Algorithm for the XOR gate to study its learning behavior.

The implementation includes:

- Weight updates during training
- Decision boundary progression
- Final predictions
- Analysis of why the algorithm does not converge

This experiment demonstrates that the XOR gate is **not linearly separable**, making it impossible for a Single Layer Perceptron to learn a correct decision boundary. This limitation highlights the need for **Multi-Layer Perceptrons (MLPs)** with hidden layers.

---

## Running the Notebook

Open `notebook/Additional_Tasks_Gates.ipynb` and run all cells sequentially to generate:

- Weight update history
- Decision boundary visualizations
- Final predictions
- Learning analysis
