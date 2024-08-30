from PIL import Image
import os

img= Image.open(r"C:\Users\shriv\Downloads\Kaggle-LunarCraters\LU3M6TGT_yolo_format\train\images\99.86369132681097,101.2355721666483,58.44674068374186,59.81862152357916.png")
img_width, img_height = img.size


with open(r"C:\users\shriv\Downloads\Kaggle-LunarCraters\LU3M6TGT_yolo_format\train\labels\99.86369132681097,101.2355721666483,58.44674068374186,59.81862152357916.txt") as f:
    lines = f.readlines()

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
cropped_img.show()



