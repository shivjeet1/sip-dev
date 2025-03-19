import pytesseract
from preprocess import preprocess_image
from PIL import Image
import numpy as np

def extract_text(image_path, lang='eng'):
    processed_image = preprocess_image(image_path)
    
    if isinstance(processed_image, np.ndarray):
        pil_image = Image.fromarray(processed_image)
    else:
        pil_image = processed_image
    
    text = pytesseract.image_to_string(pil_image, lang=lang)
    return text
