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

flag = 0
img90 = cv2.rotate(sharpen, cv2.ROTATE_90_CLOCKWISE)
img180 = cv2.rotate(sharpen, cv2.ROTATE_180)

if flag==0:
  reader = easyocr.Reader(['en'])
  result90 = reader.readtext(img90)
  
   for i in result90:
      coordinates = i[0]
      text = i[1]
      confi = i[2]
      
   if text[:2] == "GR":
      print("90 it is")
   else:
      flag = 1

     
elif flag ==1:
   reader = easrocr.Reader(["en"])
   result180 = reader.readtext(img180)

  for i in result180:
      coordinates = i[0]
      text = i[1]
      confi = i[2]
  
  if text[:2] == 'GR':
    print("180 it is")
  else:
    print("Sorry - this image is too tough for me")
    
print("coordinates : {}, text : {}, confi : {}".format(coordinates, text, confi))
