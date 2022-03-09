try:
        from PIL import Image
except ImportError:
        import Image
import os
import re
import pathlib
import pytesseract

contador = 0
dir = f'{pathlib.Path(__file__).parent.absolute()}/bypass-captcha/imagenes/captcha'

def processNum(Num, Num2):

    '''Fuerza bruta de numeros de 6 digitos del 0 al 9.

    **Parametros**
       - **Num**: Primer numero en comprobar
       - **Num2**: Numero verdadero que debe acertar **Num**
    '''

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

    '''Pide como parametro una IMG (imagen) la cual se tomara como el captcha
    a resolver por la función

    **Parametros**
       - **img**: Imagen del captcha
    '''

    os.system(f"convert {dir}/{img} -morphology Erode Disk:2.2 captcha5.tif")
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

print(contador)
