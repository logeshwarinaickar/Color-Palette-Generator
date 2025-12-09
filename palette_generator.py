import cv2
import numpy as np 
import matplotlib.pyplot as plt

import matplotlib
matplotlib.use("Agg")


image_path = "IMAGES/ocean.jpg"
image = cv2.imread(image_path)

if image is None:
    print("Error! Image not shown")
    exit()

image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

max_size = 500  
height, width = image.shape[:2]

if max(height, width) > max_size:
    scale = max_size / max(height, width)
    new_size = (int(width * scale), int(height * scale))
    image = cv2.resize(image, new_size)
    print(f"Resized image to {new_size} for faster processing")

#plt.imshow(image) 
#plt.axis('off') 
#plt.show()


pixels = image.reshape((-1,3))
print("Shape of pixel array: ", pixels.shape)

num_colors = 5 
pixels = np.float32(pixels)
criteria = (cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,20,0.2)

_,labels,centers = cv2.kmeans(pixels,num_colors,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
centers = np.uint32(centers)
print("DOMINANT COLORS (RGB): ",centers)

palette = np.zeros((50,300,3),dtype= np.uint8)
block_width =  300//num_colors

for i,colors in enumerate(centers):
    start_pt = i * block_width
    end_pt = (i+1) * block_width
    palette[:,start_pt:end_pt] = colors

plt.figure(figsize=(6,2))
#plt.imshow(palette)
#plt.axis('off') 
#plt.show()

import os

if not os.path.exists("output/images"):
    os.makedirs("output/images")
if not os.path.exists("output/palettes"): 
    os.makedirs("output/palettes")

output_path = f"output/palettes/{os.path.basename(image_path)}" 
cv2.imwrite(output_path, cv2.cvtColor(palette, cv2.COLOR_RGB2BGR))
print(f"Palette saved as {output_path}")

img_path = f"output/images/{os.path.basename(image_path)}"
cv2.imwrite(img_path, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
print("Input image saved inside output/images")


import json
colors_list = centers.tolist()  #numpy array to list
with open("output/colors.json", "w") as f:
    json.dump(colors_list, f)

print("RGB values saved to output/colors.json")
