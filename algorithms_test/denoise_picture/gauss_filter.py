import cv2


# 读取图片
frame = cv2.imread("tmp_data/lab.jpg")

# 高斯滤波去噪
blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)

# 写入原始帧和去噪后的帧到文件系统
cv2.imwrite("tmp_data/filter_effect/gauss/original.jpg", frame)
cv2.imwrite("tmp_data/filter_effect/gauss/gaussian_blurred.jpg", blurred_frame)

# 显示原始帧和去噪后的帧
cv2.imshow('原图片', frame)
cv2.imshow('高斯滤波处理图', blurred_frame)

cv2.waitKey(0)
cv2.destroyAllWindows()
