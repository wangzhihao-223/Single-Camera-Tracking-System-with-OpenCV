import cv2

def display_video():
    # 打开视频文件
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("无法打开视频文件")
        return

    while cap.isOpened():
        # 逐帧读取视频
        ret, frame = cap.read()
        cv2.imshow('Video', frame)
        # 按下空格键时进行截图
        key = cv2.waitKey(25)
        if key & 0xFF == ord('q'):
            break
        elif key & 0xFF == ord(' '):
            # 保存截图
            cv2.imwrite('tmp_data/screenshots/shot1.jpg', frame)
            print("截图已保存为 screenshot.jpg")

    # 释放资源
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    display_video()
