class Triangulo:
    def __init__(self, lado_uno, lado_dos, lado_tres):
        self.lado_uno = lado_uno
        self.lado_dos = lado_dos
        self.lado_tres = lado_tres
    
    def lado_mayor(self):
        mayor = self.lado_uno
        if mayor < self.lado_dos:
            mayor = self.lado_dos
            if mayor < self.lado_tres:
                mayor = self.lado_tres
                return f"El lado mayor mide {mayor}cm"
            else:
                return f"El lado mayor mide {mayor}cm"
        elif mayor < self.lado_tres:
            mayor = self.lado_tres
            return f"El lado mayor mide {mayor}cm"
        else:
            return f"El lado mayor mide {mayor}cm"
        
    def tipo_triangulo(self):
        if self.lado_uno == self.lado_dos and self.lado_dos == self.lado_tres:
            return "El triangulo es equilátero\n"
        # Refactorizar el elif
        elif self.lado_uno != self.lado_dos and self.lado_uno != self.lado_tres and self.lado_dos != self.lado_tres:
            return "El triangulo es escaleno\n"
        else:
            return "El triangulo es isóceles\n"
    

primer_lado = int(input("Ingrese el primer lado del triangulo: "))
segundo_lado = int(input("Ingrese el segundo lado del triangulo: "))
tercer_lado = int(input("Ingrese el tercer lado del triangulo: "))

triangulo_usuario = Triangulo(primer_lado, segundo_lado, tercer_lado)

print(triangulo_usuario.lado_mayor())
print(triangulo_usuario.tipo_triangulo())