# Bias Elimination in CT Reconstruction Modalities: A Comparative Study

This repository contains the code, data, and analysis for our research on addressing bias in different CT reconstruction modalities (IMR and iDose Ya) using three approaches: Gaussian Filter (GS), CycleGAN, and Denoising Diffusion Model (DM). Our work thoroughly evaluates these methods, providing insights into their strengths, weaknesses, and applications for researchers and physicians.

---

## **Repository Contents**
- `data/`  
  Contains sample data used for the evaluation, including CT reconstructions from different modalities (IMR and iDose Ya).

- `Models/`  
  Implementation of the three methods: Gaussian Filter, CycleGAN, and Denoising Diffusion Model. Each method is in its respective folder with training scripts, preprocessing pipelines, and evaluation utilities.

- `results/`  
  SSIM score analysis, violin plots, and performance metrics used in the paper.

- `notebooks/`  
  Jupyter Notebooks for visualizing and analyzing the results, including cross-modality and in-modality comparisons.

- `figures/`  
  Plots and figures (e.g., SSIM violin plots) presented in the paper.

- `README.md`  
  This file, explaining the repository structure, methods, and instructions for use.

---

## **Background**
CT reconstruction modalities often introduce inherent biases, impacting image quality and structural similarity. Our study evaluates:
- **Gaussian Filter (GS):** A simple smoothing filter that reduces noise but may blur important signal details.
- **CycleGAN:** A machine learning-based approach capable of generating high-quality images but prone to variability in similarity performance.
- **Denoising Diffusion Model (DM):** A robust generative model offering consistent high-quality outputs but at higher computational costs.

---

## **Method Performance**
| **Method**        | **Computation Speed** | **Similarity Check** | **Image Quality** |
|--------------------|-----------------------|-----------------------|-------------------|
| Gaussian Filter    | ++                   | ++                    | -                 |
| CycleGAN           | +                    | -                     | ++                |
| Denoising Diffusion| -                    | +                     | ++                |

- Gaussian Filter: Effective and fast but blurs fine details.
- CycleGAN: High-quality images but inconsistent in similarity.
- Diffusion: Best generalization and consistency, at the cost of computation time.

---

## **Installation and Setup**
1. Clone the repository:
   ```bash
   git clone https://github.com/lenalee103/CTbias.git
   cd CTbias
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
  
## **Usage**

### Data Preprocessing
Run the preprocessing script to prepare the data for analysis:

    ```bash
    python code/preprocess.py --input data/ --output processed_data/

### Method Evaluation
1. Gaussian Filter:
    ```bash
    python code/gs/apply_gs.py --input processed_data/ --output results/gs/

2. CycleGAN:
    ```bash
    python code/cyclegan/train.py --data processed_data/ --output results/cyclegan/

3. Diffusion:
    ```bash
    python code/diffusion/train.py --data processed_data/ --output results/diffusion/

4. Visualization
Use the provided notebooks to generate violin plots and compare results:
    ```bash
    jupyter notebook notebooks/visualization.ipynb

## Key Findings
Gaussian Filter (GS): Quick and effective for basic bias reduction but lacks detail preservation due to signal blurring.
CycleGAN: Provides high-quality reconstructions but struggles with variability in similarity.
Denoising Diffusion Model (DM): Offers the most robust and consistent results, making it ideal for bias elimination and data augmentation in machine learning applications.
Applications
Physicians and Researchers: Provides insights into selecting appropriate methods for CT modality bias elimination based on their specific needs (e.g., speed, similarity, or image quality).
Machine Learning: Useful for data augmentation to improve generalization across CT modalities.

## License

This repository is licensed under the MIT License.

## Contributions
We welcome contributions to enhance this project! If you’d like to contribute, please:

Fork the repository.
Create a new branch for your feature or bug fix.
Submit a pull request describing your changes.

## Citation
If you use this work in your research, please cite:




