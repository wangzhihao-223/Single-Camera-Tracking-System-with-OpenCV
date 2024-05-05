#! /usr/bin/python3
import cv2

# 从摄像头读取视频，参数 0 表示默认摄像头
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 均值滤波
    averaged_frame = cv2.blur(frame, (5, 5))

    # 写入原始帧和去噪后的帧到文件系统
    cv2.imwrite("tmp_data/bilat/original.jpg", frame)
    cv2.imwrite("tmp_data/bilat/bilateral.jpg", averaged_frame)
    # 显示原始帧和均值滤波后的帧
    cv2.imshow('Original', frame)
    cv2.imshow('meanFilter', averaged_frame)

    if cv2.waitKey(30) & 0xFF == 27:  # 按Esc键退出
        break

cap.release()
cv2.destroyAllWindows()
