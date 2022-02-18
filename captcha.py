try:
        from PIL import Image
except ImportError:
        import Image
import os
import pathlib
import pytesseract

#ABCDEFGHIJKMNLOPKRSTUVWXYZ1

def resolve(img):
    os.system(f"convert /home/gatete/Workspace/MM-S/auto-captcha/imagenes/captcha/{img} -morphology Erode Disk:2 captcha5.tif")
    os.system("convert captcha5.tif -morphology Dilate Disk:1.5 captcha5.tif")
    os.system("convert captcha5.tif -threshold 41% captcha5.tif")
    os.system("convert captcha5.tif -level %70,100% captcha5.tif")
    captcha = pytesseract.image_to_string(Image.open('captcha5.tif'),config='--oem 0 --dpi 70 --psm 8 -c tessedit_char_whitelist=0123456789')
    captcha = captcha.replace(" ", "").strip()
    print(captcha)

dir = '/home/gatete/Workspace/MM-S/auto-captcha/imagenes/captcha'
directorio = pathlib.Path(dir)
for fichero in directorio.iterdir():
    print(fichero.name)
    resolve(fichero.name)
