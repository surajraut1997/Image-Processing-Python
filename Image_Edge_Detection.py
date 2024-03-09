# Import the necessary Libraries
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load the Image
Image = cv2.imread("F:\Suraj Technology\pics art\Ganpati_Bappa.jpg")

#Convert Image BGR to RGB
Image_rgb = cv2.cvtColor(Image, cv2.COLOR_BGR2RGB)

# Apply Canny edge detection
edges = cv2.Canny(Image_rgb, threshold1= 100, threshold2 = 700)

#Create subplots
fig, axs = plt.subplots(1,2,figsize =(7,4))

#Plot the original image
axs[0].imshow(Image_rgb)
axs[0].set_title("Original Image")

#Plot the edge detection  image
axs[1].imshow(edges)
axs[1].set_title("Edge detection")

#Remove ticks from the subplots

for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

#Display the subplots
plt.tight_layout()
plt.show()

