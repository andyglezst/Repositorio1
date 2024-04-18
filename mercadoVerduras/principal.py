import funcionesM
import time

descuento = 0
total = 0
cantidadManzana = 1

print("Hola buenas tardes")
opcion, nombreFruta = funcionesM.menu()

while cantidadManzana != 0:
    # PARTE 1
    # PEDIR DATOS
    cantidadManzana = float(input(f'Dime la cantidad de {nombreFruta} vendidas: '))
    if cantidadManzana == 0:
        break
    precioManzana = float(input('Dime el precio de la manzana: '))
    
    total = cantidadManzana * precioManzana
    # PARTE 2
    # CALCULAR DESCUENTO
    descuento = funcionesM.calculoDesc(cantidadManzana,precioManzana)
    # PARTE 3
    # MOSTRAR RESULTADOS
    print(f"Total: {total}" )
    
    time.sleepsleep(5)