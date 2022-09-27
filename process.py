import cv2 

imgpath = "./img/spaghetti-1932466_1280.jpg"

# read and display image
img = cv2.imread(imgpath,flags=4) # 4 means IMREAD_ANYCOLOR
cv2.imshow("Original image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()