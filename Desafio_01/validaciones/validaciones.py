def validar_opcion(num_min: int, num_max: int):
    opcion = input(f'Ingrese una opcion [{num_min} y {num_max}] \n')

    # if not opcion or not opcion.isdigit() or not (num_min <= int(opcion) <= num_max):
    #     return validar_opcion(num_min,num_max)
    # else:
    #     return(int(opcion))
    if not opcion or not opcion.isdigit() or int(opcion) > num_max or int(opcion) < num_min:
        return validar_opcion(num_min,num_max)
    
    return(int(opcion))
    
if __name__ == '__main__':
    print(validar_opcion(1,10))