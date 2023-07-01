import cv2
import numpy as np

def local_gamma_correction(image, block_size, threshold_low, threshold_high, gamma_low, gamma_high):
    height, width = image.shape[:2]
    corrected_image = np.zeros_like(image, dtype=np.float32)

    for y in range(0, height - block_size, block_size):
        for x in range(0, width - block_size, block_size):
            block = image[y:y+block_size, x:x+block_size]

            # Compute histogram and mean
            hist = cv2.calcHist([block], [0], None, [256], [0, 256])
            mean_value = np.mean(hist)

            if mean_value < threshold_low:
                gamma = gamma_low
            elif mean_value > threshold_high:
                gamma = gamma_high
            else:
                gamma = 1.0

            # Apply gamma correction
            corrected_block = np.power(block / 255.0, 1.0 / gamma) * 255.0
            corrected_block = np.clip(corrected_block, 0, 255).astype(np.uint8)

            corrected_image[y:y+block_size, x:x+block_size] = corrected_block

    return corrected_image.astype(np.uint8)

input_image = cv2.imread('image/yy.jpg', 0)  # Read grayscale image
block_size = 64
threshold_low = 100
threshold_high = 150
gamma_low = 0.5
gamma_high = 1.5

output_image = local_gamma_correction(input_image, block_size, threshold_low, threshold_high, gamma_low, gamma_high)

cv2.imshow('Input Image', input_image)
cv2.imshow('Output Image', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


