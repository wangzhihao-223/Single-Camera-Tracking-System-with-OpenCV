#! /usr/bin/python3
import cv2
import numpy as np

cap = cv2.VideoCapture(0)


while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    # 转换为灰度图像
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 计算光流
    new_corners, status, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, corners, None)

    # 筛选跟踪成功的角点
    good_new = new_corners[status == 1]
    good_old = corners[status == 1]

    # 计算场景锁定变换矩阵
    M, _ = cv2.estimateAffinePartial2D(good_old, good_new)

    # 应用变换矩阵到原始帧
    result_frame = cv2.warpAffine(old_frame, M, (old_frame.shape[1], old_frame.shape[0]))

    # 更新角点和帧
    corners = cv2.goodFeaturesToTrack(frame_gray, maxCorners=100, qualityLevel=0.3, minDistance=7, blockSize=7)
    corners = np.int0(corners)
    old_frame = frame.copy()
    old_gray = frame_gray.copy()

    # 显示锁定后的场景
    cv2.imshow('SceneLock', result_frame)

    # 如果按下 'Esc' 键则退出循环
    if cv2.waitKey(30) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
