import numpy as np
import pyautogui
import imutils
import cv2

image = pyautogui.screenshot()
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
cv2.imwrite("read.png", image)


pyautogui.screenshot("read.png")

#load our screenshot from disk in OpenCV format
image = cv2.imread("read.png")
cv2.imshow("SAKSHI PANDITA", imutils.resize(image, width=1500))
status = cv2.imwrite('C:\\Users\\Sakshi\\Desktop\\labl_pics\\'+'.png',image)

cv2.waitKey(0)
