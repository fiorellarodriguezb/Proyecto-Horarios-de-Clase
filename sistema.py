# Fiorella Rodriguez y Veronica Gonzalez

import csv
import matplotlib.pyplot as plt
import requests
from materia import Materia
from profesor import Profesor
from horario import Horario
 
from funciones import *


class Sistema():
    """
    Clase principal que orquesta la lógica del negocio del sistema de horarios.
    
    Se encarga de la integración con la API externa, el procesamiento de datos,
    la ejecución del algoritmo de asignación automática, la modificación manual
    de la oferta académica y la exportación de resultados a archivos CSV.
    """
    def __init__(self):
        self.codigos_materias = []
        self.materias_t1 = []
        self.materias_t2 = []
        self.materias_t3 = []
        self.profesores = []
        self.horarios = []  # lista de horarios generados (cada elemento es un dict)
    
    def prueba_csv(self):
              
       def guardar_horarios_csv(self):
        """
        Exporta el horario generado a un archivo CSV para que la información
        pueda ser consultada externamente o cargada en el futuro.
        """
        if not self.horarios:
            print("No hay un horario generado para guardar. Primero genere el horario en la opción 3.")
            return

        nombre_archivo = input("Ingrese el nombre del archivo para guardar (ej: mi_horario.csv): ").strip()
        if not nombre_archivo.endswith('.csv'):
            nombre_archivo += '.csv'

        try:
            with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as file:
                escritor = csv.writer(file)
                
                # Escribimos los encabezados de las columnas
                escritor.writerow(['Codigo Materia', 'Nombre Materia', 'Seccion', 'Dia', 'Hora', 'Profesor', 'Salon', 'Estado'])
                
                for h in self.horarios:
                    # Extraemos dia y hora de la tupla bloque (dia, hora)
                    dia = h.bloque[0] if h.bloque else "N/A"
                    hora = h.bloque[1] if h.bloque else "N/A"
                    
                    # Formateamos el nombre del profesor
                    prof = f"{h.profesor.nombre} {h.profesor.apellido}" if h.profesor else "Sin asignar"
                    
                    escritor.writerow([
                        h.materia_codigo,
                        h.materia_nombre,
                        h.seccion_num,
                        dia,
                        hora,
                        prof,
                        h.salon if h.salon else "N/A",
                        h.estado
                    ])
                    
            print(f"\n¡Éxito! El horario se ha exportado correctamente a: {nombre_archivo}")
        except Exception as e:
            print(f"Error crítico al intentar escribir el archivo: {e}")

        
    def menu_arranque(self,api_t1,api_t2,api_t3,api_profesores):
        
        while True:
            # Cargar datos de materias
            lista_opciones = ["Iniciar sin cargar datos", "Cargar datos desde API", "Cargar datos desde CSV", "Salir"]
            eleccion = mostrar_elegir_opcion(" Iniciando Sistema", lista_opciones)
            
            if eleccion == "1":
                print("Iniciando sin cargar datos...")
                self.menu_principal()
                break
            elif eleccion == "2":
                self.cargar_datos_API(api_t1,api_t2,api_t3,api_profesores)
                self.menu_principal()
                break
            elif eleccion == "3":
                print("Cargando datos desde un CSV...")
                
            elif eleccion == "4":
                # Guardar asignación de horarios en CSV
                self.guardar_horarios_csv()
                
                self.menu_principal()
                break
            elif eleccion == "5":
                print("Saliendo del sistema...")
                break
    

def cargar_datos_api(self):
        """
        Permite al usuario seleccionar un trimestre y descarga los datos 
        correspondientes de profesores y materias desde la API de GitHub.
        """
        print("\n--- Selección de Trimestre ---")
        print("1. Trimestre 2425-3")
        print("2. Trimestre 2526-1")
        print("3. Trimestre 2526-2")
        
        opcion = input("Seleccione el trimestre a gestionar: ").strip()
        
        # Diccionario para mapear la selección con el nombre de la carpeta en GitHub
        trimestres = {
            "1": "2425-3",
            "2": "2526-1",
            "3": "2526-2"
        }

        if opcion not in trimestres:
            print("Opción inválida. Volviendo al menú principal.")
            return

        trimestre_seleccionado = trimestres[opcion]
        base_url = f"https://raw.githubusercontent.com/FernandoSapient/BPTSP05/main/{trimestre_seleccionado}"
        
        try:
            # Carga de Profesores
            print(f"Descargando datos del trimestre {trimestre_seleccionado}...")
            res_prof = requests.get(f"{base_url}/profesores.json")
            res_prof.raise_for_status()
            datos_prof = res_prof.json()

            for p in datos_prof:
                # IMPORTANTE: Asegúrate de que 'Profesor' esté con P mayúscula
                nuevo = Profesor(
                    p['nombre'], p['apellido'], p['cedula'], 
                    p['correo'], p['materias'], p['max_carga']
                )
                self.profesores.append(nuevo)

            # Carga de Materias
            res_mat = requests.get(f"{base_url}/materias.json")
            res_mat.raise_for_status()
            datos_mat = res_mat.json()

            for m in datos_mat:
                # IMPORTANTE: Asegúrate de que 'Materia' esté con M mayúscula
                nueva = Materia(m['codigo'], m['nombre'], m['secciones'])
                self.materias.append(nueva)

            print(f"\n¡Éxito! Se cargaron los datos del trimestre {trimestre_seleccionado}.")

        except requests.exceptions.RequestException as e:
            print(f"Error de conexión con la API: {e}")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
             
def cargar_materias_tn(self, api_trimestre,num_trimestre):
        respuesta = requests.get(api_trimestre)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            for materia in datos:
                
                codigo = materia['Código']
                
                if codigo not in self.codigos_materias:
                    self.codigos_materias.append(codigo)
                
                nombre = materia['Nombre']
                secciones = materia['Secciones']
                                
                nueva_materia = Materia(codigo, nombre, secciones)  
                if num_trimestre == 1:
                    self.materias_t1.append(nueva_materia)
                elif num_trimestre == 2:
                    self.materias_t2.append(nueva_materia)
                elif num_trimestre == 3:
                    self.materias_t3.append(nueva_materia)
                    
def menu_principal(self):
        """
Interfaz de usuario de consola que gestiona el flujo principal del programa 
y el acceso a los diferentes módulos del sistema.
"""
        while True:
            # Funcionalidades del sistema por realizar
            titulo = '    ----- Bienvenido al sistema de horarios de clase. -----'
            opciones = ["Profesores", "Materias", "Generacion horarios", "Modificacion horarios","Estadisticas","Salir del sistema"]

            eleccion = mostrar_elegir_opcion(titulo, opciones)

            if eleccion == "1":
                # Modulo profesores
                self.modulo_profesores()    
            
            elif eleccion == "2":
                # Modulo materias
                self.modulo_materias()

            elif eleccion == "3":
                # Modulo generación de horarios
                self.generar_horarios()
                
            elif eleccion == "4":
                # Modulo modificacion de horarios
                self.modificar_horarios()
            
            elif eleccion == "5":
                # Modulo estadisticas
                self.ver_estadisticas()
                
            elif eleccion == "6":
                print("Saliendo del sistema...")
                break

            def ver_estadisticas(self):
                """
        Genera gráficos estadísticos sobre la asignación de carga de los profesores
        utilizando matplotlib.
        """
        if not self.horarios:
            print("No hay datos de horario para generar estadísticas. Primero genere el horario.")
            return

        # 1. Preparar los datos: Contar materias por profesor
        conteo_carga = {}
        for h in self.horarios:
            if h.estado == "asignada" and h.profesor:
                nombre_completo = f"{h.profesor.nombre} {h.profesor.apellido}"
                conteo_carga[nombre_completo] = conteo_carga.get(nombre_completo, 0) + 1

        if not conteo_carga:
            print("No hay profesores asignados en el horario actual.")
            return

        profesores = list(conteo_carga.keys())
        materias_asignadas = list(conteo_carga.values())

        # 2. Crear el gráfico de barras
        plt.figure(figsize=(10, 6))
        plt.bar(profesores, materias_asignadas, color='skyblue', edgecolor='navy')
        
        # 3. Personalización del gráfico
        plt.title('Carga Académica por Profesor (Materias Asignadas)', fontsize=14)
        plt.xlabel('Profesores', fontsize=12)
        plt.ylabel('Cantidad de Materias', fontsize=12)
        plt.xticks(rotation=45, ha='right') # Rotar nombres para que se lean bien
        plt.yticks(range(0, max(materias_asignadas) + 2)) # Escala de 1 en 1
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        
        plt.tight_layout() # Ajusta el diseño para que no se corten los nombres
        print("Generando gráfico... Por favor, cierre la ventana del gráfico para continuar.")
        plt.show()
            
def modulo_profesores(self):   
        while True:
            titulo = '    ----- Módulo Profesores -----'
            opciones = ["Ver lista de profesores", "Ver un profesor específico", "Agregar un profesor a la lista", "Eliminar un profesor de la lista", "Modificar la lista de materias de un profesor", "Volver al menú principal"]

            eleccion = mostrar_elegir_opcion(titulo, opciones)

            if eleccion == "1":
                # Ver la lista de profesores 
                if len(self.profesores)>0:
                    for profesor in self.profesores:
                        print(f"Profesor: {profesor.nombre} {profesor.apellido}. C.I:{profesor.cedula}")
                else:
                    print('No hay profesores registrados, carge datos o registre profesores.')
            elif eleccion == "2":
                # Ver un profesor específico
                if len(self.profesores)>0:
                    cedula = solicitar_dato('cedula')

                    profesor = None
                    for prof in self.profesores:
                        if prof.cedula == int(cedula):
                            profesor = prof
                            break   
                        
                    if profesor != None:
                        profesor.ver_datos() 
                    else:
                        print('No existe el profesor con la cedula ingresada')       
                else:
                    print('No hay profesores registrados, carge datos o registre profesores.')
                                
            
            elif eleccion == "3":
                if len(self.codigos_materias) > 0:
                    # Agregar un profesor a la lista 
                    cedula = solicitar_dato('cedula')
                    
                    encontrado = False
                    for prof in self.profesores:
                        if prof.cedula == int(cedula):
                            encontrado = True
                            break

                    if encontrado == False:
                        email = solicitar_dato('correo')
                        apellido = solicitar_dato('apellido')
                        nombre = solicitar_dato('nombre')
                        max_carga = solicitar_dato('numero')
                        materias = solicitar_dato('lista de materias', 4, self.codigos_materias)
                        nuevo_prof = Profesor(int(cedula),email,apellido,nombre,max_carga,materias)
                        self.profesores.append(nuevo_prof)
                        print('Profesor registrado.')
                        nuevo_prof.ver_datos()
                    else:
                        print('Cedula ya registrada.')
                else:
                        print('Por favor registre materias antes para asignarsela a un profesor.')
            
            elif eleccion == "4":
                # Eliminar un profesor de la lista 
                cedula = solicitar_dato('cedula')
                
                profesor = None
                for prof in self.profesores:
                    if prof.cedula == int(cedula):
                        profesor = prof
                        break   
                
                if profesor != None:
                    print('     Profesor a eliminar:')
                    profesor.ver_datos() 
                    cont = input(f'Desea eliminarlo (y/n):')
                    if cont.lower() == 'y':
                        for i in range(len(self.profesores)):
                            if self.profesores[i].cedula == int(cedula):
                                # Verificar y mostrar mensaje si cuando lo elimino se queda alguna materia sin profesor
                                self.profesores.pop(i)
                            print('Profesor eliminado')
                                   
                    else:
                        print('No existe el profesor con la cedula ingresada')
                    
            elif eleccion == "5":
                self.modificar_materias_profesor()
            
            elif eleccion == "6":
                print("Volviendo al menú principal...")
                break
            
def modificar_materias_profesor(self):
        # Modificar la lista de materias de un profesor (agregar o quitar materias)
        cedula = solicitar_dato('cedula')
        profesor = None
        for prof in self.profesores:
            if prof.cedula == int(cedula):
                profesor = prof
                break

        if profesor is None:
            print('No existe el profesor con la cedula ingresada')
            return

        print('     Profesor a editar:')
        profesor.ver_datos()
        # Modifico su lista de materias
        list_original = profesor.materias

        # Le pido la nueva lista al usuario
        list_materias_prof_editada = agregar_eliminar_materia(profesor.materias, 4, self.codigos_materias)

        copia_lista_profes = self.profesores.copy()
        for p in copia_lista_profes:
            if p.cedula == profesor.cedula:
                p.materias = list_materias_prof_editada

        # Verificar si cuando elimino la materia esa materia se queda sin profesores que la den
        for cod in list_original:
            if cod in list_materias_prof_editada:
                continue
            else:
                existe_profesor_que_la_dicte = False
                # Recorrer la lista copia verificando
                for prof in copia_lista_profes:
                    if cod in prof.materias:
                        existe_profesor_que_la_dicte = True
                        break
                # Mensaje advertencia
                if not existe_profesor_que_la_dicte:
                    print(f"La materia con el codigo {cod} quedara sin profesor")

        cont = input('Desea continuar y guardar la edicion (y/n):')
        if cont == 'y':
            self.profesores = copia_lista_profes

def modulo_materias(self):
        while True:
            titulo = "    ----- Módulo Materias -----"
            opciones = [
                "1. Ver todas las materias",
                "2. Buscar materia por código",
                "3. Agregar materia",
                "4. Eliminar materia",
                "5. Modificar materia",
                "6. Volver al menú principal"
            ]
            eleccion = mostrar_elegir_opcion(titulo, opciones)

            if eleccion == "1":
                for n, trimestre in [("2526-1", self.materias_t1), ("2526-2", self.materias_t2), ("2526-3", self.materias_t3)]:
                    print(f"\nTrimestre {n}:")
                    if not trimestre:
                        print("  (sin materias)")
                    else:
                        for m in trimestre:
                            m.ver_datos()
                print()

            elif eleccion == "2":
                codigo = solicitar_dato("codigo").strip()
                encontrado = None
                for grupo in [self.materias_t1, self.materias_t2, self.materias_t3]:
                    for m in grupo:
                        if m.codigo == codigo:
                            encontrado = m
                            break
                    if encontrado: break
                if encontrado:
                    encontrado.ver_datos()
                else:
                    print("Materia no encontrada.")

            elif eleccion == "3":
                codigo = solicitar_dato("codigo").strip()
                nombre = solicitar_dato("nombre").strip()
                secciones = solicitar_dato("numero").strip()
                trimestre = solicitar_dato("trimestre (1,2 o 3)").strip()
                if codigo in self.codigos_materias:
                    print("Ese código ya existe.")
                    continue
                try:
                    secciones_int = int(secciones)
                except:
                    secciones_int = 1
                    materia: any
                nueva = materia(codigo, nombre, secciones_int)
                self.codigos_materias.append(codigo)
                if trimestre == "2":
                    self.materias_t2.append(nueva)
                elif trimestre == "3":
                    self.materias_t3.append(nueva)
                else:
                    self.materias_t1.append(nueva)
                print("Materia agregada.")

            elif eleccion == "4":
                codigo = solicitar_dato("codigo").strip()
                eliminado = False
                for lista in [self.materias_t1, self.materias_t2, self.materias_t3]:
                    for i,m in enumerate(lista):
                        if m.codigo == codigo:
                            lista.pop(i)
                            if codigo in self.codigos_materias:
                                self.codigos_materias.remove(codigo)
                            eliminado = True
                            print("Materia eliminada.")
                            break
                    if eliminado: break
                if not eliminado:
                    print("No se encontró esa materia.")

            elif eleccion == "5":
                codigo = solicitar_dato("codigo").strip()
                materia_obj = None
                for lista in [self.materias_t1, self.materias_t2, self.materias_t3]:
                    for m in lista:
                        if m.codigo == codigo:
                            materia_obj = m
                            break
                    if materia_obj:
                        break
                if not materia_obj:
                    print("Materia no encontrada.")
                    continue
                print("Deje vacío para mantener valor actual.")
                new_nombre = input("Nuevo nombre: ").strip()
                new_secciones = input("Nuevas secciones: ").strip()
                if new_nombre:
                    materia_obj.nombre = new_nombre
                if new_secciones.isdigit():
                    materia_obj.secciones = int(new_secciones)
                print("Materia actualizada.")

            elif eleccion == "6":
                print("Volviendo al menú principal...")
                break

            else:
                print("Opción inválida. Intente de nuevo.")
        
def generar_horarios(self):
        """
Algoritmo de asignación automática. Distribuye las materias según la disponibilidad 
de los profesores, respetando su carga máxima y los bloques horarios de 1.5 horas.
"""
        # Bloques disponibles (par de días + hora)
        dias = ["Lunes y Miércoles", "Martes y Jueves"]
        horarios = [
            "7:00 - 8:30",
            "8:45 - 10:15",
            "10:30 - 12:00",
            "12:15 - 1:45",
            "2:00 - 3:30",
            "3:45 - 5:15",
            "5:30 - 7:00",
        ]

        # Solicitar la cantidad de salones disponibles (capacidad por bloque)
        while True:
            salones = input("Ingrese la cantidad de salones disponibles por bloque horario: ")
            if salones.isdigit() and int(salones) > 0:
                salones = int(salones)
                break
            print("Número inválido. Ingrese un número entero positivo.")

        # Seleccione el trimestre del cual desea generar un horario
        titulo = "Trimestres disponibles:"
        lista_opciones = ["2526-1", "2526-2", "2526-3"]
        eleccion = mostrar_elegir_opcion(titulo, lista_opciones)

        if eleccion == '1':
            materias = self.materias_t1
        elif eleccion == '2':
            materias = self.materias_t2
        elif eleccion == '3':
            materias = self.materias_t3

        if len(materias) == 0:
            print("No hay materias cargadas. Cargue datos antes de generar horarios.")
            return

        # Preparar estructura de bloques
        bloques = []
        for dia in dias:
            for hora in horarios:
                bloques.append((dia, hora))

        # Generar las secciones pendientes de asignar
        secciones_pendientes = []
        for materia in materias:
            try:
                num_secciones = int(materia.secciones)
            except Exception:
                num_secciones = 1

            for sec in range(1, num_secciones + 1):
                secciones_pendientes.append(Horario(materia.codigo,materia.nombre,sec))

        # Estado de asignaciones por bloque y por profesor
        bloque_asignaciones = {bloque: [] for bloque in bloques}
        profesor_estado = {}  # cedula -> {"materias": set(), "bloques": set(), "obj": Profesor}
        
        # Asignar secciones por bloque
        bloque_idx = 0
        total_bloques = len(bloques)
        for seccion in secciones_pendientes:
            intentos = 0
            asignada = False
            while intentos < total_bloques:
                bloque = bloques[bloque_idx]
                if len(bloque_asignaciones[bloque]) < salones:
                    asignada = self.asignar_seccion(seccion, bloque, bloque_asignaciones, profesor_estado)
                    if asignada:
                        break
                bloque_idx = (bloque_idx + 1) % total_bloques
                intentos += 1

            if not asignada:
                seccion.estado = "cerrada"
                seccion.bloque = bloques[bloque_idx]
        
        
                # después de self.horarios = secciones_pendientes
        cerradas = {}
        no_salon = {}
        bloques_disponibles = {}

        for bloque, asignadas in bloque_asignaciones.items():
            disponibles = salones - len(asignadas)
            if disponibles > 0:
                bloques_disponibles[bloque] = disponibles

        for s in self.horarios:
            if s.estado == "cerrada":
                cerradas[s.materia_codigo] = cerradas.get(s.materia_codigo, 0) + 1
            elif s.estado == "sin_salon":
                no_salon[s.materia_codigo] = no_salon.get(s.materia_codigo, 0) + 1

        print("\n--- Reporte de cierre por falta de profesor ---")
        if cerradas:
            for m, c in cerradas.items():
                print(f"{m}: {c} secciones cerradas")
        else:
            print("No hubo secciones cerradas por falta de profesor")

        print("\n--- Reporte de falta de salones ---")
        if no_salon:
            for m, c in no_salon.items():
                print(f"{m}: {c} secciones sin salon")
        else:
            print("No hubo secciones sin salon")

        print("\n--- Bloques con salones disponibles ---")
        if bloques_disponibles:
            for bloque, disp in bloques_disponibles.items():
                dia, hora = bloque
                print(f"{dia} {hora}: {disp} salones libres")
        else:
            print("No hay bloques con capacidad libre")
        

            # GENERAR REPORTE USANDO SELF.HORARIOS       
            #Una vez concluida la asignación, el sistema debe reportar 
            #1. Cuáles materias tuvieron secciones que se debieron cerrar por falta de profesores (y 
            #cuántas secciones de esa materia fueron) 
            #2. Cuáles materias tuvieron secciones que no se pudieron asignar por falta de salones 
            #(y cuántas secciones de esa materia fueron) 
            #3. Cuáles horarios quedaron con salones disponibles 
        
     
        
        # Guardar y mostrar resultados
        self.horarios = secciones_pendientes
        # print("\n--- Horario generado ---")
        # for s in self.horarios:
        #     if s.estado == "asignada":
        #         dia, hora = s.bloque
        #         print(f"{s.materia_codigo}-{s.seccion_num}). {s.materia_nombre}| {dia} {hora} | Prof: {s.profesor.nombre} {s.profesor.apellido} ({s.profesor.cedula}) | Salón {s.salon}")
        #     else:
        #         print(
        #             f"{s.materia_codigo}-{s.seccion_num}). {s.materia_nombre}| CERRADA (no se pudo asignar profesor)"
        #         )

        # Después de generar el horario, mostrar un menú para explorarlo
        self.menu_horario_generado()


def obtener_estado(self,prof,profesor_estado):
        if prof.cedula not in profesor_estado:
            profesor_estado[prof.cedula] = {"materias": set(), "bloques": set(), "profesor": prof}
        return profesor_estado[prof.cedula]

def profesores_para_materia(self,codigo_materia):
        resultado = []
        for prof in self.profesores:
            if codigo_materia in prof.materias:
                resultado.append(prof)
        return resultado

    # Intentar asignar una sección a un bloque
def asignar_seccion(self,seccion, bloque,bloque_asignaciones,profesor_estado):
        candidatos = []
        for prof in self.profesores_para_materia(seccion.materia_codigo):
            estado = self.obtener_estado(prof,profesor_estado)
            ya_dicte_esta_materia = seccion.materia_codigo in estado["materias"]
            carga_actual = len(estado["materias"])
            max_carga = int(prof.max_carga)
            # Ya está ocupado en ese bloque
            if bloque in estado["bloques"]:
                continue
            # Si no dicta esta materia y ya no tiene capacidad, no es candidato
            if not ya_dicte_esta_materia and carga_actual >= max_carga:
                continue
            candidatos.append((prof, estado, ya_dicte_esta_materia))
        if not candidatos:
            return False
        # Elegir el candidato con menor carga (y por apellido para determinismo)
        def orden(candidato):
            prof_cand, estado_cand, _ = candidato
            carga = len(estado_cand["materias"])
            apellido = prof_cand.apellido
            return (carga, apellido)

        candidatos.sort(key=orden)
        prof, estado, ya_dicte = candidatos[0]
        seccion.bloque = bloque
        seccion.profesor = prof
        seccion.estado = "asignada"
        seccion.salon = len(bloque_asignaciones[bloque]) + 1
        bloque_asignaciones[bloque].append(seccion)
        estado["bloques"].add(bloque)
        if not ya_dicte:
            estado["materias"].add(seccion.materia_codigo)
        return True

def menu_horario_generado(self):
        if not self.horarios:
            print("No hay un horario generado. Genere uno antes.")
            return

        dias = ["Lunes y Miércoles", "Martes y Jueves"]
        horarios = [
            "7:00 - 8:30",
            "8:45 - 10:15",
            "10:30 - 12:00",
            "12:15 - 1:45",
            "2:00 - 3:30",
            "3:45 - 5:15",
            "5:30 - 7:00",
        ]
        bloques = []
        for dia in dias:
            for hora in horarios:
                bloques.append((dia, hora))

        while True:
            opciones = [
                "Ver el horario de una materia",
                "Ver el horario de un profesor",
                "Ver salones asignados a una hora",
                "Guardar asignación de horarios en CSV",
                "Modificar asignación de horarios",
                "Volver al menú principal",
            ]
            eleccion = mostrar_elegir_opcion("Menú horario generado", opciones)

            if eleccion == "1":
                codigo = input("Ingrese el código de la materia: ").strip()
                encontrados = []
                for h in self.horarios:
                    if h.materia_codigo == codigo:
                        encontrados.append(h)
                if not encontrados:
                    print("No se encontró ninguna materia con ese código en el horario.")
                else:
                    for h in encontrados:
                        h.ver_datos()

            elif eleccion == "2":
                cedula = input("Ingrese la cédula del profesor: ").strip()
                try:
                    cedula_val = int(cedula)
                except Exception:
                    cedula_val = cedula
                encontrados = []
                for h in self.horarios:
                    if h.profesor and h.profesor.cedula == cedula_val:
                        encontrados.append(h)
                if not encontrados:
                    print("No se encontró ningún horario para ese profesor.")
                else:
                    for h in encontrados:
                        h.ver_datos()

            elif eleccion == "3":
                print("Seleccione un bloque:")
                for i, (dia, hora) in enumerate(bloques):
                    print(f"{i+1}. {dia} {hora}")
                opcion = input("Ingrese el número del bloque: ").strip()
                if not opcion.isdigit() or int(opcion) not in range(1, len(bloques) + 1):
                    print("Opción inválida.")
                    continue
                bloque = bloques[int(opcion) - 1]

                encontrados = []
                for h in self.horarios:
                    if h.bloque == bloque and h.estado == "asignada":
                        encontrados.append(h)

                if not encontrados:
                    print("No hay salones asignados a ese bloque.")
                else:
                    for h in encontrados:
                        print(f"Salón {h.salon}: {h.materia_codigo} (Sec {h.seccion_num}) - Prof: {h.profesor.nombre} {h.profesor.apellido}")

            elif eleccion == "4":
                nombre_archivo = input("Ingrese el nombre del archivo CSV (ej: horario.csv): ").strip()
                if not nombre_archivo:
                    nombre_archivo = "horario.csv"
                try:
                    with open(nombre_archivo, "w", encoding="utf-8", newline="") as f:
                        writer = csv.writer(f)
                        writer.writerow(["materia_codigo", "materia_nombre", "seccion", "dia", "hora", "prof_cedula", "prof_nombre", "prof_apellido", "salon", "estado"])
                        for h in self.horarios:
                            dia, hora = (h.bloque if h.bloque else ("", ""))
                            cedula = h.profesor.cedula if h.profesor else ""
                            nombre_prof = h.profesor.nombre if h.profesor else ""
                            apellido_prof = h.profesor.apellido if h.profesor else ""
                            writer.writerow([h.materia_codigo, h.materia_nombre, h.seccion_num, dia, hora, cedula, nombre_prof, apellido_prof, h.salon or "", h.estado])
                    print(f"Horario guardado en {nombre_archivo}.")
                except Exception as e:
                    print(f"No se pudo guardar el archivo: {e}")

            elif eleccion == "5":
                codigo = input("Ingrese el código de la materia para modificar su horario: ").strip()
                seccion = input("Ingrese el número de sección: ").strip()
                try:
                    seccion_num = int(seccion)
                except Exception:
                    print("Número de sección inválido.")
                    continue

                match = None
                for h in self.horarios:
                    if h.materia_codigo == codigo and h.seccion_num == seccion_num:
                        match = h
                        break

                if not match:
                    print("No se encontró esa sección en el horario.")
                    continue
                if match.estado != "asignada":
                    print("Esa sección no está asignada.")
                    continue

                profesores = self.profesores_para_materia(codigo)
                if not profesores:
                    print("No hay profesores que dicten esa materia.")
                    continue

                print("Profesores disponibles:")
                for i in range(len(profesores)):
                    p = profesores[i]
                    print(f"{i+1}. {p.nombre} {p.apellido} (C.I. {p.cedula})")
                elegido = input("Seleccione el número del profesor para re-asignar: ").strip()
                if not elegido.isdigit() or int(elegido) not in range(1, len(profesores) + 1):
                    print("Selección inválida.")
                    continue
                nuevo_prof = profesores[int(elegido) - 1]
                match.profesor = nuevo_prof
                print("Asignación modificada.")

            elif eleccion == "6":
                print("Volviendo al menú principal...")
                break

            def modificar_horarios(self):
             """
        Permite al usuario buscar una sección específica y cambiarle 
        manualmente el profesor asignado o el bloque horario.
        """
        if not self.horarios:
            print("No hay un horario generado. Por favor, genere o cargue uno primero.")
            return

        codigo = input("Ingrese el código de la materia: ").strip()
        seccion_input = input("Ingrese el número de sección: ").strip()

        try:
            seccion_num = int(seccion_input)
        except:
            print("Número de sección inválido.")
            return

        # Buscamos la sección en la lista de horarios generados
        seccion_encontrada = None
        for h in self.horarios:
            if h.materia_codigo == codigo and h.seccion_num == seccion_num:
                seccion_encontrada = h
                break

        if not seccion_encontrada:
            print("No se encontró esa sección en el sistema.")
            return

        # Mostrar estado actual de la sección
        prof_nombre = f"{seccion_encontrada.profesor.nombre} {seccion_encontrada.profesor.apellido}" if seccion_encontrada.profesor else "Sin asignar"
        bloque_str = f"{seccion_encontrada.bloque[0]} {seccion_encontrada.bloque[1]}" if seccion_encontrada.bloque else "Sin asignar"
        
        print(f"\n--- Editando: {seccion_encontrada.materia_nombre} (Sección {seccion_encontrada.seccion_num}) ---")
        print(f"Profesor actual: {prof_nombre}")
        print(f"Horario actual: {bloque_str}")

        opciones = ["Cambiar Profesor", "Cambiar Bloque Horario", "Volver"]
        eleccion = mostrar_elegir_opcion("¿Qué desea modificar?", opciones)

        if eleccion == "1":
            # Lógica para cambiar profesor
            candidatos = self.profesores_para_materia(codigo)
            if not candidatos:
                print("No existen otros profesores registrados para esta materia.")
            else:
                print("\nProfesores aptos para esta materia:")
                for i, p in enumerate(candidatos):
                    print(f"{i+1}. {p.nombre} {p.apellido} (CI: {p.cedula})")
                
                sel = input("Seleccione el número del nuevo profesor: ")
                if sel.isdigit() and 1 <= int(sel) <= len(candidatos):
                    seccion_encontrada.profesor = candidatos[int(sel)-1]
                    seccion_encontrada.estado = "asignada"
                    print("¡Profesor actualizado con éxito!")
                else:
                    print("Selección inválida.")

        elif eleccion == "2":
            # Lógica para cambiar bloque (Incluye los 7 bloques reglamentarios)
            dias = ["Lunes y Miércoles", "Martes y Jueves"]
            horas = [
                "7:00 - 8:30", "8:45 - 10:15", "10:30 - 12:00", 
                "12:15 - 1:45", "2:00 - 3:30", "3:45 - 5:15", "5:30 - 7:00"
            ]
            
            bloques_posibles = []
            for d in dias:
                for h in horas:
                    bloques_posibles.append((d, h))
            
            print("\nBloques horarios disponibles:")
            for i, b in enumerate(bloques_posibles):
                print(f"{i+1}. {b[0]} {b[1]}")
            
            sel = input("Seleccione el número del nuevo bloque: ")
            if sel.isdigit() and 1 <= int(sel) <= len(bloques_posibles):
                seccion_encontrada.bloque = bloques_posibles[int(sel)-1]
                seccion_encontrada.estado = "asignada"
                print("¡Bloque horario actualizado con éxito!")
            else:
                print("Selección inválida.")

                if __name__ == "__main__":
                    app = Sistema()
            app.menu_principal()