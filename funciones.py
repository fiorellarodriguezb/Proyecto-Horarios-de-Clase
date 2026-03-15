def mostrar_elegir_opcion(titulo,lista_opciones):
    print(f"     {titulo}")          
    # Elegir un trimestre o elegir cargar todos
    opciones = lista_opciones
    for opcion in range(len(opciones)):
        print(f"{opcion + 1}. {opciones[opcion]}")
    
    eleccion = input("Ingrese el numero de una opción: ")        # Validar
    eleccion = validar_opcion(eleccion, opciones)
    
    return eleccion

def validar_opcion(eleccion, lista_opciones):
    if int(eleccion) not in range(1,len(lista_opciones) + 1):
        while True:
            eleccion = input("Opción inválida. Por favor, ingrese un número válido: ")
            if int(eleccion) in range(1,len(lista_opciones) + 1):
                break
    return eleccion