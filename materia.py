# Fiorella Rodriguez y Veronica Gonzalez

class Materia():
     """
    Clase que representa una asignatura del pensum de Ingeniería.
    """
def __init__(self, codigo, nombre, secciones):
        """
        Inicializa una materia con su requerimiento de secciones.
        :param codigo: Código alfanumérico único de la materia.
        :param nombre: Título de la asignatura.
        :param secciones: Número de secciones que deben abrirse en el trimestre.
        """
        self.codigo = codigo
        self.nombre = nombre
        self.secciones = secciones
        
def ver_datos(self):
        print(f"Código: {self.codigo}")
        print(f"Nombre: {self.nombre}")
        print(f"Secciones: {self.secciones}")