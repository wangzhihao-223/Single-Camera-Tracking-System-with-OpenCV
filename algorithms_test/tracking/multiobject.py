#! /usr/bin/python3
import cv2

cap = cv2.VideoCapture(0)
tracker = cv2.TrackerMedianFlow_create()

# 选择初始目标区域
ret, frame = cap.read()
roi = cv2.selectROI('Select Object', frame)
tracker.init(frame, roi)

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    success, roi = tracker.update(frame)

    if success:
        (x, y, w, h) = tuple(map(int, roi))
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('MTT Tracking', frame)

    if cv2.waitKey(30) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
