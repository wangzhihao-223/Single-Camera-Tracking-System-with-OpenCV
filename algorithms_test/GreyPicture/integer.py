import cv2
import numpy as np

def integer_gray_image_processing(image):
    # Convert pixel values to integers
    image_int = image.astype(int)
    
    # Example processing: Invert the image
    inverted_image_int = 255 - image_int
    
    # Convert pixel values back to uint8 type
    inverted_image = inverted_image_int.astype(np.uint8)
    
    return inverted_image

# Read a grayscale image
image = cv2.imread('../flower.png', cv2.IMREAD_GRAYSCALE)

# Perform integer-based image processing
processed_image = integer_gray_image_processing(image)

# Display the original and processed images
cv2.imshow('Original Image', image)
cv2.imshow('Processed Image', processed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
