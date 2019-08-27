import tkinter as tk
try:
    from PIL import ImageGrab
except ImportError:
    import Image
import pytesseract
import time as TIME
from matplotlib import pyplot as plt
import cv2
import numpy as np
import winsound
import easygui
import datetime
from openpyxl import Workbook
from openpyxl import load_workbook
import OCR

#bitmaps

zero = [cv2.imread("resources/bitmaps/0.bmp"),'0',0]
nine = [cv2.imread("resources/bitmaps/9.bmp"),'9',0]
seven = [cv2.imread("resources/bitmaps/7.bmp"),'7',0]
plus = [cv2.imread("resources/bitmaps/+.bmp"),'+',0]
six = [cv2.imread("resources/bitmaps/6.bmp"),'6',0]
two = [cv2.imread("resources/bitmaps/2.bmp"),'2',0]
eight = [cv2.imread("resources/bitmaps/8.bmp"),'8',0]
three = [cv2.imread("resources/bitmaps/3.bmp"),'3',0]
four = [cv2.imread("resources/bitmaps/4.bmp"),'4',0]
minus = [cv2.imread("resources/bitmaps/-.bmp"),'-',0]
precent = [cv2.imread("resources/bitmaps/%.bmp"),'%',0]
one = [cv2.imread("resources/bitmaps/1.bmp"),'1',0]
colon = [cv2.imread("resources/bitmaps/colon.bmp"),':',0]
five = [cv2.imread("resources/bitmaps/5.bmp"),'5',0]

bitmaps = [zero,one,colon,five,minus,precent,two,three,four,six,seven,eight,nine,plus]

print('running tool...')

tmpl = cv2.imread("resources/newtmp.png")  #get the template ready as cv2
max_detect_allowed = 1409208576.0

def CAPTURE():
	print('attempting to capture!')
	winsound.Beep(2500,200)
	screen = ImageGrab.grab() #screenshot
	screen_np = np.array(screen) #translate it to a format cv2 understands
	screen_np = cv2.cvtColor(screen_np, cv2.COLOR_BGR2RGB)

	res = cv2.matchTemplate(screen_np,tmpl,cv2.TM_CCORR)
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

	if max_val < max_detect_allowed:

		floor_num = ImageGrab.grab(bbox=(max_loc[0]+41,max_loc[1]+56,max_loc[0]+94,max_loc[1]+78))
		bon_num = ImageGrab.grab(bbox=(max_loc[0]+297,max_loc[1]+136,max_loc[0]+332,max_loc[1]+164))
		time_num = ImageGrab.grab(bbox=(max_loc[0]+34,max_loc[1]+300,max_loc[0]+82,max_loc[1]+321))
		mod_num = ImageGrab.grab(bbox=(max_loc[0]+297,max_loc[1]+157,max_loc[0]+331,max_loc[1]+182))

		image_np = np.array(floor_num)
		image_np2 = np.array(bon_num)
		image_np3 = np.array(time_num)
		image_np4 = np.array(mod_num)

		inv_flr = cv2.bitwise_not(image_np)
		inv_bon = cv2.bitwise_not(image_np2)
		inv_time = cv2.bitwise_not(image_np3)
		inv_mod = cv2.bitwise_not(image_np4)

		cv2.imwrite('resources/flr.png',inv_flr)
		cv2.imwrite('resources/bon.png',inv_bon)
		cv2.imwrite('resources/time.png',inv_time)
		cv2.imwrite('resources/mod.png',inv_mod)

		bon_ocr = cv2.imread('resources/bon.png')
		time_ocr = cv2.imread('resources/time.png')
		mod_ocr = cv2.imread('resources/mod.png')

		floor = pytesseract.image_to_string('resources/flr.png')
		bon =  OCR.apply_ocr(bitmaps,bon_ocr)
		print(bon)
		time = OCR.apply_ocr(bitmaps,time_ocr)
		mod = OCR.apply_ocr(bitmaps,mod_ocr)
		#print(floor)
		
		winterface = [floor,bon,time,mod]

		line = winterface[0] + '\t bon: ' + winterface[1]+ '\t time: ' + winterface[2] + '\t mod: ' + winterface[3]+'\n'
		xl_line = (floor,bon,time,mod)
		datecm = str(datetime.datetime.now())
		blank_line = True

		if "Floor" in floor:
			blank_line = False
			print('successfully captured a floor winterface!')
			print(winterface)

		if blank_line == False:

			log = open('resources/OCR_LOG.txt','a+')
			log.write(line)



			winsound.Beep(2500,1500)
			#log = open("LOGGED FLOORS.xlsx",'a+')
			easygui.msgbox("logged the floor!!", title="winterface logger")
			#log.write(line +'\t' + datecm + '\n')
			#log.close()
			blank_line = True
			TIME.sleep(10)



win = tk.Tk()
win.title('winterface capture!')
but = tk.Button(win,text= "Capture",command = CAPTURE)
but.pack()

win.mainloop()