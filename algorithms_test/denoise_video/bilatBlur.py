#! /usr/bin/python3
import cv2

# 从摄像头读取视频，参数 0 表示默认摄像头
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 双边滤波去噪
    bilateral_frame = cv2.bilateralFilter(frame, 9, 75, 75)

     # 写入原始帧和去噪后的帧到文件系统
    cv2.imwrite("tmp_data/bilat/original.jpg", frame)
    cv2.imwrite("tmp_data/bilat/bilateral.jpg", bilateral_frame)
    
    # 显示原始帧和去噪后的帧
    cv2.imshow('原图片', frame)
    cv2.imshow('双边滤波处理图', bilateral_frame)

    if cv2.waitKey(30) & 0xFF == 27:  # 按Esc键退出
        break

cap.release()
cv2.destroyAllWindows()
