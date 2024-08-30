from PIL import Image, ImageEnhance
import numpy as np


img = Image.open(r"D:\Study Material\College - II\OHRC-SIH\Chandrayaan 2 OHRC Lunar Crater Dataset.v4i.multiclass\train\5_jpg.rf.8498e33b0e122225503153d2ce588016.jpg","r")
img.show()

ed1= ImageEnhance.Contrast(img)
ed2= ImageEnhance.Brightness(img)
ed3= ImageEnhance.ImageFilter
img=ed2.enhance(0.4)
img.show()

img= ed1.enhance(2.0)
img.show()

grain_intensity = 0.05

img_array = np.array(img)
noise = np.random.normal(loc=0, scale=grain_intensity*255, size=img_array.shape)
img_array = img_array + noise
img_array = np.clip(img_array, 0, 255).astype(np.uint8)
img_with_grain = Image.fromarray(img_array)


img_with_grain.show()
