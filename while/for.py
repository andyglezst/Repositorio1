numero1 =  int(input("Ingresa el numero 1:"))
numero2 =  int(input("Ingresa el numero 2:"))
table = range(numero1, numero2)
for numero in table:
    if numero %2 == 0 :
        print(f"Este numero es par {numero}")
    else:            
        print(f"Este numero es impar {numero}")

nombre = "Andy"
for letra in nombre:
    print(letra)