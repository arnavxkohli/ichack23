from PIL import Image
import pytesseract
import cv2
import re
import numpy as np
import os
import matplotlib.pyplot as plt

# pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'

IMAGE_PATH = os.getcwd() + "/img/exp_date.jpg"

img = cv2.imread(IMAGE_PATH)

# Convert to graycsale
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blur the image for better edge detection
img = cv2.GaussianBlur(img, (3,3), cv2.BORDER_DEFAULT)

img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

kernel = np.ones((1,1),np.uint8)
img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

img = cv2.Canny(img, 100, 200)

text = pytesseract.image_to_string(img)


#Define configuration that only whitelists number characters
custom_config = r'--oem 3 --psm 11 -c tessedit_char_whitelist=0123456789/-'

#Find the numbers in the image
numbers_string = pytesseract.image_to_string(img, config=custom_config)

#Remove all non-number characters
numbers_int = re.sub(r'[a-z\n]', '', numbers_string.lower())

print(numbers_int)

plt.imshow(img,cmap='gray')
plt.show()