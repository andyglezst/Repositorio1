
nombre = "Andy" #Contexto global
def mostrarUsuario(nombreFuncion): #contexto local 
    print(nombreFuncion)
    print("Hola mundo")
    
def noMostrarUsuario():
    print("Ydna")
    print("Adios Mmndo") 
    
mostrarUsuario(nombre)
noMostrarUsuario(nombre)

