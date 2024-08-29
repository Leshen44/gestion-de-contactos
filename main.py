from contactos.busqueda import *
from contactos.gestion import *
from contactos.mostrar import *
from contactos.actualizar import *


def menu():
    input("Presione enter")
    print("Bienvenido al menu \n")
    print("[1]. Agregar contacto \n")
    print("[2]. Buscar contacto \n")
    print("[3]. Mostrar Todo \n")
    print("[4]. Actualizar \n")
    print("[5-9]. Salir \n")
    opc = int(input("Seleccione una opcion \n"))
    

    if opc == 1:
        print("Bienvenido al menu de ingreso \n")
        nombre = input("Ingrese el nombre \n")
        correo = input("Ingrese el correo \n")
        agregar_contacto(nombre, correo)
        mostrar_contacto()
        menu()
    elif opc == 2:
        print("Bienvenido al menu de busqueda \n")
        nombre = input("Ingrese el nombre \n")
        buscar_contacto(nombre)
        menu()
    elif opc == 3:
        print("Bienvenido al menu de mostrar \n")
        mostrar_contacto()
        menu()
    elif opc==4:
        print("Bienvenido al menu de actualizar \n")
        mostrar_contacto()
        indice=int(input("Seleccione cual desea modificar \n"))
        nombre = input("Ingrese el nuevo nombre \n")
        correo = input("Ingrese el nuevo correo \n")
        actualizar_contacto(indice,nombre, correo)
        menu()
    else:
        exit()


menu()