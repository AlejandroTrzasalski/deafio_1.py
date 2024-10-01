from funciones import (
    mostrar_menu,
    play_sound,
    limpiar_pantalla,
    utn_mostrar_nombres_heroes,
    utn_mostrar_identidades_heroes,
    utn_mostar_heroe_mayor_altura,
    utn_mostrar_heroes_mas_fuertes,
    filtrar_heroes_generodef,
    utn_mostrar_heroes_poder_superior_promedio,
    utn_mostrar_heroes_mas_debiles,
    ordenar_burbujeo_heroes,
    ordenar_burbujeo_alturas_desc
)

from validaciones import validar_opcion

def utn_heroes_app(
        lista_alturas,
        lista_generos,
        lista_identidades,
        lista_nombres,
        lista_poderes
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
                    lista_alturas,
                    lista_generos,
                    lista_identidades,
                    lista_nombres,
                    lista_poderes
                )
            case 4:
                utn_mostrar_heroes_mas_fuertes(
                    lista_alturas,
                    lista_generos,
                    lista_identidades,
                    lista_nombres,
                    lista_poderes
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
                filtrar_heroes_generodef(
                        lista_alturas,
                        lista_generos,
                        lista_identidades,
                        lista_nombres,
                        lista_poderes,
                        genero="No-Binario"
                    )
            case 8:
                utn_mostrar_heroes_poder_superior_promedio(
                        lista_alturas,
                        lista_generos,
                        lista_identidades,
                        lista_nombres,
                        lista_poderes
                )
            case 9:
                utn_mostrar_heroes_mas_debiles(
                        lista_alturas,
                        lista_generos,
                        lista_identidades,
                        lista_nombres,
                        lista_poderes
                )
            case 10:
                ordenar_burbujeo_heroes(
                    lista_nombres,
                    lista_poderes
                    )
            case 11:
                ordenar_burbujeo_alturas_desc(
                    lista_nombres,
                    lista_alturas
                    )
            case 12:
                pass
            case 13: # Salir del programa
                break
        limpiar_pantalla()
