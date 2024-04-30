class persona:
    def __init__(self,nombre,apellidoP,apellidoM,edad,codigo):
        self.nombre = nombre
        self.apellidoP  = apellidoP
        self.apellidoM = apellidoM
        self.edad= edad
        self.codigo = codigo
    
    def impimirNombreCompleto(self):
        print(f"nombre {self.nombre} apellido paterno {self.apellidoP} apellido materno {self.apellidoM}")
        
    #imprimir informacion del objeto
    def __str__(self):
        return f"Codigo: {self.codigo} nombre {self.nombre} apellido paterno {self.apellidoP} apellido materno {self.apellidoM} edad {self.edad}"
        
alumno1 = persona("Andy","Gonzalez","Serratos",24,1)
# alumno1.nombre  = "andy"
# alumno1.apellidoP = "gonzalez"
# alumno1.apellidoM  = "serratos"
# alumno1.edad = 24
# alumno1.codigo = 1
print(f"nombre alumno1: {alumno1.nombre}")
alumno1.impimirNombreCompleto()
    