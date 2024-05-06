import cv2

def get_camera_resolution():
    # 打开摄像头
    cap = cv2.VideoCapture(0)

    # 检查摄像头是否成功打开
    if not cap.isOpened():
        print("无法打开摄像头")
        return

    # 获取摄像头的分辨率
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    print("摄像头分辨率为: {}x{}".format(width, height))

    # 释放摄像头
    cap.release()

if __name__ == "__main__":
    get_camera_resolution()
