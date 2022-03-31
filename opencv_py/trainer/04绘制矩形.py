# 导入Cv模块
import cv2 as cv

# 读取图片
img = cv.imread('face1.jpg')
# 坐标
x, y, w, h = 50, 50, 50, 50
# 绘制矩形
cv.rectangle(img, (x, y, x + w, y + h), color=(0, 0, 255), thickness=1)
# 绘制圆形
cv.circle(img, center=(x + w, y + h), radius=50, color=(255, 255, 0), thickness=2)
# 显示
cv.imshow('re_img', img)

# 等待
while True:
    if ord('q') == cv.waitKey(8):
        break

# 释放内存
cv.destroyAllWindows()
