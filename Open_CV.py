import cv2
import numpy as np
import matplotlib.pyplot as plt
 
# Make a black image with a white square
image = np.zeros((100, 100, 3), dtype=np.uint8)
image[20:80, 20:80] = (255, 255, 255)
 
# Convert to grayscale, then make a black-and-white mask
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
_, mask = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
 
# Show all three images
fig, axes = plt.subplots(1, 3, figsize=(9, 3))
 
axes[0].imshow(image)
axes[0].set_title("Original")
axes[1].imshow(gray, cmap="gray")
axes[1].set_title("Grayscale")
axes[2].imshow(mask, cmap="gray")
axes[2].set_title("Threshold mask")
 
for ax in axes:
    ax.axis("off")
 
plt.tight_layout()
plt.show()