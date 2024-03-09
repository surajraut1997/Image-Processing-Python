# Import the necessary libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread(r"F:\Suraj Technology\pics art\Ganpati_Bappa.JPG")
# Convert BGR image to RGB
image_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

# Define the scale factor
#Increase the size by 7 times
scale_factor_1 = 7.0
#Decrease the scale factor by 7 times
scale_factor_2 = 1/7.0

# Get the original image dimension
# The dimension orders is like (height , width , channel ) as we need only height and width we use below code.
height = image_rgb.shape[0]
width = image_rgb.shape[1]

#Calculate the new image dimesion - Increase te size

new_height = int(height*scale_factor_1)
new_width = int(width*scale_factor_1)

zoomed_image = cv2.resize(src=image_rgb,dsize=(new_width, new_height), interpolation=cv2.INTER_CUBIC)

# Again #Calculate the new image dimesion - decrease te size
new_height1 = int(height*scale_factor_2)
new_width1 = int(width*scale_factor_2)

#Scaled Image
scaled_image = cv2.resize(src = image_rgb, dsize= (new_width1, new_height1) , interpolation = cv2.INTER_AREA)

#Create subplots
fig, axs = plt.subplots(1, 3, figsize=(10, 4))

# Plot the original image
axs[0].imshow(image_rgb)
axs[0].set_title(f"Original Image Shape: - {image_rgb.shape}")

# Plot the Zoomed Image
axs[1].imshow(zoomed_image)
axs[1].set_title(f"Zoomed Image Shape:  - {zoomed_image.shape} ")

# Plot the Scaled Image
axs[2].imshow(scaled_image)
axs[2].set_title(f"Scaled Image Shape: - {scaled_image.shape}")

#Remove ticks from the subplots
for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

# Display the subplots
plt.tight_layout()
plt.show()















