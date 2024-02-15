print("Hola buenas tardes")
cantManzana = float(input ("Cuantas manzanas va a llevar: "))
print(cantManzana)
precioManzana = float(input("Precio de las manzanas: "))
print(precioManzana)

descuento = (cantManzana * precioManzana)*.10
descSecreto =(cantManzana * precioManzana)*.20
if cantManzana >= 30:
    print(f"Total con super descuento: {(cantManzana*precioManzana)-descSecreto}")
elif cantManzana >= 10:
    print(f"Total con descuento: {(cantManzana * precioManzana)-descuento}")
    
else :
    print(f"Total: {(cantManzana * precioManzana)}")