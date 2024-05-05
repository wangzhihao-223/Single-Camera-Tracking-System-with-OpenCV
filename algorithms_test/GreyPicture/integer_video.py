#! /usr/bin/python3
import cv2
import numpy as np
# 定义
def integer_gray_image_processing(image):
    greyFrame = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Convert pixel values to integers
    image_int = greyFrame.astype(int)
    
    # Example processing: Invert the image
    inverted_image_int = 255 - image_int
    
    # Convert pixel values back to uint8 type
    inverted_image = inverted_image_int.astype(np.uint8)
    
    return inverted_image

# 从摄像头读取视频，参数 0 表示默认摄像头
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 整型灰度处理
    processed_image = integer_gray_image_processing(frame)

    # 显示原始帧和去噪后的帧
    cv2.imshow('Original Frame', frame)
    cv2.imshow('integer_grey_video', processed_image)

    if cv2.waitKey(30) & 0xFF == 27:  # 按Esc键退出
        break

cap.release()
cv2.destroyAllWindows()
