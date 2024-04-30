num1 = int(input("Ingresa el primer numero:"))
num2 = int(input("Ingresa el segundo numero:"))
num3 = int(input("Ingresa el segundo numero:"))

if num1 == num2 and num1 == num3 :
    print("Los 3 numeros son iguales")
elif num1 == num2 or num1 == num3 or num2 == num3:
    print("Dos numeros son iguales")
else :
    print("Los tres numeros son diferentes")
