from PIL import Image
import pytesseract

image = Image.open("./test_samples/test_2.jpg")
gray_image = image.convert("L")

text = pytesseract.image_to_string(gray_image)
clean_text = text.replace("\x0c", "").strip()
print(clean_text)