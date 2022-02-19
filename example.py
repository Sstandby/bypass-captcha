contador = 0
contador_2 = 0
def processNum(Num, Num2):
    global contador
    global contador_2
    for i in range(54):
      temp = Num
      contador_2 += 1
      for x in range(10):
         temp_new = temp[:i] + f'{x}' + temp[contador_2:]
         print(temp_new)
         if int(temp_new) == int(Num2):
            contador += 1
            print("LOGRADO")
            break
      if contador == 1:
         return temp_new
#Numero del resolver:  137488  - Numero del archivo:  737488
print(contador)
print(processNum(Num="137488", Num2="737488"))
