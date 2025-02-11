import cv2 as cv
img = cv.imread('photos/accountScreenshot.png')
cv.imshow('accountScreenshot', img)

# Reading videos
capture = cv.VideoCapture('videos/lewis.mp4') #reference webcam using int 0


cv.waitKey(0)