lista_contactos=[("Juan Pérez","juan@correo.cl"),("María López","maria@correo.cl")]

def agregar_contacto(nombre,correo):
    lista_contactos.append((nombre,correo))
    print(f"Contacto '{nombre}' añadido exitosamente \n")