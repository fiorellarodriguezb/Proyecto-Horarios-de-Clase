# Fiorella Rodriguez y Veronica Gonzalez

class Profesor():
     """
    Clase que representa a un docente de la universidad.
    Contiene información personal, académica y de disponibilidad.
    """
def __init__(self, cedula, email, apellido, nombre, max_carga, materias):
        """
        Inicializa una instancia de Profesor.
        :param nombre: Nombre del docente.
        :param apellido: Apellido del docente.
        :param cedula: Documento de identidad.
        :param correo: Dirección de correo electrónico.
        :param materias: Lista de códigos de materias que puede dictar.
        :param max_carga: Cantidad máxima de secciones que puede asumir.
        """
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

