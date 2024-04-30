cont = 0
numero = int(input('Ingresa un numero:'))


while numero < 0 or numero >= 20:
    print("El numero no se encuentra en el rango (0, 20). Por favor, ingresa otro número.")
    numero = int(input('Ingresa un numero:'))
    cont += 1

print("Numeros ingresados:", cont, "antes de encontrar un numero dentro del rango")

