import os
import nibabel as nib
import numpy as np
from scipy.ndimage import gaussian_filter
from pathlib import Path

def apply_gaussian_filter(input_folder):
    # Create output folder with "GaussianFilter" added to the input folder name
    output_folder = input_folder + "_GaussianFilter"
    Path(output_folder).mkdir(parents=True, exist_ok=True)

    # Get all .nii files in the input folder
    nii_files = [f for f in os.listdir(input_folder) if f.endswith('.nii') or f.endswith('.nii.gz')]

    for nii_file in nii_files:
        input_path = os.path.join(input_folder, nii_file)
        output_path = os.path.join(output_folder, nii_file)

        # Load the NIfTI image
        img = nib.load(input_path)
        data = img.get_fdata()

        # Apply 3D Gaussian filter
        # Convert FWHM to sigma: sigma = FWHM / (2 * sqrt(2 * ln(2)))
        sigma = 2 / (2 * np.sqrt(2 * np.log(2)))
        # Use 15x15x15 kernel size (truncate at 7.5 to get 15x15x15)
        filtered_data = gaussian_filter(data, sigma=(sigma, sigma, sigma), truncate=7.5)

        # Create a new NIfTI image with the filtered data
        filtered_img = nib.Nifti1Image(filtered_data, img.affine, img.header)

        # Save the filtered image
        nib.save(filtered_img, output_path)

        print(f"Processed: {nii_file}")

# Example usage
input_folder = "./Datasets/Ya"
apply_gaussian_filter(input_folder)


