import cv2
import easyocr
import numpy as np

#img = cv2.imread("/home/divya/Downloads/IMG_0464.JPG") #Grade -1 
#img = cv2.imread("/home/divya/Downloads/chilli/train/IMG_0372.JPG") #Grade- 4
#img = cv2.imread("/home/divya/Downloads/chilli/train/IMG_0431.JPG") #Grade- 3
img = cv2.imread("/home/divya/Downloads/chilli/train/IMG_0344.JPG") #Grade- 2

img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)
#img = cv2.rotate(img, cv2.cv2.ROTATE_180)
sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
sharpen = cv2.filter2D(img, -1, sharpen_kernel)
reader = easyocr.Reader(['en'])
result = reader.readtext(sharpen)
#print("balhhh ",type(result))
for i in result:
    print("blahh",i[0])
#print("demo",len(result))
print(result)