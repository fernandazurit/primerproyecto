class Calculadora:
    def __init__(self, num_uno, num_dos):
        self.num_uno = num_uno
        self.num_dos = num_dos
    
    def sumar(self):
        return f"\nResultado:{self.num_uno + self.num_dos}"

    def restar(self):
        return f"\nResultado:{self.num_uno - self.num_dos}"

    def multiplicar(self):
        return f"\nResultado:{self.num_uno * self.num_dos}"
    
    def dividir(self):
        if self.num_uno != 0:
            return f"\nResultado:{self.num_uno / self.num_dos}"
        else:
            return "\nNo se pudo realizar la división porque el primer número es 0"
    
    def dividir_redondear(self):
        if self.num_uno != 0:
            return f"\nResultado:{self.num_uno // self.num_dos}"
        else:
            return "\nNo se pudo realizar la división porque el primer número es 0"
        


numero_uno = int(input("\nIngrese el primer número: "))
numero_dos = int(input("\nIngrese el segundo número: "))
operacion = int(input("\n1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. Dividir y redondear\nIndique la operación que desea realizar: "))

calculadora = Calculadora(numero_uno, numero_dos)

match operacion:
    case 1:
        print(calculadora.sumar())
    case 2:
        print(calculadora.restar())
    case 3:
        print(calculadora.multiplicar())
    case 4:
        print(calculadora.dividir())
    case 5:
        print(calculadora.dividir_redondear())
    case _:
        print("\nLa operación ingresada no es correcta.")
        