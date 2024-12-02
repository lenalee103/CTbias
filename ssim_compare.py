import os
import cv2
import numpy as np
import pandas as pd
from skimage.metrics import structural_similarity as ssim


def compare_images(image1_path, image2_path):
    # Read images
    img1 = cv2.imread(image1_path)
    img2 = cv2.imread(image2_path)

    # Convert images to grayscale
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    if img2 is None:
        print(f"Error: Unable to read image from {image2_path}")
        return 0  # or handle this error case as appropriate
    elif len(img2.shape) == 3:
        gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    else:
        gray2 = img2

        # Compute SSIM between the two images
    score, _ = ssim(gray1, gray2, full=True)
    return score


def compare_folders(folder1, folder2):
    results = []

    # Get list of image files in both folders and sort them
    image_extensions = ('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')
    files1 = sorted([f for f in os.listdir(folder1) if f.lower().endswith(image_extensions)])
    files2 = sorted([f for f in os.listdir(folder2) if f.lower().endswith(image_extensions)])

    # Use min length to avoid index errors when folders have different sizes
    min_files = min(len(files1), len(files2))
    for file1, file2 in zip(files1[:min_files], files2[:min_files]):
        path1 = os.path.join(folder1, file1)
        path2 = os.path.join(folder2, file2)

        if os.path.isfile(path1) and os.path.isfile(path2):
            # Read and resize images to 256x256 before comparison
            img1 = cv2.imread(path1)
            img2 = cv2.imread(path2)
            img1 = cv2.resize(img1, (256, 256))
            img2 = cv2.resize(img2, (256, 256))
            # Convert to grayscale and compare
            gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
            gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
            ssim_score, _ = ssim(gray1, gray2, full=True)
            # Calculate PSNR
            # img1 = cv2.imread(path1)
            # img2 = cv2.imread(path2)
            # img1 = cv2.resize(img1, (256, 256))
            # img2 = cv2.resize(img2, (256, 256))
            mse = np.mean((img1 - img2) ** 2)
            if mse == 0:
                psnr = float('inf')
            else:
                psnr = 20 * np.log10(255.0 / np.sqrt(mse))
            results.append({
                'File1': file1, 
                'File2': file2, 
                'SSIM Score': ssim_score,
                'PSNR Score': psnr
            })
            
    # Convert results to a DataFrame
    df_results = pd.DataFrame(results)
    return df_results


# Example usage
# folder1 = "./datasets/IMRSlices/IMR2D6206878_ThaxLF2KM_IMR.nii"
folder1 = "./datasets/lr_dn_p1_B"
folder2 = "./datasets/YaSlices/Ya2D5288895_ThaxLF2KM_Y.nii"

comparison_results = compare_folders(folder1, folder2)

# Display the DataFrame
print(comparison_results)

# Store the DataFrame into a CSV file named 'patient1.csv'
comparison_results.to_csv('patient1_lr_dn_Ya.csv', index=False)