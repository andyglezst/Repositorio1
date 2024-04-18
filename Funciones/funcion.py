
def saludo(nombre):
    print("Hola",nombre)
#saludo("Andy")


def numParImpar(num):
    if num %2 == 0:
        print(num, "es par")
    else: 
        print(num, "es impar")
#numParImpar(8)

def totalIva(cant, iva):
    iva = iva * .01
    if iva > 0:
        total = print((cant*iva)+cant)
    else:
        total = print((cant*.21)+cant)

  #  return total 

totalIva(100,16)