import numpy as np
import cv2

# Load the image
image_path = "image/cc.png"  # Replace with the path to your image
image = cv2.imread(image_path)

# Reverse the color
reversed_image = 255 - image

# Display the reversed image
cv2.imshow("Reversed Image", reversed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
