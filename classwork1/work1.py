import numpy as np
import cv2 as cv

img = cv.imread('image/shurima.jpg', cv.IMREAD_GRAYSCALE)
kernel_size = 20

# สร้างเมทริกซ์เปล่าที่มีค่าเป็น 0
kernel = np.zeros((kernel_size, kernel_size), np.float32)

# กำหนดค่าความชันและค่าคงที่ของสมการเส้นตรง
m = 1  # ค่าความชัน (slope)
c = 2  # ค่าคงที่ (intercept)

# คำนวณและกำหนดค่าในเมทริกซ์ให้เป็น 1 ตามสมการเส้นตรง
for i in range(kernel_size):
    j = int(m * i + c)
    if 0 <= j < kernel_size:
        kernel[j, i] = 1

# ทำการ normalize kernel โดยหารด้วยผลรวมของค่าใน kernel
kernel /= np.sum(kernel)

print(kernel)

output = cv.filter2D(img, -1, kernel, borderType=cv.BORDER_REFLECT)
cv.imwrite('classwork1/input.png', img)
cv.imwrite('classwork1/output.png', output)
