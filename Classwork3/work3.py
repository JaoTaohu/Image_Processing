import cv2 as cv
import random

image = cv.imread('image/shurima.jpg', cv.IMREAD_GRAYSCALE)
img = cv.imread('image/shurima.jpg', cv.IMREAD_GRAYSCALE)

density_salt = 0.1
density_pepper = 0.1

number_of_white_pixel = int(density_salt*(img.shape[0]*img.shape[1]))

for i in range(number_of_white_pixel):
    y_coord = random.randint(0, img.shape[0]-1)
    x_coord = random.randint(0, img.shape[1]-1)
    img[y_coord][x_coord] = 255


number_of_black_pixel = int(density_pepper*(img.shape[0]*img.shape[1]))

for i in range(number_of_black_pixel):
    y_coord = random.randint(0, img.shape[0]-1)
    x_coord = random.randint(0, img.shape[1]-1)
    img[y_coord][x_coord] = 0

median_blur= cv.medianBlur(img, 5)

cv.imwrite('Classwork3/img with sp.png', img)
cv.imwrite('Classwork3/img without sp.png', median_blur)
cv.imwrite('Classwork3/Original.png', image)
