class Estudiante:
    def __init__(self, nombre, nota_evaluacion):
        self.nombre = nombre
        self.nota_evaluacion = nota_evaluacion
        
    def consultar_atributos(self):
        return f"Nombre: {self.nombre} \nNota de evaluación: {self.nota_evaluacion} \n"
    
    def consultar_nota(self):
        if self.nota_evaluacion >= 6:
            return f"El estudiante aprobó con {self.nota_evaluacion} \n"
        else:
            return f"El estudiante desaprobó con {self.nota_evaluacion} \n"
            
            
estudiante_uno = Estudiante('Jorge', 7)
estudiante_dos = Estudiante('Pablo', 9)
estudiante_tres = Estudiante('Raul', 4)

print(estudiante_uno.consultar_atributos())
print(estudiante_tres.consultar_nota())
print(estudiante_dos.consultar_atributos())
        