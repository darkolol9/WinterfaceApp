import OCR
import cv2



inv_bon = cv2.imread('resources/bon.png')


bon =  OCR.apply_ocr(OCR.bitmaps,inv_bon)


print(bon)

input()