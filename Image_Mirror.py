# Import the necessary libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread(r"F:\Suraj Technology\pics art\Ganpati_Bappa.JPG")
# Convert BGR image to RGB
image_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
# Perform mirror reflection (horizontal flip)
mirrored_image = cv2.flip(image_rgb, 1)


# Plot the mirrored image
plt.imshow(mirrored_image)

plt.title("Mirror Reflection")
plt.axis('off')
plt.show()