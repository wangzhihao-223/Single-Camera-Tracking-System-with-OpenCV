#! /usr/bin/python3
import cv2

# 读取视频
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 将帧转换为灰度图像
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 使用阈值进行分割
    _, segmented_image = cv2.threshold(gray_frame, 127, 255, cv2.THRESH_BINARY)

    # 显示分割结果
    cv2.imshow('Segmented Image', segmented_image)

    if cv2.waitKey(30) & 0xFF == 27:  # 按Esc键退出
        break

cap.release()
cv2.destroyAllWindows()
