from .gestion import *

def mostrar_contacto():
    print("Los contactos registrados son:")
    for l in range(0,len(lista_contactos)):
        print(f"[{l+1}] Nombre: {lista_contactos[l][0]}, Email: {lista_contactos[l][1]}")
    print("---------")