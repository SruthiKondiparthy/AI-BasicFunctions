try:
    from PIL import Image
except ImportError:
    from PIL import Image

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Sivak\AppData\Local\Tesseract-OCR\tesseract.exe'

def recText(filename):
    text = pytesseract.image_to_string(Image.open(filename))
    return text

info = recText('healthtips.png')
print(info)
file = open("health.txt","w")
file.write(info)
file.close()
print("Written Successful")
