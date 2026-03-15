def mostrar_elegir_opcion(titulo,lista_opciones):
    print(f"     {titulo}")          
    # Elegir un trimestre o elegir cargar todos
    opciones = lista_opciones
    for opcion in range(len(opciones)):
        print(f"{opcion + 1}. {opciones[opcion]}")
    
    eleccion = input("Ingrese el numero de una opción: ")        
    eleccion = validar_opcion(eleccion, opciones)
    
    return eleccion

def validar_opcion(eleccion, lista_opciones):
    if int(eleccion) not in range(1,len(lista_opciones) + 1):
        while True:
            eleccion = input("Opción inválida. Por favor, ingrese un número válido: ")
            if int(eleccion) in range(1,len(lista_opciones) + 1):
                break
    return eleccion

def solicitar_dato(nombre_del_dato,num_materias_del_prof=0,lista_codigos_materias=[]):
    dato = None
    if nombre_del_dato != 'lista de materias':
        dato = input(f"Ingrese el dato {nombre_del_dato}: ")
    
    #cedula 5 millones hasta 40 millones
    if nombre_del_dato == 'cedula':
        dato = validar_cedula(dato)
    #email
    #elif
    #apellido
    #nombre
    #max_carga  (numero)
    #materias
     
    elif nombre_del_dato == 'lista de materias':
        dato = validar_lista_materias(num_materias_del_prof, lista_codigos_materias)
    
    return dato

def validar_cedula(cedula):
    #5 millones hasta 40 millones
    while True:
        if cedula.isdigit():
            if int(cedula)>5000000 and int(cedula)<40000000:
                return cedula
        cedula = input("Opción inválida. Por favor, ingrese una cedula válida: ")
    
    

def validar_correo():
    pass

def validar_numero():
    pass

def validar_lista_materias(num_materias_del_prof,lista_codigos_materias):
    list_profesor = []
    list_codigos_usados = []
    print('Codigos:')
    for i in range(len(lista_codigos_materias)):
        print(f'{i+1} {lista_codigos_materias[i]}')
    
    while len(list_profesor) < num_materias_del_prof:
        print(f'Materias del profesor {list_profesor}')
        elegido = input(f'Seleccione el numero de la materia a agregar (maximo {num_materias_del_prof}):')
        if elegido.isdigit():
            if int(elegido) in range(1,len(lista_codigos_materias)+1):
                if lista_codigos_materias[int(elegido)-1] not in list_codigos_usados:
                    list_profesor.append(lista_codigos_materias[int(elegido)-1])
                    list_codigos_usados.append(lista_codigos_materias[int(elegido)-1])
                else:
                    print('Materia ya elegida')
        cont = input(f'Desea continuar (y/n):')
        if cont == 'n':
            break
    
    return list_profesor

def agregar_eliminar_materia(lista_materias_prof,num_materias_del_prof,lista_codigos_materias):
    while True:
        titulo = '--- Modificacion de materias ---'
        lista_opciones = ['Agregar materia','Eliminar materia']
        eleccion = mostrar_elegir_opcion(titulo,lista_opciones)
        
        # Agregar
        if eleccion == "1":
            while len(lista_materias_prof) < num_materias_del_prof:
                print('Codigos:')
                for i in range(len(lista_codigos_materias)):
                    print(f'{i+1} {lista_codigos_materias[i]}')
                    print('')
                elegido = input(f'Seleccione el numero de la materia a agregar (maximo {num_materias_del_prof}):')
                if elegido.isdigit():
                    if int(elegido) in range(1,len(lista_codigos_materias)+1):
                        lista_materias_prof.append(lista_codigos_materias[int(elegido)-1])
        if eleccion == '2':
            if len(lista_materias_prof)>0:
                print('Materias del profesor:')
                for i in range(len(lista_materias_prof)):
                    print(f'{i+1} {lista_materias_prof[i]}')
                    print('')
                elegido = input(f'Seleccione el numero de la materia a eliminar:')
                if elegido.isdigit():
                    if int(elegido) in range(1,len(lista_materias_prof)+1):
                        lista_materias_prof.pop(int(elegido)-1)
            else:
                print('El profesor no tiene materias')
                                 
        cont = input(f'Desea continuar (y/n):')
        if cont == 'n':
            break
        
    return lista_materias_prof