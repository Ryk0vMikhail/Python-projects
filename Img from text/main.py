import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"D:\Programming\Tesseract-OCR\tesseract.exe"

image = Image.open("D:\MyPythonProject\Img from text\image.jpg")

text = pytesseract.image_to_string(image, lang="rus")

print(text)
