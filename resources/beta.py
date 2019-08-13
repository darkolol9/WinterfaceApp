try:
    from PIL import ImageGrab
except ImportError:
    import Image
import pytesseract
import time as TIME
from matplotlib import pyplot as plt
import cv2
import numpy as np

max_detect_allowed = 1709208576.0

tmpl = cv2.imread('newtmp.png')  #get the template ready as cv2
#test run




print('running!\n')

while 1:
	TIME.sleep(1)

	screen = ImageGrab.grab() #screenshot
	screen_np = np.array(screen) #translate it to a format cv2 understands
	#screen_np = cv2.bitwise_not(screen_np) #invert colors before comparing
	screen_np = cv2.cvtColor(screen_np, cv2.COLOR_BGR2RGB)


	cv2.imwrite('scrnshotforcompare.png',screen_np)

	res = cv2.matchTemplate(screen_np,tmpl,cv2.TM_CCORR) #run the image detection on screenshot
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)  #get the location and accuracy val
	if max_val > max_detect_allowed:
		print("too different! undetected!, difference is ",max_val - max_detect_allowed , '\n')

	if max_val < max_detect_allowed:
		print('detected winterface!  \n')
		#now we need to crop the parts we need and run text detection

		floor_num = ImageGrab.grab(bbox=(max_loc[0]+41,max_loc[1]+56,max_loc[0]+94,max_loc[1]+78))
		bon_num = ImageGrab.grab(bbox=(max_loc[0]+297,max_loc[1]+157,max_loc[0]+332,max_loc[1]+182))
		time_num = ImageGrab.grab(bbox=(max_loc[0]+34,max_loc[1]+300,max_loc[0]+82,max_loc[1]+321))
		mod_num = ImageGrab.grab(bbox=(max_loc[0]+297,max_loc[1]+178,max_loc[0]+329,max_loc[1]+200))

		image_np = np.array(floor_num)
		image_np2 = np.array(bon_num)
		image_np3 = np.array(time_num)
		image_np4 = np.array(mod_num)

		inv_flr = cv2.bitwise_not(image_np)
		inv_bon = cv2.bitwise_not(image_np2)
		inv_time = cv2.bitwise_not(image_np3)
		inv_mod = cv2.bitwise_not(image_np4)



		cv2.imwrite('flr.png',inv_flr)
		cv2.imwrite('bon.png',inv_bon)
		cv2.imwrite('time.png',inv_time)
		cv2.imwrite('mod.png',inv_mod)

		floor = pytesseract.image_to_string('flr.png')
		bon = pytesseract.image_to_string('bon.png')
		time = pytesseract.image_to_string('time.png')
		mod = pytesseract.image_to_string('mod.png')
		print(floor)


		winterface = [floor,bon,time,mod]
		#print(winterface)
		line = winterface[0] + ' ' + winterface[1]+ ' ' + winterface[2] + ' ' + winterface[3]+'\n'
		blank_line = True

		if len(line) > 0:
			blank_line = False
			print('successfully captured a floor winterface!')
			print(winterface)

		if blank_line == False:
			log = open("log.txt",'a+')
			log.write(line)
			log.close()
			blank_line = True


		
	

