# Import the necessary libraries
import cv2
import matplotlib.pyplot as plt

# Load the Image
image = cv2.imread("F:\Suraj Technology\pics art\Ganpati_Bappa.jpg")

# Convert BGR image to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Image rotation parameter
centre = (image_rgb.shape[0]//2 , image_rgb.shape[1] //2)
angle = 10
scale = 1

centre1 = (image_rgb.shape[0]//2 , image_rgb.shape[1] //2)
angle1 = 15
scale1 = 1

# getRotationMatrix2D creates a matrix needed for transformation.
rotation_matrix = cv2.getRotationMatrix2D(centre, angle,scale)
rotation_matrix1 = cv2.getRotationMatrix2D(centre1, angle1,scale1)


# We want matrix for rotation w.r.t center to 30 degree without scaling.
rotated_image = cv2.warpAffine(image_rgb, rotation_matrix, (image.shape[0], image.shape[1]))
rotated_image1 = cv2.warpAffine(image_rgb, rotation_matrix1, (image.shape[0], image.shape[1]))

# Create subplots
fig, axs = plt.subplots(1,3, figsize=(7,4))

#Plot the original image
axs[0].imshow(image_rgb)
axs[0].set_title("Original Image")

# Plot the Rotated image = 0
axs[1].imshow(rotated_image)
axs[1].set_title("Image Rotation:- 45 deg")

# Plot the Rotated image = 1
axs[2].imshow(rotated_image1)
axs[2].set_title("Image Rotation: - 15 deg")

#Remove ticks from the subplots
for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

# Display the subplots
plt.tight_layout()
plt.show()


