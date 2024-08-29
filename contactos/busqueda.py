from .gestion import *

def buscar_contacto(nombre):
	for i in lista_contactos:	
		if nombre in i[0]:
			print(f"Los Contactos encontrados son {i[0]} - {i[1]}")
			
