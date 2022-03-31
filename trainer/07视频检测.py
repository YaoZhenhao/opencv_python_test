# 导入Cv模块
import cv2 as cv


# 检测函数
def face_detect_demo(img):
    gary = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    face_detect = cv.CascadeClassifier('E:/opencv/opencv/sources/data/haarcascades/haarcascade_frontalface_alt2.xml')
    face = face_detect.detectMultiScale(gary)
    for x, y, w, h in face:
        cv.rectangle(img, (x, y), (x + w, y + h), color=(0, 1, 255), thickness=2)
    cv.imshow('result', img)


# 读取摄像头
# cap = cv.VideoCapture(0)
cap = cv.VideoCapture('lb.mp4')


while True:
    flag, frame = cap.read()
    if not flag:
        break
    face_detect_demo(frame)
    if ord('q') == cv.waitKey(8):
        break


# 释放内存
cv.destroyAllWindows()
# 释放摄像头
cap.release()
