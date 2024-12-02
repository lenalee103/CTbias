import os
import torch
from PIL import Image
from torchvision import transforms
from diffusion_model import DiffusionModel  # Assuming this is your model class

def process_images(input_folder, output_folder, model_path):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Load pretrained model
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = DiffusionModel()  # Initialize your model
    model.load_state_dict(torch.load(model_path, map_location=device))
    model.to(device)
    model.eval()

    # Image preprocessing
    transform = transforms.Compose([
        transforms.Resize((256, 256)),  # Adjust size as needed
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.5], std=[0.5])
    ])

    # Process each image in input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            # Load and preprocess image
            input_path = os.path.join(input_folder, filename)
            img = Image.open(input_path).convert('RGB')
            img_tensor = transform(img).unsqueeze(0).to(device)

            # Generate output
            with torch.no_grad():
                output = model(img_tensor)

            # Convert output tensor to image and save
            output_img = transforms.ToPILImage()(output.squeeze().cpu())
            output_path = os.path.join(output_folder, f'output_{filename}')
            output_img.save(output_path)

if __name__ == "__main__":
    input_folder = "./input_images"  # Path to your input images
    output_folder = "./output_images"  # Path where outputs will be saved
    model_path = "./pretrained_model.pth"  # Path to your pretrained model weights

    process_images(input_folder, output_folder, model_path)
