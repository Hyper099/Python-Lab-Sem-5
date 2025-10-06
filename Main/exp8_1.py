from PIL import Image, ImageFilter, ImageEnhance, ImageOps
import os

img_path = "./Data/images/image.png"

with Image.open(img_path) as img:
   print(f"Image Format: {img.format}")
   print(f"Image Size: {img.size}")
   print(f"Image Mode: {img.mode}")
