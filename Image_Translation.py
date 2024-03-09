# Import the necessary Libraries
import cv2
import matplotlib.pyplot as plt
import numpy as np

#Load the image
image = cv2.imread("F:\Suraj Technology\pics art\Ganpati_Bappa.jpg")

#Convert image BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

width = image_rgb.shape[1]
height = image_rgb.shape[0]

tx = 100
ty = 70

# Translation matrix
translation_matrix = np.array([[1,0,tx],[0,1,ty]], dtype = np.float32)

# warpAffine does appropriate shifting given the Translation matrix.
translated_image = cv2.warpAffine(image_rgb, translation_matrix,(width, height))

#Create subplots
fig, axs = plt.subplots(1,2, figsize= (7,4))

#Plot the original image
axs[0].imshow(image_rgb)
axs[0].set_title("Original Image")
#Plot the translated image
axs[1].imshow(translated_image)
axs[1].set_title("Translated Image")

# Remove ticks from the subplots
for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

#Display the subplots
plt.show()
