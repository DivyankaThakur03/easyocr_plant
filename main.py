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

img = cv2.imread(args.path)
sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
sharpen = cv2.filter2D(img, -1, sharpen_kernel)

flag = True
img90 = cv2.rotate(sharpen, cv2.ROTATE_90_CLOCKWISE)
img180 = cv2.rotate(sharpen, cv2.ROTATE_180)
reader = easyocr.Reader(['en'])

if flag== True:
    result90 = reader.readtext(img90)
  
    for i in result90:
      coordinates = i[0]
      text = i[1]
      confi = i[2]
      
    if text[:2] == "GR":
      print("90 it is")
    else:
      flag == False
      print("Now the flag is initiated to 1 so it is img180")

elif flag == False:
    
    if result180 == reader.readtext(img180):
      print("img180 is read")
    else:
      print("something is messed")
      
    for i in result180:
      coordinates = i[0]
      text = i[1]
      confi = i[2]
  
    if text[:2] == 'GR':
        print("180 it is")
    else:
        print("Sorry - this image is too tough for me")
    
print("coordinates : {}, text : {}, confi : {}".format(coordinates, text, confi))
