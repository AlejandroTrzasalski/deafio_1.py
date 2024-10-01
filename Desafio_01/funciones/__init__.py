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

# from .funciones import (
#     utn_filtrar_heroes_genero, utn_mostrar_heroe_mayor_altura,
#     utn_mostrar_heroes_mas_fuertes, utn_mostrar_identidades_heroes,
#     utn_mostrar_nombres_heroes, utn_mostrar_heroes_poder_superior_promedio,
#     utn_mostrar_heroes_mas_debiles
# )

from .funciones import (
    utn_mostrar_nombres_heroes,
    utn_mostrar_identidades_heroes,
    utn_mostar_heroe_mayor_altura,
    utn_mostrar_heroes_mas_fuertes,
    filtrar_heroes_generodef,
    utn_mostrar_heroes_poder_superior_promedio,
    utn_mostrar_heroes_mas_debiles,
    ordenar_burbujeo_heroes,
    ordenar_burbujeo_alturas_desc,
    elegir_des_o_asc
)

from .auxiliares import play_sound, limpiar_pantalla
from .salida_consola import mostrar_menu