# Copyright (C) 2024 <UTN FRA>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import pygame.mixer as mixer
import time



def limpiar_pantalla():
    """
    The function `limpiar_pantalla` clears the console screen and waits for user input to continue.
    """
    import os
    _ = input("\nPresiona Enter para continuar...")
    os.system('cls' if os.name in ['nt', 'dos'] else 'clear')

def play_sound():
    """
    The `play_sound` function initializes the mixer, loads a sound file, sets the volume to 0.4, and
    plays the sound.
    """
    mixer.init()
    mixer.music.load('./assets/snd/select.mp3')
    mixer.music.set_volume(0.4)
    mixer.music.play()
    time.sleep(0.4)

"""
D1 - En el modulo "auxiliares": 
Desarrolla la funcion "mostrar_nombre" 
la cual recibira como parametros, la lista de nombres y un numero entero 
que representara el indice de la lista el cual debe extraer el nombre, 
luego debe retornarlo.
"""

def mostrar_nombre(lista_nombres: list,indice: int) -> str:
    if indice < 0 or indice > len(lista_nombres):
        print("Error. Ingrese otro numero. Ese numero no esta en la lista.\n")
    else:
        lista_nombres[indice]

""" 
D4 - En el modulo "auxiliares": Desarrolla la funcion "obtener_maximo", 
la cual recibira como parametro una lista de numeros y 
debe obtener el numero mas grande, 
luego retornarlo como un flotante.
"""

def obtener_maximo(lista_numeros: list) -> float:
    maximo = None
    for numero in lista_numeros:
        if not maximo or maximo < numero:
            maximo = numero
    return float(maximo)


def imprimir_datos_heroes(
        indice: int,
        lista_alturas: list,
        lista_generos: list,
        lista_identidades: list,
        listas_nombres: list,
        lista_poder: list):
    
    mensaje = f"Nombre: {listas_nombres[indice]:15} | Identidad: {lista_identidades[indice]:15}"\
    f" | Genero: {lista_generos[indice]}   | Poder: {lista_poder[indice]}  |  Altura: {lista_alturas[indice]}"
    print(mensaje)


"""
D8 - En el modulo "auxiliares": Desarrolla la funcion "promedio" la cual recibira como parametro una lista de numeros, 
debe retornar el promedio numerico.
"""
def promedio_de_lista_numerica (lista_numeros: list) -> int:
    return sum(lista_numeros) / len(lista_numeros)

# if __name__ == '__main__':
#     lista_testing = [1,5,10,15,20,88,1110]
#     numero = obtener_maximo(lista_testing)
#     print(numero)