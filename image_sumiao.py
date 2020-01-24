# 导入cv2模块
import cv2
# 输入图片路径
SRC = input("Please input image's path:")
img_rgb = cv2.imread(SRC)

# 读取原图
# cv2.imshow('rbg', img_rgb)
# cv2.waitKey(0)
# exit()

img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
# 展示灰度图
# cv2.imshow("gray", img_gray)
# cv2.waitKey(0)
# exit()

img_blur = cv2.GaussianBlur(img_gray, ksize=(21, 21), sigmaX=0, sigmaY=0)
# 展示高斯虚化后效果图
# cv2.imshow("img_blur", img_blur)
# cv2.waitKey(0)
# exit()

img_blend = cv2.divide(img_gray, img_blur, scale=255)
# 展示素描图
cv2.imshow("img_blend", img_blend)
cv2.waitKey(0)
cv2.imwrite("image_sumiao.jpg", img_blend)
