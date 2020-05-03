import cv2
import numpy as np
from matplotlib import pyplot as plt


zero = [cv2.imread("resources/bitmaps/0.bmp",0),'0',0]
nine = [cv2.imread("resources/bitmaps/9.bmp",0),'9',0]
seven = [cv2.imread("resources/bitmaps/7.bmp",0),'7',0]
plus = [cv2.imread("resources/bitmaps/+.bmp",0),'+',0]
six = [cv2.imread("resources/bitmaps/6.bmp",0),'6',0]
two = [cv2.imread("resources/bitmaps/2.bmp",0),'2',0]
eight = [cv2.imread("resources/bitmaps/8.bmp",0),'8',0]
three = [cv2.imread("resources/bitmaps/3.bmp",0),'3',0]
four = [cv2.imread("resources/bitmaps/4.bmp",0),'4',0]
minus = [cv2.imread("resources/bitmaps/-.bmp",0),'-',0]
precent = [cv2.imread("resources/bitmaps/%.bmp",0),'%',0]
one = [cv2.imread("resources/bitmaps/1.bmp",0),'1',0]
colon = [cv2.imread("resources/bitmaps/colon.bmp",0),':',0]
five = [cv2.imread("resources/bitmaps/5.bmp",0),'5',0]
floor = [cv2.imread("resources/bitmaps/floor.png",0),'Floor - ',0]
b0 = [cv2.imread("resources/bitmaps/0_.png",0),'0',0]
b1 = [cv2.imread("resources/bitmaps/1_.png",0),'1',0]
b2 = [cv2.imread("resources/bitmaps/2_.png",0),'2',0]
b3 = [cv2.imread("resources/bitmaps/3_.png",0),'3',0]
b4 = [cv2.imread("resources/bitmaps/4_.png",0),'4',0]
b5 = [cv2.imread("resources/bitmaps/5_.png",0),'5',0]
b6 = [cv2.imread("resources/bitmaps/6_.png",0),'6',0]
b7 = [cv2.imread("resources/bitmaps/7_.png",0),'7',0]
b8 = [cv2.imread("resources/bitmaps/8_.png",0),'8',0]
b9 = [cv2.imread("resources/bitmaps/9_.png",0),'9',0]

bitmaps = [zero,one,floor,b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,colon,five,minus,precent,two,three,four,six,seven,eight,nine,plus]



def detect_bitmaps(bitmap,image,found_bits):
	w, h = bitmap[0].shape[::-1]

	res = cv2.matchTemplate(image,bitmap[0],cv2.TM_CCOEFF_NORMED)
	threshold = 0.9
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
	string = ''
	found_bits = []
	for bitmap in bitmaps:
		detect_bitmaps(bitmap,image,found_bits)
	sort_bitmaps(found_bits)
	'''and now to make a string out of the list of bitmaps [2] being the char index'''
	string_list = []

	for bit in found_bits:
		string_list.append(bit[0])

	string = ""
	string = string.join(string_list)
	striped = string.strip()

	if len(found_bits) > 0:
		return striped
	else:
		return "NOT FOUND"





#test_img = cv2.imread("resources/time.png")


#string = apply_ocr(bitmaps,test_img)
#print(string)
#input('click any key to continue')








	
	
#input('yes?')



