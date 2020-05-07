import os
from pathlib import Path
from pdf2image import convert_from_path

# poppler/binを環境変数PATHに追加する
poppler_dir = Path(sys.argv[0]).parent.absolute() / "poppler/bin"
print("dir:",poppler_dir )
os.environ["PATH"] += os.pathsep + str(poppler_dir)
# PDFファイルのパス

pdf_path = Path(sys.argv[0]).parent.absolute() / "pdf_file/pdf3009p.pdf"
print("pdf:pasf:",pdf_path)
# PDF -> Image に変換（150dpi）
pages = convert_from_path(str(pdf_path), 300)

# 画像ファイルを１ページずつ保存
image_dir = Path(sys.argv[0]).parent.absolute() / "image_file"
tiff_name = pdf_path.stem + ".tif"
image_path = image_dir / tiff_name
print(image_path)
pages[0].save(str(image_path), "TIFF", compression="tiff_deflate", save_all=True, append_images=pages[1:])