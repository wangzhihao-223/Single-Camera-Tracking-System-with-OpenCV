#! /usr/bin/python3
import cv2
import numpy as np

# 打开视频文件
cap = cv2.VideoCapture(0)

while cap.isOpened():
    # 读取一帧
    ret, frame = cap.read()

    if not ret:
        break

    # 转换为灰度图像
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 使用阈值分割（参数可以根据实际情况调整）
    _, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    # 寻找轮廓
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 遍历每个轮廓
    for contour in contours:
        # 计算轮廓的质心
        M = cv2.moments(contour)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])

            # 在图像上标注质心
            cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1)

    # 显示帧
    cv2.imshow('Centroid Tracking', frame)

    # 如果按下 'Esc' 键则退出循环
    if cv2.waitKey(30) & 0xFF == 27:
        break

# 释放视频捕捉对象和关闭窗口
cap.release()
cv2.destroyAllWindows()
