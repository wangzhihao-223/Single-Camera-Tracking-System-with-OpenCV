import cv2
import numpy as np

def float_gray_image_processing(frame, adjustment):
    greyFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Convert pixel values to integers
    
    frame_int = greyFrame.astype(int)
    
    # Apply brightness adjustment to each pixel
    adjusted_frame_int = frame_int + adjustment
    
    # Limit pixel values to the range 0-255
    adjusted_frame_int[adjusted_frame_int < 0] = 0
    adjusted_frame_int[adjusted_frame_int > 255] = 255
    
    # Convert pixel values back to uint8 type
    adjusted_frame = adjusted_frame_int.astype(np.uint8)
    
    return adjusted_frame

# 从摄像头读取视频，参数 0 表示默认摄像头
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 整型灰度处理
    processed_image = float_gray_image_processing(frame, adjustment = 1.5)

    # 显示原始帧和去噪后的帧
    cv2.imshow('Original Frame', frame)
    cv2.imshow('processed_image', processed_image)

    if cv2.waitKey(30) & 0xFF == 27:  # 按Esc键退出
        break

cap.release()
cv2.destroyAllWindows()
