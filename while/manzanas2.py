print("Hola buenas tardes")
cantManzana = float(input ("Cuantas manzanas va a llevar: "))
print(cantManzana)

while cantManzana > 0:
    precioManzana = float(input("Precio de las manzanas: "))
    print(precioManzana)
    print("Total es de: ") 
    print("Total: ", cantManzana * precioManzana)
    print("Total: " + str(cantManzana * precioManzana))
    print(f"Total: {cantManzana * precioManzana}")


