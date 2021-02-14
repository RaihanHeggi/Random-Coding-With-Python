import cv2

# thanks to AnbiDev for this tutorial

# preparing data read and make it grayscale picture
img = cv2.imread("example_pic.jpg", 1)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("example_pic_gray.png", img_gray)


# inverting image
img_invert = cv2.bitwise_not(img_gray)
cv2.imwrite("example_pic_invert.png", img_invert)

# smoothing image
img_smoothing = cv2.GaussianBlur(img_invert, (21, 21), sigmaX=0, sigmaY=0)
cv2.imwrite("example_pic_smoothing.png", img_smoothing)

# finalizing
img_final = cv2.divide(img_gray, 255 - img_smoothing, scale=256)
cv2.imwrite("example_pic_final.png", img_final)

