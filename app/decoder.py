import base64
import os
import re
import sys
from io import BytesIO

import pytesseract
from PIL import Image

data = 'PATH_TO_RESPONSE_DATA'  # Add path to base64 file
pytesseract.pytesseract.tesseract_cmd = r'PATH_TO_PYTESSERACT'  # Add path to tesseract.exe

if os.path.isfile(data):
    print('File exists: ' + str(os.path.isfile(data)))
else:
    print('File not found!')
    sys.exit()

try:
    response = open(data, 'r')
    response_text = response.read()
except IOError as e:
    print('I/O error({0}): {1}'.format(e.errno, e.strerror))
    print('File cannot be opened.')
    sys.exit()

# Regex for identifying Base64
b64Marker = '(^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$)'
b64check = re.search(b64Marker, response_text)
if b64check:
    print('Base64 found!')
else:
    print('File error - not base64.')
    sys.exit(1)

im = Image.open(BytesIO(base64.b64decode(response_text)))

# Add points for cropping the image. More information:
# https://pillow.readthedocs.io/en/3.1.x/reference/Image.html#PIL.Image.Image.crop
cropped_im = im.crop((VALUE1, VALUE2, VALUE3, VALUE4))
cropped_im.save('output_file.jpg')
print('Result: ' + pytesseract.image_to_string('output_file.jpg'))
im.close()
