import base64
import os
import re
import sys
from io import BytesIO

import pytesseract
from PIL import Image

data = 'PATH_TO_BASE64_FILE'

if os.path.isfile(data):
    print('File exists: ' + str(os.path.isfile(data)))
else:
    print('File not found!')
    sys.exit()

try:
    response = open(data, 'r')
    text = response.read()
    response.close()
except IOError as e:
    print('I/O error({0}): {1}'.format(e.errno, e.strerror))
    print('File cannot be opened.')
    sys.exit()

# Regex for identifying Base64
b64Marker = '(^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$)'
b64check = re.search(b64Marker, text)
if b64check:
    print('Base64 found!')
else:
    print('File error - not base64.')


im = Image.open(BytesIO(base64.b64decode(data)))
cropped_im = im.crop((VALUE1, VALUE2, VALUE3, VALUE4))
cropped_im.save('output_file.jpg')
pytesseract.pytesseract.tesseract_cmd = r'PATH_TO_TESSERACT_OCR'
print('Result: ' + pytesseract.image_to_string('output_file.jpg'))
im.close()