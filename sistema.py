import requests
from Materia import Materia
from Profesor import Profesor
from funciones import *


class Sistema():
    def __init__(self):
        self.codigos_materias = []
        self.materias_t1 = []
        self.materias_t2 = []
        self.materias_t3 = []
        self.profesores = []
    
    def prueba_csv(self):
              
        # Visualizacion de como podemos pasar todo a csv
              
        lista_para_csv = '['
        for materia in self.materias_t1:
            lista_para_csv += f"{materia.codigo},{materia.nombre} ;"
        lista_para_csv += ']'
        print(lista_para_csv)
    
    
    
        
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
                
                # Funcion por realizar
                
                self.menu_principal()
                break
            elif eleccion == "4":
                print("Saliendo del sistema...")
                break
    

    def cargar_datos_API(self,api_t1,api_t2,api_t3,api_profesores):
        
        opciones = ["Trimestre 1", "Trimestre 2", "Trimestre 3", "Todos los trimestres"]
        eleccion = mostrar_elegir_opcion("Cargando materias...", opciones)
       
        if eleccion == "1":
            self.cargar_materias_tn(api_t1,1)
        elif eleccion == "2":
            self.cargar_materias_tn(api_t2,2)
        elif eleccion == "3":
            self.cargar_materias_tn(api_t3,3)
        elif eleccion == "4":
            self.cargar_materias_tn(api_t1,1)
            self.cargar_materias_tn(api_t2,2)
            self.cargar_materias_tn(api_t3,3)

        # Cargar datos de profesores
        print("Cargando profesores...")
        respuesta = requests.get(api_profesores)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            for profesor in datos:
                cedula = profesor["Cedula"]
                email = profesor["Email"]
                apellido = profesor["Apellido"]
                nombre = profesor["Nombre"]
                max_carga = profesor["Max Carga"]
                materias = profesor["Materias"]

                nuevo_profesor = Profesor(cedula, email, apellido, nombre, max_carga, materias)
                
                self.profesores.append(nuevo_profesor)
                
                
        self.prueba_csv()   
             
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
    
    def cargar_datos_csv(self):
        # Función por realizar
        pass
                    
    def menu_principal(self):
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
                pass
            elif eleccion == "3":
                # Modulo generacion de horarios
                pass
            elif eleccion == "4":
                # Modulo modificacion de horarios
                pass
            elif eleccion == "5":
                # Modulo estadisticas
                pass
                
            elif eleccion == "6":
                print("Saliendo del sistema...")
                break
            
    def modulo_profesores(self):
        # Modulo profesores
        # Ver la lista de profesores 
        # Ver un profesor específico 
        # Agregar un profesor a la lista 
        # Eliminar un profesor de la lista 
        # Modificar la lista de materias de un profesor (agregar o quitar materias)      
        while True:
            titulo = '    ----- Módulo Profesores -----'
            opciones = ["Ver lista de profesores", "Ver un profesor específico", "Agregar un profesor a la lista", "Eliminar un profesor de la lista", "Modificar la lista de materias de un profesor", "Volver al menú principal"]

            eleccion = mostrar_elegir_opcion(titulo, opciones)

            if eleccion == "1":
                # Ver la lista de profesores 
                for profesor in self.profesores:
                    print(f"Profesor: {profesor.nombre} {profesor.apellido}")
            elif eleccion == "2":
                # Ver un profesor específico 
                pass
            elif eleccion == "3":
                # Agregar un profesor a la lista 
                pass
            elif eleccion == "4":
                # Eliminar un profesor de la lista 
                pass
            elif eleccion == "5":
                # Modificar la lista de materias de un profesor (agregar o quitar materias)  
                pass
            elif eleccion == "6":
                print("Volviendo al menú principal...")
                break
        
    def generar_horarios(self):
        # Función por realizar
        pass