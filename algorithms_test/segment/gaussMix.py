#! /usr/bin/python3
import cv2

# 从摄像头读取视频，参数 0 表示默认摄像头
cap = cv2.VideoCapture(0)

# 创建GMM背景减除器
gmm = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 背景减除
    fg_mask = gmm.apply(frame)

    # 显示分割结果
    cv2.imshow('Segmented Image', fg_mask)

    if cv2.waitKey(30) & 0xFF == 27:  # 按Esc键退出
        break

cap.release()
cv2.destroyAllWindows()
