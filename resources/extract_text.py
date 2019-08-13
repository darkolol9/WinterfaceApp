try:
    from PIL import ImageGrab
except ImportError:
    import Image
import pytesseract
import cv2

img = cv2.imread('time.png')
print(pytesseract.image_to_string(img))
input()