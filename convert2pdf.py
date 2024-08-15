from PIL import Image
import pytesseract

# Specify the path to the Tesseract executable (if it's not in your PATH)
# Example for Windows (uncomment if needed):
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load the image
img_path = "claim1.png"
image = Image.open(img_path)

# Extract text from the image
extracted_text = pytesseract.image_to_string(image)

# Output the extracted text
print("Extracted Text:")
print(extracted_text)
