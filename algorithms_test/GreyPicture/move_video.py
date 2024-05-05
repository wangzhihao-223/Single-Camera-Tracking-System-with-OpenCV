import cv2
import numpy as np


def move_gray_image_processing(image, factor):
    # 将图像数据类型转换为int16
    greyFrame = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_int16 = greyFrame.astype(np.int16)
    
    # 应用对比度调整
    adjusted_image_int16 = image_int16 * factor
    
    # 将超出范围的像素值限制在0-255之间
    adjusted_image_int16[adjusted_image_int16 < 0] = 0
    adjusted_image_int16[adjusted_image_int16 > 255] = 255
    
    # 将图像数据类型转换回uint8
    adjusted_image = adjusted_image_int16.astype(np.uint8)
    return adjusted_image


# 从摄像头读取视频，参数 0 表示默认摄像头
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 整型灰度处理
    processed_image = move_gray_image_processing(frame, factor = 1.5)

    # 显示原始帧和去噪后的帧
    cv2.imshow('Original Frame', frame)
    cv2.imshow('integer_grey_video', processed_image)

    if cv2.waitKey(30) & 0xFF == 27:  # 按Esc键退出
        break

cap.release()
cv2.destroyAllWindows()