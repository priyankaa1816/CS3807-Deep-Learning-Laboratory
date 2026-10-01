# Experiment 07: Autoencoders, Denoising and Variational Autoencoders

Implementation and comparison of Fully Connected Autoencoders, Convolutional Autoencoders, Denoising Autoencoders and Variational Autoencoders for image reconstruction, denoising, latent-space visualization and image generation using the MNIST dataset.

---

## Objective

- Implement a Fully Connected Autoencoder for image reconstruction.
- Implement a Convolutional Autoencoder and compare reconstruction quality.
- Build a Denoising Autoencoder using controlled image noise.
- Evaluate reconstruction using MSE, MAE and SSIM.
- Implement a Variational Autoencoder with a probabilistic latent space.
- Visualize the latent space, generate new images and perform latent-space interpolation.
- Study the effect of latent dimension and KL-loss weighting.

---

## Dataset

### MNIST Handwritten Digit Dataset

- **Image Size:** `28 × 28 × 1`
- **Classes:** 10 handwritten digits
- **Training Images:** 10,000
- **Test Images:** 2,000
- **Pixel Range:** Normalized from `[0,255]` to `[0,1]`

The original image is used as the reconstruction target.

---

## Folder Structure

```text
Experiment-07-Autoencoders-VAE
│
├── notebook
│   └── Experiment_07_Autoencoders_VAE.ipynb
│
├── figures
│   └── Experiment_7_Results
│
├── report
│   └── Experiment_07_Report.pdf
│
└── README.md
```

---

## Contents

This experiment includes:

- MNIST Data Preparation
- Fully Connected Autoencoder
- Convolutional Autoencoder
- Reconstruction Metrics
- Denoising Autoencoder
- Gaussian and Salt-and-Pepper Noise
- Variational Autoencoder
- VAE Latent-Space Visualization
- VAE Image Generation
- Latent-Space Interpolation
- Reconstruction Error Analysis
- Latent-Dimension Study
- Beta-VAE Analysis
- Additional Experiments

---

## Models

### Autoencoders

- Fully Connected Autoencoder
- Convolutional Autoencoder
- Denoising Convolutional Autoencoder

### Variational Autoencoder

The VAE uses a probabilistic latent representation:

```text
Input → Encoder → (μ, log(σ²)) → z → Decoder → Reconstruction
```

The main VAE uses a 2-dimensional latent space for visualization.

---

## Performance Metrics

The models are evaluated using:

- MSE
- MAE
- SSIM
- Number of Parameters
- Training Time

For the VAE:

- Reconstruction Loss
- KL Divergence
- Total Loss

---

## Results

### Main Models

| Model | MSE | MAE | SSIM | Parameters |
| :--- | :---: | :---: | :---: | :---: |
| **Fully Connected AE** | 0.02239 | 0.05884 | 0.7328 | 211,040 |
| **Convolutional AE** | 0.00259 | 0.01511 | 0.9731 | 74,497 |
| **Denoising CAE** | 0.00468 | 0.02138 | 0.9442 | 74,497 |
| **VAE** | 0.05533 | 0.12939 | 0.3091 | 134,165 |

### VAE Loss

| Metric | Value |
| :--- | :---: |
| Reconstruction Loss | 177.3696 |
| KL Loss | 2.3794 |
| Total Loss | 179.7489 |

---

## Additional Experiments

- Effect of latent dimension on reconstruction
- Gaussian vs. salt-and-pepper noise
- Different noise levels
- UpSampling vs. Conv2DTranspose decoders
- VAE latent dimensions
- Beta-VAE with different KL weights
- VAE-generated image samples
- Latent-space interpolation

---

## How to Run

1. Open the notebook in the `notebook/` folder.
2. Install the required Python libraries.
3. Run all cells sequentially.

---

## Author

**A. Priyankaa**  
B.Tech Artificial Intelligence & Data Science  
Shiv Nadar University Chennai
