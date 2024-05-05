#! /usr/bin/python3
import cv2

# 读取视频
cap = cv2.VideoCapture(0)

# 使用MOG2背景减除器
background_subtractor = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 背景减除
    fg_mask = background_subtractor.apply(frame)

    # 显示分割结果
    cv2.imshow('Segmented Image', fg_mask)

    if cv2.waitKey(30) & 0xFF == 27:  # 按Esc键退出
        break

cap.release()
cv2.destroyAllWindows()
