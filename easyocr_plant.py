import cv2
import easyocr
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Take image path for ocr')
parser.add_argument('path', metavar='N',
                    help='path of the image')

args = parser.parse_args()

#img = cv2.imread("/home/divya/Downloads/IMG_0464.JPG") #Grade -1 
#img = cv2.imread("/home/divya/Downloads/chilli/train/IMG_0372.JPG") #Grade- 4
#img = cv2.imread("/home/divya/Downloads/chilli/train/IMG_0431.JPG") #Grade- 3
#img = cv2.imread("/home/divya/Downloads/chilli/train/IMG_0344.JPG") #Grade- 2

img = cv2.imread(args.path)
#rotating an image so that the label is clear
img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)
#img = cv2.rotate(img, cv2.cv2.ROTATE_180)

#to sharpen the blurness
sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
sharpen = cv2.filter2D(img, -1, sharpen_kernel)
reader = easyocr.Reader(['en'])
result = reader.readtext(sharpen)
print("balhhh ",type(result))

#access the elements of an array in a list
for i in result:
    print("blahh",i[0])
#print("length ",len(result))
print(result)
