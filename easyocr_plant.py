import cv2
import easyocr
import numpy as np
import argparse

coordinates = ''
text = ''
confi = ''

parser = argparse.ArgumentParser(description='Take image path for ocr')
parser.add_argument('path', metavar='N',
                    help='path of the image')

args = parser.parse_args()

#img = cv2.imread("/home/divya/Downloads/IMG_0464.JPG") #Grade -1 
#img = cv2.imread("/home/divya/Downloads/chilli/train/IMG_0372.JPG") #Grade- 4
#img = cv2.imread("/home/divya/Downloads/chilli/train/IMG_0431.JPG") #Grade- 3
#img = cv2.imread("/home/divya/Downloads/chilli/train/IMG_0344.JPG") #Grade- 2

img = cv2.imread(args.path)
#cv2.imshow("img", img)

flag = 0
#rotating an image so that the label is clear
if flag==0:
  img90 = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)
  #cv2.imshow("90", img90)

#to sharpen the blurness
  sharpen_kernel90 = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
  sharpen90 = cv2.filter2D(img90, -1, sharpen_kernel90)
  reader90 = easyocr.Reader(['en'])
  result90 = reader90.readtext(sharpen90)

#access the elements of an array in a list
  for i in result90:
      coordinates = i[0]
      text = i[1]
      confi = i[2]
      
  if text[:2] == 'GR':
    flag = 0
    print("90 it is")
  else:
    flag = 1
 
elif flag==1:
  img180 = cv2.rotate(img, cv2.cv2.ROTATE_180)
  #cv2.imshow("180",img180)
  sharpen_kernel180 = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
  sharpen180 = cv2.filter2D(img180, -1, sharpen_kernel180)
  reader180 = easyocr.Reader(['en'])
  result180 = reader180.readtext(sharpen180)

#access the elements of an array in a list
  for i in result180:
      coordinates = i[0]
      text = i[1]
      confi = i[2]
  
  if text[:2] == 'GR':
    print("180 it is")
  else:
    print("Sorry - this image is too tough for me")
    

print("coordinates : {}, text : {}, confi : {}".format(coordinates, text, confi))
#print(result)
