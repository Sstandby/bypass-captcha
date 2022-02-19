try:
        from PIL import Image
except ImportError:
        import Image
import os
import re
import pathlib
import pytesseract

#ABCDEFGHIJKMNLOPKRSTUVWXYZ1
contador = 0
dir = '/home/gatete/Workspace/MM-S/auto-captcha/imagenes/captcha'
directorio = pathlib.Path(dir)

def resolve(img):
    os.system(f"convert {dir}/{img} -morphology Erode Disk:2.2 captcha5.tif")
    os.system("convert captcha5.tif -morphology Dilate Disk:1.2 captcha5.tif")
    os.system("convert captcha5.tif -gaussian-blur 0 -threshold 41% -paint 1 captcha5.tif")
    captcha = pytesseract.image_to_string(Image.open('captcha5.tif'),config='--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789')
    captcha = captcha.replace(" ", "").strip()
    return captcha

for fichero in directorio.iterdir():
    numero = resolve(fichero.name)
    temp = fichero.name.replace(".png", "").strip()
    print("Numero del resolver: ", numero, " - Numero del archivo: ", temp)
    if numero != '' and int(numero) == int(temp):
       contador += 1
    #else:
    #: numero.re

print(contador)
