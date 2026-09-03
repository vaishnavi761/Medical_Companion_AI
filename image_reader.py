import easyocr

import numpy as np

from PIL import Image

reader = easyocr.Reader(["en"], gpu=False)

def extract_text_from_image(file):

    image = Image.open(file)

    image = np.array(image)

    result = reader.readtext(image)

    text = ""

    for _, detected_text, _ in result:
        text += detected_text + " "

    return text