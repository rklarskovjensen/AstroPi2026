import cv2
import numpy as np
#from fastiecm import fastiecm
#original = cv2.imread('ISS_billeder\cslab3ogel_Files_RawData_raw_image_222.jpeg')

from exif import Image
from datetime import datetime
import math

from picamzero import Camera








def display(image, image_name):
    image = np.array(image, dtype=float)/float(255)
    shape = image.shape
    height = int(shape[0] / 2)
    width = int(shape[1] / 2)
    image = cv2.resize(image, (width, height))
    cv2.namedWindow(image_name)
    cv2.imshow(image_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def contrast_stretch(im):
    in_min = np.percentile(im, 5)
    in_max = np.percentile(im, 95)

    out_min = 0.0
    out_max = 255.0

    out = im - in_min
    out *= ((out_min - out_max) / (in_min - in_max))
    out += in_min

    return out
def calc_ndvi(image):
    b, g, r = cv2.split(image)
    bottom = (r.astype(float) + b.astype(float))
    bottom[bottom==0] = 0.01
    ndvi = (b.astype(float) - r) / bottom
    return ndvi

# Create an instance of the Camera class
cam = Camera()

# Capture an image

cam.take_photo("image1.jpg")
image_1 = 'image1.jpg'
original = cv2.imread(image_1)

#original = cv2.imread('ISS_billeder\cslab3ogel_Files_RawData_raw_image_222.jpeg')

#display(original, 'Original')
contrasted = contrast_stretch(original)
#display(contrasted, 'Contrasted original')
cv2.imwrite('contrasted.png', contrasted)
ndvi = calc_ndvi(contrasted)
#display(ndvi, 'NDVI')
cv2.imwrite('ndvi.png', ndvi)
ndvi_contrasted = contrast_stretch(ndvi)
#display(ndvi_contrasted, 'NDVI Contrasted')
cv2.imwrite('ndvi_contrasted.png', ndvi_contrasted)

#color_mapped_prep = ndvi_contrasted.astype(np.uint8)
#color_mapped_image = cv2.applyColorMap(color_mapped_prep, fastiecm)
#display(color_mapped_image, 'Color mapped')
#cv2.imwrite('color_mapped_image.jpg', color_mapped_image)
