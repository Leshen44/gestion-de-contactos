from .gestion import *

def buscar_contacto(nombre):
	coincidencias=[]
	for i in lista_contactos:	
		if nombre in i[0]:
			coincidencias.append((i[0],i[1]))
			
			# print(f"Los Contactos encontrados son {i[0]} - {i[1]}")
	return coincidencias	
