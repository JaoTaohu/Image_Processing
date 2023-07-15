import numpy as np
import cv2 as cv

img = cv.imread('image/Cup1.jpg', cv.IMREAD_GRAYSCALE)

#cast data type to float32
img = img.astype(np.float32);

#take fourier transform
imgF = np.fft.fft2(img)

#ship(0,0) to center of image
imgF = np.fft.fftshift(imgF)

#find magnitude & phase
imgReal = np.real(imgF)
imglma = np.imag(imgF)
imgMag = np.sqrt(imgReal**2 + imglma**2)
imgPhs = np.arctan2(imglma, imgReal)

#inverse fourier transform
imgRealinv = imgMag*np.cos(imgPhs)
imglmainv = imgMag*np.sin(imgPhs)

imgFinv = imgRealinv + imglmainv*1j

imgFinv = np.fft.ifftshift(imgFinv)
imgInv = np.fft.ifft2(imgFinv)

imgInv = np.real(imgInv)
imgInv = imgInv.astype(np.uint8)

cv.imwrite('fourier/input.png', img)
cv.imwrite('fourier/output.png', imgInv)

imgMag = np.log(1+imgMag)
imgMag = cv.normalize(imgMag, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)
cv.imwrite('fourier/magnitude.png', imgMag)