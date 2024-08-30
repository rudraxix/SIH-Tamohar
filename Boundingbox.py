import os
from PIL import Image, ImageDraw

def bounding_box_visuals(input_folder, label_folder, output_folder):
    # Ensure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # loop over all image files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png')):  
            image_path = os.path.join(input_folder, filename)
    
    #loop over label files in input folder
    for filename in os.listdir(label_folder):
        if filename.endswith(('.txt')):
            label_path = os.path.join(label_folder, os.path.splitext(filename)[0] + '.txt')


def visualize_yolo_bboxes(image_path, label_path, output_path=None):
    img = Image.open(image_path)  # Load the image
    img_width, img_height = img.size  # Get image dimensions

    draw = ImageDraw.Draw(img)  # Create a drawing context

    with open(label_path, 'r') as f:
        lines = f.readlines()

    # Process each bounding box
    for line in lines:
        class_id, x_center, y_center, width, height = map(float, line.split())

        x_center_pixel = x_center*img_width
        y_center_pixel = y_center*img_height
        bbox_width_pixel = width*img_width
        bbox_height_pixel = height*img_height

        x_min = int(x_center_pixel- (bbox_width_pixel / 2))
        y_min = int(y_center_pixel- (bbox_height_pixel / 2))
        x_max = int(x_center_pixel+ (bbox_width_pixel / 2))
        y_max = int(y_center_pixel+ (bbox_height_pixel / 2))

        draw.rectangle([x_min, y_min, x_max, y_max], outline="red", width=2)

        output_path = os.path.join(output_folder, filename)
        img.save(output_path)

        print(f"Created bounding boxes for the {filename} and saved it to {output_path}")


input_folder = r"C:\Users\shriv\Downloads\Kaggle-LunarCraters\LU3M6TGT_yolo_format\train\images"
label_folder = r"C:\Users\shriv\Downloads\Kaggle-LunarCraters\LU3M6TGT_yolo_format\train\labels"
output_folder = r"D:\SIH\Kaggle-8000-Boundingboxes"


bounding_box_visuals(input_folder, label_folder, output_folder)
visualize_yolo_bboxes(image_path, label_path, output_path=None)