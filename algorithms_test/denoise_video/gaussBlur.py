#! /usr/bin/python3
import cv2

# 从摄像头读取视频，参数 0 表示默认摄像头
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 高斯滤波去噪
    blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)

    # 写入原始帧和去噪后的帧到文件系统
    cv2.imwrite("tmp_data/bilat/original.jpg", frame)
    cv2.imwrite("tmp_data/bilat/bilateral.jpg", blurred_frame)

    # 显示原始帧和去噪后的帧
    cv2.imshow('原图片', frame)
    cv2.imshow('高斯滤波处理图', blurred_frame)

    if cv2.waitKey(30) & 0xFF == 27:  # 按Esc键退出
        break

cap.release()
cv2.destroyAllWindows()
