class Seccion():
    def __init__(self, codigo_seccion, profesor, bloque, salon):
        self.codigo = codigo_seccion
        self.profesor = profesor
        self.bloque = bloque
        self.salon = salon
        
    def ver_datos(self):
        print(f"Código seccion: {self.codigo}")
        print(f"Profesor: {self.profesor}")
        print(f"Bloque: {self.bloque}")
        print(f"Salon: {self.salon}")