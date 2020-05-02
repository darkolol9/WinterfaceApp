import cv2


img1 = cv2.imread("red.png",0)
img2 = cv2.imread("blue.png",0)


res = cv2.matchTemplate(img1,img2,cv2.TM_CCORR_NORMED) 