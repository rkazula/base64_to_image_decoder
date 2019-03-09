from PIL import Image
from io import BytesIO
import base64

data: str = "YOUR_BASE64_IMAGE_HERE"


im = Image.open(BytesIO(base64.b64decode(data)))
cropped_im = im.crop((VALUE1, VALUE2, VALUE3, VALUE4))
cropped_im.save('nazwa.jpg')
im.close()


