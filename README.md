<a href="https://www.codefactor.io/repository/github/rkazula/base64_to_image_decoder"><img src="https://www.codefactor.io/repository/github/rkazula/base64_to_image_decoder/badge" alt="CodeFactor" /></a>

# base64_to_image_decoder
Decoding images from byte array[] base64 to image. 

<b>Before you start:</b>
<p>data = 'PATH_TO_RESPONSE_DATA' >> Put between '' the path to your file with response data. </p>

<b>Cropping the image:</b>
<p>If you need only a part of the image, please add concrete poitns for cropping/
More information:  https://pillow.readthedocs.io/en/3.1.x/reference/Image.html#PIL.Image.Image.crop</p>
<p><i>Example: </i></p>
<p>cropped_im = im.crop((950, 630, 1450, 693))</p>

<b>OCR:</b>
<p>For OCR you have to install and configure Tesseract OCR Engine: https://github.com/tesseract-ocr/tesseract
And in the next step add path to tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r'PATH_TO_PYTESSERACT'</p>

