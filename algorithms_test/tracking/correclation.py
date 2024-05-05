#! /usr/bin/python3
import cv2
import numpy as np

# 读取视频文件或摄像头
cap = cv2.VideoCapture(1)

# 读取第一帧并选择ROI
_, frame = cap.read(1)
roi = cv2.selectROI('Select Object', frame)
cv2.destroyAllWindows()

# 获取ROI图像并显示
x, y, w, h = int(roi[0]), int(roi[1]), int(roi[2]), int(roi[3])
roi_img = frame[y:y+h, x:x+w]
cv2.imshow('Selected ROI', roi_img)
cv2.waitKey(0)  # 等待按下任意键继续

# 设置初始的跟踪窗口
track_window = (x, y, w, h)

# 获取ROI图像并计算直方图
hsv_roi = cv2.cvtColor(roi_img, cv2.COLOR_BGR2HSV)
roi_hist = cv2.calcHist([hsv_roi], [0], None, [256], [0, 256])
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

# 设置相关跟踪参数
term_criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 将当前帧转换为HSV颜色空间
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 计算反向投影
    dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

    # 运行均值漂移以获取新的目标位置
    ret, track_window = cv2.meanShift(dst, track_window, term_criteria)

    # 更新ROI位置
    x, y, w, h = track_window

    # 在图像上绘制跟踪窗口
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # 显示跟踪结果
    cv2.imshow('Correlation Tracking', frame)

    # 检测键盘输入，按 'q' 键退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()
