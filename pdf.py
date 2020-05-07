# ocr_card.py
import os
from PIL import Image
import pyocr
import pyocr.builders
from pathlib import Path
import pdb

# 1.インストール済みのTesseractのパスを通す
path_tesseract = Path(sys.argv[0]).parent.absolute() / "Tesseract-OCR"
str_path = str(path_tesseract)
print(path_tesseract)
#pdb.set_trace()

if str_path not in os.environ["PATH"].split(os.pathsep):
    os.environ["PATH"] += os.pathsep + str_path

# 2.OCRエンジンの取得
tools = pyocr.get_available_tools()
tool = tools[0]

# 3.原稿画像の読み込み
img_org = Image.open( Path(sys.argv[0]).parent.absolute() / "image_file/pdf3009p.tif")

# 4.ＯＣＲ実行
builder = pyocr.builders.TextBuilder()

result = tool.image_to_string(img_org, lang="jpn", builder=builder)

print(result)
