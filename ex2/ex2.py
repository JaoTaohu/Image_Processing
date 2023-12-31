import cv2 as cv
import numpy as np

img_in = cv.imread("image\Cup1.jpg")

gamma = 1.5
gamma_corrected = (img_in / 255)**gamma

gamma_corrected = gamma_corrected*255

img_out = np.array(gamma_corrected, dtype = 'uint8')

cv.imshow('Power-law', img_out)

cv.imwrite('Demo03_Pow_img_input.png',img_in)
cv.imwrite('Demo03_Pow_img_output.png',img_out)