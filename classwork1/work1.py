import numpy as np
import cv2

# Create a black image with a white background
def line():
    image = np.zeros((500, 500, 3), dtype=np.uint8)

    # Define the start and end points of the line
    start_point = (50, 50) # (x1, y1)
    end_point = (400, 400) # (x2, y2)

# Calculate the slope and intercept of the line
    slope = (end_point[1] - start_point[1]) / (end_point[0] - start_point[0])
    intercept = start_point[1] - slope * start_point[0]

# Iterate over the x-coordinates of the line and set corresponding pixel values
    for x in range(start_point[0], end_point[0] + 1):
        y = int(slope * x + intercept)
        image[y, x] = (255, 255, 255) #set colour
    
    cv2.imwrite("classwork1/Linear Line.png", image)
    

    
cv2.waitKey(0)
cv2.destroyAllWindows()
