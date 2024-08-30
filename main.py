from contactos.busqueda import *
from contactos.gestion import *
from contactos.mostrar import *
from contactos.actualizar import *
from contactos.eliminar import *

def menu():
    input("Presione enter \n")
    print("Bienvenido al menú \n")
    print("Ingrese un número para acceder a la funcionalidad \n")
    print("[1]. Agregar contacto \n")
    print("[2]. Buscar contacto \n")
    print("[3]. Mostrar Todo \n")
    print("[4]. Actualizar \n")
    print("[5]. Eliminar \n")
    print("[6-9]. Salir \n")
    opc = int(input("Seleccione una opción \n"))

    if opc == 1:
        print("Bienvenido al menú de ingreso \n")
        nombre = input("Ingrese el nombre \n")
        correo = input("Ingrese el correo \n")
        agregar_contacto(nombre, correo)
        print("Los contactos actualizados son: \n")
        mostrar_contacto()
        menu()
    elif opc == 2:
        print("Bienvenido al menú de búsqueda \n")
        nombre = input("Ingrese el nombre \n")
        coincidencia=[]
        coincidencia =buscar_contacto(nombre)
        print("Contactos encontrados")
        if coincidencia ==[]:
            print("No se encontraron coincidencias")
        else:
            for i in coincidencia:
                print(f" {i[0]} - {i[1]}")
        menu()
    elif opc == 3:
        print("Bienvenido al menú de mostrar \n")
        print("Los contactos registrados son: \n")
        mostrar_contacto()
        menu()
    elif opc == 4:
        print("Bienvenido al menú de actualizar \n")
        mostrar_contacto()
        indice = int(input("Seleccione cual desea modificar \n"))
        nombre = input("Ingrese el nuevo nombre \n")
        correo = input("Ingrese el nuevo correo \n")
        actualizar_contacto(indice, nombre, correo)
        menu()
    elif opc == 5:
        print("Bienvenido al menú de eliminar \n")
        mostrar_contacto()
        indice = int(input("Seleccione cual desea modificar \n"))
        eliminar_contacto(indice)
        menu()
    else:
        print("Gracias por usar el programa \n")
        exit()

menu()
