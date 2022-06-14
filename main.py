import cv2 as cv
import numpy as np
filepath = 'Banana.jpg'
windowTitle = "This is a banana"
cvflag = 1
img = cv.imread(filepath,cvflag)
inpitem = int(input("input x coordiante: "))
inpitem2 = int(input("input y coordinate: "))
inpitem3 = int(input("input color channel (1 - green, 2 - red, 3 - blue): "))
if inpitem3 == 3:
    inpitem3 = 0
print(img.item(inpitem,inpitem2,inpitem3))
inpred = int(input("\nchange pixel color for red channel(0-255): "))
inpgreen = int(input("change pixel color for green channel(0-255): "))
inpblue = int(input("change pixel color for blue channel(0-255): "))
print("Before: ", img[inpitem,inpitem2])
img.itemset((inpitem,inpitem2,2),inpred)
img.itemset((inpitem,inpitem2,1),inpgreen)
img.itemset((inpitem,inpitem2,0),inpblue)
print("After: ", img[inpitem,inpitem2])
cmpshape = img.shape
cmpshape1 = (700,700,3)
if cmpshape1[0] <= cmpshape[0] and cmpshape1[1] <= cmpshape[1]:
    print("\nnot out of bounds...")
else:
    print("\nout of bounds")
cmpsize = img.size
cmpsize1 = 123456
if cmpsize > cmpsize1:
    print("set pixel count is lower than loaded image...\n")
else:
    print("set pixel count is higher than loaded image...\n")
print(img.shape)
print(img.size)
print(img.dtype)
cv.imshow(windowTitle,img)
cv.waitKey(0)
cv.destroyAllWindows()