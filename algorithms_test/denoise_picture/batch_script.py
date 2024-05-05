import cv2

# 读取图像
image = cv2.imread("tmp_data/original/cross2.jpg")
if image is None:
    print("无法加载图像，请检查文件路径。")
else:
    # 均值去噪
    blur_mean = cv2.blur(image, (5, 5))

    # 中值去噪
    blur_median = cv2.medianBlur(image, 5)

    # 高斯去噪
    blur_gaussian = cv2.GaussianBlur(image, (5, 5), 0)

    # 双边去噪
    blur_bilateral = cv2.bilateralFilter(image, 9, 75, 75)

    path = 'tmp_data/filter_effect/cross2'
    cv2.imwrite(path + '/Mean_Blur.png', blur_mean)
    cv2.imwrite(path + '/Median_Blur.png', blur_median)
    cv2.imwrite(path + '/Gaussian_Blur.png', blur_gaussian)
    cv2.imwrite(path + '/Bilateral_Blur.png', blur_bilateral)

    print("所有图片已经处理完毕！")