from funciones import (
    mostrar_menu,
    play_sound,
    limpiar_pantalla,
    utn_mostrar_nombres_heroes,
    utn_mostrar_identidades_heroes,
    utn_mostar_heroe_mayor_altura,
    utn_mostrar_heroes_mas_fuertes,
    filtrar_heroes_generodef
    
)

from validaciones import validar_opcion

def utn_heroes_app(
        lista_nombres,
        lista_identidades,
        lista_poderes,
        lista_alturas,
        lista_generos
        ):
    
    while True:

        mostrar_menu()

        opcion = validar_opcion(1,10)
        play_sound()

        match opcion:
            case 1:
                utn_mostrar_nombres_heroes(lista_nombres)
            case 2:
                utn_mostrar_identidades_heroes(lista_identidades)
            case 3:
                utn_mostar_heroe_mayor_altura(
                    lista_nombres,
                    lista_identidades,
                    lista_poderes,
                    lista_alturas,
                    lista_generos)
            case 4:
                utn_mostrar_heroes_mas_fuertes(
                    lista_nombres,
                    lista_identidades,
                    lista_poderes,
                    lista_alturas,
                    lista_generos
                )
            case 5:
                    filtrar_heroes_generodef(
                        lista_alturas,
                        lista_generos,
                        lista_identidades,
                        lista_nombres,
                        lista_poderes,
                        genero="Femenino"
                    )
            case 6:
                    filtrar_heroes_generodef(
                        lista_alturas,
                        lista_generos,
                        lista_identidades,
                        lista_nombres,
                        lista_poderes,
                        genero="Masculino"
                    )
            case 7:
                pass
            case 8:
                pass
            case 9:
                pass
            case 10: # Salir del programa
                break
        limpiar_pantalla()
