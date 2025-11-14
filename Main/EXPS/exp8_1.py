import os

from PIL import Image, ImageEnhance, ImageFilter, ImageOps

img_path = "../Data/images/image.png"

with Image.open(img_path) as img:
   
   out = img.filter(ImageFilter.DETAIL)
   # out.show()
   
   blur = img.filter(ImageFilter.GaussianBlur(5))
   # blur.show()
   
   gray_img = img.convert('L')  # Convert to grayscale
   
   edged = gray_img.filter(ImageFilter.FIND_EDGES)
   
   edge_enhance = gray_img.filter(ImageFilter.EDGE_ENHANCE)
   ImageEnhance.Contrast(edge_enhance).enhance(2.0)
   
   w, h = img.size
   print(w,h)
   
   ImageEnhance.Brightness(img).enhance(2).show()
   