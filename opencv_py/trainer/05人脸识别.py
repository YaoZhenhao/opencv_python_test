# 导入Cv模块
import cv2 as cv


# 检测函数
def face_detect_demo():
    gary = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    face_detect = cv.CascadeClassifier('E:/opencv/opencv/sources/data/haarcascades/haarcascade_frontalface_alt2.xml')
    face = face_detect.detectMultiScale(gary, 1.01, 10, 0)
    for x, y, w, h in face:
        cv.rectangle(img, (x, y), (x + w, y + h), color=(38, 171, 237), thickness=2)
    cv.imshow('result', img)


# 读取图片
img = cv.imread('zm.jpg')
# 检测函数
face_detect_demo()

# 等待
while True:
    if ord('q') == cv.waitKey(8):
        break

# 释放内存
cv.destroyAllWindows()
