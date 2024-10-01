from .auxiliares import obtener_maximo
from .auxiliares import promedio_de_lista_numerica
from .auxiliares import obtener_mitad_de_maximo

""" 
D2 - En el modulo "funciones": Desarrolla la funcion 
"utn_mostrar_nombres_heroes" la cual recibira como parametro la lista de nombres. 
Dentro debe iterarla y mostrar en consola cada uno de los elementos.
"""
def utn_mostrar_nombres_heroes(lista_nombres: list):
    
    for nombre in lista_nombres:
        print(nombre)

""" 
D3 - En el modulo "funciones": Desarrolla la funcion 
"utn_mostrar_identidades_heroes" la cual recibira como parametro la lista de identidades. 
Dentro debe iterarla y mostrar en consola cada uno de los elementos.
"""

def utn_mostrar_identidades_heroes(lista_identidades: list):

    for identidad in range(len(lista_identidades)):
        print(lista_identidades[identidad])

""" 
D5 - En el modulo "funciones": Desarrolla la funcion "utn_mostrar_heroe_mayor_altura" 
la cual recibira por parametro las 5 listas, dentro debe mostrar todos los datos del heroe mas alto. 
Debe llamar a la funcion "obtener_maximo"
"""


def utn_mostar_heroe_mayor_altura(
        lista_alturas: list,
        lista_generos: list,
        lista_identidades: list,
        listas_nombres: list,
        lista_poder: list) -> list:
    
    altura_max = obtener_maximo(lista_alturas)
    indice_mas_alto = lista_alturas.index(altura_max)

    heroe_mas_alto = [
        lista_alturas[indice_mas_alto],
        lista_generos[indice_mas_alto],
        lista_identidades[indice_mas_alto],
        listas_nombres[indice_mas_alto],
        lista_poder[indice_mas_alto]
    ]
    
    print(heroe_mas_alto)

def utn_mostrar_heroes_mas_fuertes(
        lista_alturas: list,
        lista_generos: list,
        lista_identidades: list,
        listas_nombres: list,
        lista_poder: list
):
    max_poder = obtener_maximo(lista_poder)

    for indice in range(len(lista_poder)):
        if lista_poder[indice] == max_poder:
            mensaje = f"Nombre: {listas_nombres[indice]} | Identidad: {lista_identidades[indice]}"\
            f" | Genero: {lista_generos[indice]}   | Poder: {lista_poder[indice]}  |  Altura: {lista_alturas[indice]}"
            print(mensaje)



""" 
D7 - En el modulo "funciones": Desarrolla la funcion 
 **"utn_filtrar_heroes_genero"** la cual 
recibirá por parametros las 5 listas y 
el genero a filtrar. 
El encontrar cada elemento del genero buscado, 
debe imprimir los datos completos del heroe del mismo indice."""
def filtrar_heroes_generodef (
        lista_alturas: list,
        lista_generos: list,
        lista_identidades: list,
        listas_nombres: list,
        lista_poder: list,
        genero: str) -> None:
    
    for indice in range(len(lista_generos)):
        if lista_generos[indice] == genero:
            mensaje = f"Nombre: {listas_nombres[indice]} | Identidad: {lista_identidades[indice]}"\
            f" | Genero: {lista_generos[indice]}   | Poder: {lista_poder[indice]}  |  Altura: {lista_alturas[indice]}"
            print(mensaje)

""" 
D9 - En el modulo "funciones": Desarrolla la funcion **"utn_mostrar_heroes_poder_superior_promedio"** 
la cual recibira por parametro las 5 listas, 
llamara a la funcion "promedio" para encontrarlo, 
luego debera mostrar los datos de todos los heroes que tengan un poder superior al promedio.
"""

def utn_mostrar_heroes_poder_superior_promedio (
        lista_alturas: list,
        lista_generos: list,
        lista_identidades: list,
        listas_nombres: list,
        lista_poder: list
):
    promedio = promedio_de_lista_numerica(lista_poder)

    for indice in range(len(lista_poder)):
        if lista_poder[indice] > promedio:
            mensaje = f"Nombre: {listas_nombres[indice]} | Identidad: {lista_identidades[indice]}"\
            f" | Genero: {lista_generos[indice]}   | Poder: {lista_poder[indice]}  |  Altura: {lista_alturas[indice]}"
            print(mensaje)
    
    print(mensaje) 

def utn_mostrar_heroes_mas_debiles(
        lista_alturas: list,
        lista_generos: list,
        lista_identidades: list,
        lista_nombres: list,
        lista_poder: list
):
    menos_mitad_altura = obtener_mitad_de_maximo(lista_alturas)

    for i in range(len(lista_alturas)):
        if lista_alturas[i] <= menos_mitad_altura:
            mensaje = f"Nombre: {lista_nombres[i]} | Identidad: {lista_identidades[i]} | " \
                    f"Genero: {lista_generos[i]} | Poder: {lista_poder[i]} | Altura: {lista_alturas[i]}"
        print(mensaje)


def ordenar_burbujeo_heroes(lista_nombres: list, lista_poder: list):
    
    for indice_1 in range(len(lista_poder)-1):
        for indice_2 in range(indice_1 + 1, len(lista_poder)):
            
            if lista_poder[indice_1] > lista_poder[indice_2]: 
                
                aux_poder = lista_poder[indice_1]
                lista_poder[indice_1] = lista_poder[indice_2]
                lista_poder[indice_2] = aux_poder
                
                
                aux_nombre = lista_nombres[indice_1]
                lista_nombres[indice_1] = lista_nombres[indice_2]
                lista_nombres[indice_2] = aux_nombre
                mensaje = f"Nombre: {lista_nombres[indice_2]} | Poder: {lista_poder[indice_2]} |"
                
        print(mensaje)

def ordenar_burbujeo_alturas_desc(lista_nombres: list, lista_alturas: list):

    for indice_1 in range(len(lista_alturas)-1):
        for indice_2 in range(indice_1 + 1, len(lista_alturas)):
            
            if lista_alturas[indice_1] < lista_alturas[indice_2]: 
                
                aux_altura = lista_alturas[indice_1]
                lista_alturas[indice_1] = lista_alturas[indice_2]
                lista_alturas[indice_2] = aux_altura
                
                
                aux_nombre = lista_nombres[indice_1]
                lista_nombres[indice_1] = lista_nombres[indice_2]
                lista_nombres[indice_2] = aux_nombre
                mensaje = f"Nombre: {lista_nombres[indice_2]} | Altura: {lista_alturas[indice_2]} |"
                
        print(mensaje)
        
