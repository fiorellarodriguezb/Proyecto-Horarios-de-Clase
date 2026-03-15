
class Materia():
    def __init__(self, codigo, nombre, secciones):
        self.codigo = codigo
        self.nombre = nombre
        self.secciones = secciones
        
    def ver_datos(self):
        print(f"Código: {self.codigo}")
        print(f"Nombre: {self.nombre}")
        print(f"Secciones: {self.secciones}")