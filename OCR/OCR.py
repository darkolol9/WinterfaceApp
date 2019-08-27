import cv2
import numpy as np
from matplotlib import pyplot as plt


def detect_bitmaps(bitmap,image,found_bits):
	w, h, _ = bitmap[0].shape[::-1]

	res = cv2.matchTemplate(image,bitmap[0],cv2.TM_CCOEFF_NORMED)
	threshold = 0.7
	loc = np.where( res >= threshold)
	for pt in zip(*loc[::-1]):
	    #cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
	    #rint(bitmap[1],pt[0])
	    bitmap[2] = pt[0]
	    found_bit = [bitmap[1],bitmap[2]]
	    found_bits.append(found_bit)
	    #print(pt[0])
	#cv2.imwrite('res.png',image)

def sort_bitmaps(found_bits):
	found_bits.sort(key = lambda x: x[1])

def apply_ocr(bitmaps,image):
	found_bits = []
	for bitmap in bitmaps:
		detect_bitmaps(bitmap,test_img,found_bits)
	sort_bitmaps(found_bits)
	'''and now to make a string out of the list of bitmaps [2] being the char index'''
	string_list = []
	for bit in found_bits:
		string_list.append(bit[0])
		string = ''.join(string_list)
	return string

zero = [cv2.imread("resources/bitmaps/0.bmp"),'0',0]
one = [cv2.imread("resources/bitmaps/1.bmp"),'1',0]
colon = [cv2.imread("resources/bitmaps/colon.bmp"),':',0]
five = [cv2.imread("resources/bitmaps/5.bmp"),'5',0]

bitmaps = [zero,one,colon,five]

test_img = cv2.imread("resources/time.png")


string = apply_ocr(bitmaps,test_img)
print(string)
input('click any key to continue')








	
	
input('yes?')



