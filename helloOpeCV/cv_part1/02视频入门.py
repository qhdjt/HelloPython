import numpy as np
import cv2 as cv
# 从相机捕捉视频
# 通常，我们用相机捕捉直播。OpenCV 为此提供了一个非常简单的接口。
# 我们用相机捕捉一个视频(我用的电脑内置摄像头)，将它转换成灰度视频并显示。仅仅是一个简单的开始。
# 去获取一个视频，你需要创建一个VideoCapture对象。它的参数可以是设备索引或者一个视频文件名。
# 设备索引仅仅是摄像机编号。通常会连接一台摄像机(as in my case)。所以我只传了 0(或者-1)。
# 你可以通过传 1 来选择第二个摄像机，以此类推。之后，你能逐帧捕获。但是最后，不要忘记释放这个 Capture 对象。
# cap = cv.VideoCapture(0)
# print(cap)
# while(True):
#     # 一帧一帧捕捉
#     ret, frame = cap.read()
#     # 我们对帧的操作在这里
#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     # 显示返回的每帧
#     cv.imshow('frame',gray)
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break
# # 当所有事完成，释放 VideoCapture 对象
# cap.release()
# cv.destroyAllWindows()

# 播放视频文件
# 它和从相机捕获一样，只需要用视频文件名更改相机索引。
# 同时显示 frame，为 cv.waitKey() 使用合适的时间。如果它太小，视频将非常快，如果太大，视频将很慢 (嗯，这就是如何显示慢动作)。
# 正常情况下，25 毫秒就可以了。

cap = cv.VideoCapture('../res/video.mp4')
while cap.isOpened():
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame',gray)
    if cv.waitKey(30) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()