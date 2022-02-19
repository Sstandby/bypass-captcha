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

def processNum(Num, Num2):
    global contador
    j = 0
    for i in range(54):
      temp = Num
      j += 1
      for x in range(10):
         temp_new = temp[:i] + f'{x}' + temp[j:]
         if int(temp_new) == int(Num2):
            print(temp_new)
            contador += 1
            break
      if contador == 1: break

def resolve(img):
    os.system(f"convert {dir}/{img} -morphology Erode Disk:2.2 captcha5.tif")
    os.system("convert captcha5.tif -morphology Dilate Disk:1.2 captcha5.tif")
    os.system("convert captcha5.tif -gaussian-blur 0 -threshold 41% -paint 1 captcha5.tif")
    captcha = pytesseract.image_to_string(Image.open('captcha5.tif'),config='--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789')
    captcha = captcha.replace(" ", "").strip()
    return captcha

for fichero in directorio.iterdir():
    try:
      numero = resolve(fichero.name)
      temp = fichero.name.replace(".png", "").strip()
      print("Numero del resolver: ", numero, " - Numero del archivo: ", temp)
      if numero != '' and int(numero) == int(temp):
         contador += 1
      else:
         if len(numero) == 6:
            print("Verify")
            processNum(numero, temp)
    except ValueError:
         print("Error")
    #else:
    #: numero.re

print(contador)
