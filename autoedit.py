from PIL import Image, ImageEnhance
import os
import numpy as np


def adjust_brightness_contrast_grain(input_folder, output_folder, grain_intensity=1.0, brightness_factor=1.0, contrast_factor=1.0):
    # Create the output directory if not there
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    
    # Looping over all files in the input directory
    for filename in os.listdir(input_folder):
        if filename.endswith((".jpg", ".jpeg", ".png")):  # Process only image files
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)

            # Adjust brightness
            enhancer = ImageEnhance.Brightness(img)
            img = enhancer.enhance(brightness_factor)

            # Adjust contrast
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(contrast_factor)

            #Adjust grain
            img_array = np.array(img)
            noise = np.random.normal(loc=0, scale=grain_intensity*255, size=img_array.shape)
            img_array = img_array + noise
            img_array = np.clip(img_array, 0, 255).astype(np.uint8)
            img_with_grain = Image.fromarray(img_array)

            # Save the modified image to the output directory
            output_path = os.path.join(output_folder, filename)
            img.save(output_path)

            print(f"Edited the {filename} and saved it to {output_path}")

# set Parameters

input_folder = r"C:\Users\shriv\Downloads\Kaggle-LunarCraters\LU3M6TGT_yolo_format\valid\images"
output_folder = r"D:\SIH\Dataset-ImgEdit-Kaggle-wout-Contrast"
brightness_factor = 0.3  # Decreased brightness by x%
contrast_factor = 1.0   # Increased contrast by x%
grain_intensity= 1.0  #Added grain

adjust_brightness_contrast_grain(input_folder, output_folder, brightness_factor, contrast_factor, grain_intensity)    