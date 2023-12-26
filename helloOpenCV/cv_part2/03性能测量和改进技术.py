import cv2 as cv

# 使用 OpenCV 测量性能
# cv.getTickCount函数返回参考事件（如机器开启时刻）到调用此函数的时钟周期数。
#     因此，如果在函数执行之前和之后调用它，则会获得用于执行函数的时钟周期数。
# cv.getTickFrequency函数返回时钟周期的频率，或每秒钟的时钟周期数。
img1 = cv.imread("./res/cat.png")
e1 = cv.getTickCount()
for i in range(1, 49, 4):
    img1 = cv.medianBlur(img1, i)
    cv.putText(img1, i.__str__(), (50, 50), cv.FONT_HERSHEY_TRIPLEX, fontScale=1, color=(255, 0, 0))
    cv.imshow("img", img1)
    cv.waitKey(0)
e2 = cv.getTickCount()
t = (e2 - e1) / cv.getTickFrequency()
print(t)
