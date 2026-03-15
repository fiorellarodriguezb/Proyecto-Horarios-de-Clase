class Profesor():
    def __init__(self, cedula, email, apellido, nombre, max_carga, materias):
        self.cedula = cedula
        self.email = email
        self.apellido = apellido
        self.nombre = nombre
        self.max_carga = max_carga
        self.materias = materias
        
    def ver_datos(self):
        print(f"    Cédula: {self.cedula}")
        print(f"    Email: {self.email}")
        print(f"    Apellido: {self.apellido}")
        print(f"    Nombre: {self.nombre}")
        print(f"    Max Carga: {self.max_carga}")
        print(f"    Materias: {self.materias}")