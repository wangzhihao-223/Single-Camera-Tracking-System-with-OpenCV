import cv2


# 读取图片
frame = cv2.imread("tmp_data/lab.jpg")

# 双边滤波去噪
bilateral_frame = cv2.bilateralFilter(frame, 9, 75, 75)

# 写入原始帧和去噪后的帧到文件系统
cv2.imwrite("tmp_data/filter_effect/bilat/original_frame.jpg", frame)
cv2.imwrite("tmp_data/filter_effect/bilat/bilateral_frame.jpg", bilateral_frame)

# 显示原始帧和去噪后的帧
cv2.imshow('原图片', frame)
cv2.imshow('双边滤波处理图', bilateral_frame)

cv2.waitKey(0)
cv2.destroyAllWindows()
