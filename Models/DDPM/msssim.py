import SimpleITK as sitk
import torch
from cv2.detail import computeImageFeatures2
from torchvision import transforms
import cv2
import numpy as np
from skimage.metrics import structural_similarity

image1 = cv2.imread('./test_data/Chest/p5/p5_IMR.png')
image2 = cv2.imread('./test_data/Chest/p5/p5_Ya.png')
image3 = cv2.imread('./test_data/Chest/p5/p5_Ya2IMR.png')
image4 = cv2.imread('./test_data/Chest/p5/p5_IMR2Ya.png')

image1_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
image2_gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
image3_gray = cv2.cvtColor(image3, cv2.COLOR_BGR2GRAY)
image4_gray = cv2.cvtColor(image4, cv2.COLOR_BGR2GRAY)
(score1, diff) = structural_similarity(image1_gray, image2_gray, full=True)
(score2, diff) = structural_similarity(image1_gray, image3_gray, full=True)
(score3, diff) = structural_similarity(image2_gray, image4_gray, full=True)
print(score1, score2, score3)
# transform = transforms.Compose([transforms.PILToTensor()])
#
# tensor1 = transform(image1)
# tensor1 = tensor1.unsqueeze(0)
# tensor2 = transform(image2)
# tensor2 = tensor2.unsqueeze(0)
# tensor3 = transform(image3)
# tensor3 = tensor3.unsqueeze(0)
# tensor4 = transform(image4)
# tensor4 = tensor4.unsqueeze(0)

# ssim_index = ssim(tensor1, tensor2, data_range=255, size_average=False)
# # msssim_index = ms_ssim(tensor1, tensor2, data_range=255, size_average=False)
#
# print(ssim_index)
