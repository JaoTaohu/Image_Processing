import numpy as np
import cv2 as cv

img = np.zeros([600,600], dtype = np.uint8)

centerX = 100
centerY = 100

radius = 30

for y in range(centerY - radius , centerY + radius + 1):
    for x in range(centerX - radius , centerX + radius + 1):
        if(x - centerX)**2 + (y - centerY)**2 <= radius**2:
            img[y,x] = 255


cv.imshow('Circle',img)

cv.waitKey(0)
cv.destroyAllWindows()