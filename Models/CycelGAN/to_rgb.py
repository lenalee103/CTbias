import os
from PIL import Image


def convert_images_to_rgb(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            try:
                # Open the image
                with Image.open(input_path) as img:
                    # Convert the image to RGB mode
                    rgb_img = img.convert('RGB')

                    # Save the RGB image, replacing the original
                    rgb_img.save(output_path)

                print(f"Converted {filename} to RGB")
            except Exception as e:
                print(f"Error converting {filename}: {str(e)}")


# Example usage
input_folder = './datasets/IMR2Ya/test/A'
output_folder = './datasets/IMR2Ya_RGB/test/A'
convert_images_to_rgb(input_folder, output_folder)