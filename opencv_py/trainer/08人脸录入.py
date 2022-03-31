# 导入Cv模块
import cv2
import cv2 as cv

# 读取摄像头
cap = cv.VideoCapture(0)

flag = 1
num = 1

while (cap.isOpened()):
    ret_flag, Vshow = cap.read()
    cv2.imshow("Capture_Test", Vshow)
    k = cv2.waitKey(1) & 0xff
    if k == ord('s'):
        cv2.imwrite("E:/opencv/opencv_py/photo/" + str(num) + ".yzh" + ".jpg", Vshow)
        print("success to save" + str(num) + ".jpg")
        print("--------------")
        num += 1
    elif k == ord(' '):
        break

# 释放摄像头
cap.release()

# 释放内存
cv.destroyAllWindows()
