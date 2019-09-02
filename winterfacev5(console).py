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
import OCR



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

max_detect_allowed = 1319208576.0
threshold = 0.9

tmpl = cv2.imread("resources/newtmp.png")  #get the template ready as cv2
large = cv2.imread("resources/large.png")
leech = cv2.imread("resources/leech.png")
#test run

category = {1:'4s',2:'trio',3:'duo',4:'solo',0:'1:1'}




print('running!\n')
winsound.Beep(2500,600)

while 1:
	large_flag =  False
	TIME.sleep(2)
	leeches = 0
	

	screen = ImageGrab.grab() #screenshot
	screen_np = np.array(screen) #translate it to a format cv2 understands
	#screen_np = cv2.bitwise_not(screen_np) #invert colors before comparing
	screen_np = cv2.cvtColor(screen_np, cv2.COLOR_BGR2RGB)


	cv2.imwrite('resources/scrnshotforcompare.png',screen_np)

	res = cv2.matchTemplate(screen_np,tmpl,cv2.TM_CCORR_NORMED) 
	res2 = cv2.matchTemplate(screen_np,large,cv2.TM_CCORR_NORMED)
	res3 = cv2.matchTemplate(screen_np,leech,cv2.TM_CCORR_NORMED)

	loc = np.where(res3 >= threshold)

	#run the image detection on screenshot
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res) 
	min_val1, max_val1, min_loc1, max_loc1 = cv2.minMaxLoc(res2) #get the location and accuracy val
	
	#print(accur)
	#if max_val > max_detect_allowed:
	#	print("too different! undetected!, difference is ",max_val - max_detect_allowed , '\n')

	if   max_val > 0.8 :
		print('detected winterface!  \n')
		print('with threshold of: ',max_val)
		cv2.imwrite('resources/scrnshotforcompare.png',screen_np)

		for pt in zip(*loc[::-1]):
			leeches = leeches + 1



		if max_val1 >= 0.99:
			large_flag = True
			print('large floor')

		
		#now we need to crop the parts we need and run text detection

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

		floor = pytesseract.image_to_string('resources/flr.png')
		bon =  OCR.apply_ocr(bitmaps,inv_bon)
		time = OCR.apply_ocr(bitmaps,inv_time)
		mod = OCR.apply_ocr(bitmaps,inv_mod)
		print(floor)

		#bon[0] = '+'
		winterface = [floor,bon,time,mod]
		#print(winterface)
		


		
		
		#formatted_time = timeformt[0] +timeformt[1] + ":" + timeformt[2]+timeformt[3] + ":" +timeformt[4]+timeformt[5] 	
		if bon :
			line =  '[' + winterface[0] + '] ' + '[' +  winterface[1]+ '] ' + '[' + winterface[2] + '] ' +'[' + winterface[3]+ ']'
		blank_line = True

		if "Floor" in floor:
			blank_line = False
			print('successfully captured a floor winterface!')
			print(winterface)

		if blank_line == False:
			winsound.Beep(2500,1500)
			log = open("log.txt",'a+')

			if large_flag:
				line += '\t LARGE ' + category[leeches] + '\n'
			else :
				line += '\t MED/SMALL ' + category[leeches] + '\n'	

			log.write(line)

			log.close()
			blank_line = True
			TIME.sleep(10)


		
	

