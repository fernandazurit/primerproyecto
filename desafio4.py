class Agenda:
    def __init__(self, contactos):
        self.contactos = contactos
    
    # Operación 1
    def crear_contacto(self, nombre, telefono, email):
        self.contactos.append(Contacto(nombre, telefono, email))
        return "\nContacto creado exitosamente\n"

    # Operación 2
    def borrar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                self.contactos.remove(contacto)
                return "\nContacto eliminado exitosamente\n"

    # Operacion 3
    def editar_contacto(self, dato, nombre, telefono, email):
        for contacto in self.contactos:
            if contacto.nombre == dato:
                contacto.nombre = nombre
                contacto.telefono = telefono
                contacto.email = email
        return "\nContacto editado exitosamente\n"


    # Operación 4
    def mostrar_contactos(self):
        print("\n\nContactos: \n")
        for contacto in self.contactos:
            print(contacto)

    # Operación 5
    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                return contacto
    
    

class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        
    def __str__(self):
        return f"Nombre: {self.nombre}\nTeléfono: {self.telefono}\nEmail: {self.email}\n"
