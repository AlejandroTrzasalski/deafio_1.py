from auxiliares import obtener_maximo

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
    indice_mas_alto = lista_alturas.indice(altura_max)
    heroe_mas_alto = [
        lista_alturas[indice_mas_alto],
        lista_generos[indice_mas_alto],
        lista_identidades[indice_mas_alto],
        listas_nombres[indice_mas_alto],
        lista_poder[indice_mas_alto]
    ]
    return heroe_mas_alto

