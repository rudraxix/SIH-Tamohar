from PIL import Image
import os

def bulk_crop_boundingbox(images_folder, labels_folder, output_folder):
    #ensuring folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(images_folder):
        if filename.endswith(('.png', '.jpeg', '.jpg')):
            image_path = os.path.join(images_folder, filename)
            label_path = os.path.join(labels_folder, os.path.splitext(filename)[0] + '.txt')
            
            img= Image.open(image_path)
            img_width, img_height = img.size
            
            #check whether label exists
            if not os.path.exists(label_path):
                print(f"Label file not found for : {filename}")
                continue
            
            with open(label_path, "r") as f:
                lines = f.readlines()
                
            #bounding box visualisation for the cropping
            for i, line in enumerate(lines):
                class_id, x_center, y_center, width, height = map(float, line.split())
                
                x_pixel= x_center* img_width
                y_pixel= y_center* img_height
                bbox_width_pixel = width* img_width
                bbox_height_pixel = height* img_height
                
                x_min = int(x_pixel - (bbox_width_pixel / 2))
                y_min = int(y_pixel - (bbox_height_pixel / 2))
                x_max = int(x_pixel + (bbox_width_pixel / 2))
                y_max = int(y_pixel + (bbox_height_pixel / 2))
                
                cropped_img = img.crop((x_min, y_min, x_max, y_max))
                cropped_img_name = f"{os.path.splitext(filename)[0]}_crop{i}.png"
                cropped_img.save(os.path.join(output_folder, cropped_img_name))

                print(f"Cropped according to the bounding boxes for {filename} and saved it to {output_folder}")

#specifying the values for function
images_folder = r"C:\Users\shriv\Downloads\Kaggle-LunarCraters\LU3M6TGT_yolo_format\train\images"
labels_folder = r"C:\Users\shriv\Downloads\Kaggle-LunarCraters\LU3M6TGT_yolo_format\train\labels"
output_folder = r"D:\SIH\Kaggle-8000-BoundingboxCropped"


bulk_crop_boundingbox(images_folder, labels_folder, output_folder)