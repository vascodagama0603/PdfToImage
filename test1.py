images = ['C:/Users/yoshitaka/Downloads/PdfToImage/image_file/pdf3009p.tif']
import tesserocr
from PIL import Image

print(tesserocr.tesseract_version())  # print tesseract-ocr version
print(tesserocr.get_languages())  # prints tessdata path and list of available languages

image = Image.open('C:/Users/yoshitaka/Downloads/PdfToImage/image_file/pdf3009p.tif')
print(tesserocr.image_to_text(image))  # print ocr text from image
# or
#print(tesserocr.file_to_text('C:/Users/yoshitaka/Downloads/PdfToImage/image_file/pdf3009p.tif'))
# api is automatically finalized when used in a with-statement (context manager).
# otherwise api.End() should be explicitly called when it's no longer needed.