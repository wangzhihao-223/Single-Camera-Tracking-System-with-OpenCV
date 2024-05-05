import cv2
import numpy as np
def move_gray_image_processing(image, factor):
    # 将图像数据类型转换为int16
    image_int16 = image.astype(np.int16)
    
    # 应用对比度调整
    adjusted_image_int16 = image_int16 * factor
    
    # 将超出范围的像素值限制在0-255之间
    adjusted_image_int16[adjusted_image_int16 < 0] = 0
    adjusted_image_int16[adjusted_image_int16 > 255] = 255
    
    # 将图像数据类型转换回uint8
    adjusted_image = adjusted_image_int16.astype(np.uint8)
    
    return adjusted_image

# 读取灰度图像
image = cv2.imread('../flower.png', cv2.IMREAD_GRAYSCALE)

# 调整对比度
adjusted_image = move_gray_image_processing(image, factor=1.5)

# 显示调整后的图像
cv2.imshow('Adjusted Image', adjusted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
