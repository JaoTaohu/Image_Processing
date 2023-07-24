import numpy as np 
import cv2 as cv


img = cv.imread('image/shurima.jpg', cv.IMREAD_GRAYSCALE)

#1) สร้าง Sobel Filter แบบ Horizontal หรือ Vertical อย่างใดอย่างหนึ่งใน Spatial Domain
sobel_filt = np.array([[1,2,1],
                       [0,0,0],
                       [-1,-2,-1]])

solbel = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=3)
imgtest = cv.normalize(solbel, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)

#2) แปลงภาพ Input ให้อยู่ใน Frequency Domain ด้วย Fourier Transform
imgF = np.fft.fft2(img)

#3) แปลง Filter Sobel ให้อยู่ใน Frequency Domain ด้วย Fourier Transform
h, w = img.shape
padded_filt = np.pad(sobel_filt, ((0, h-3), (0, w-3)), mode='constant', constant_values=0)
filterF = np.fft.fft2(padded_filt)

#4) นำภาพ Input และ Filter Sobel ใน Frequency Domain มาทำการคูณกันแบบจุดต่อจุด (Dot Product)
resultF = imgF * filterF

#5) แปลงภาพผลลัพธ์กลับมายัง Spatial Domain
imgInv = np.fft.ifft2(resultF)
imgInv = np.real(imgInv)
imgReal = cv.normalize(imgInv, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)

cv.imwrite('Classwork4/result.png', imgReal)
cv.imwrite('Classwork4/original.png', imgtest)

#6) เปรียบเทียบผลลัพธ์ที่ได้ระหว่างการทำ Filter Sobel ใน Spatial Domain และ Frequency Domain ว่าเหมือนกันหรือไม่
compare_img = cv.hconcat([imgReal, imgtest])
cv.imwrite('Classwork4/compare.png', compare_img)
