class Horario:
   
    def __init__(self, materia_codigo, materia_nombre, seccion_num, bloque=None, profesor=None, salon=None, estado="pendiente"):
        self.materia_codigo = materia_codigo
        self.materia_nombre = materia_nombre
        self.seccion_num = seccion_num
        self.bloque = bloque  # (dia, hora)
        self.profesor = profesor
        self.salon = salon
        self.estado = estado

    def ver_datos(self):
        print(f"Materia: {self.materia_codigo} - {self.materia_nombre} (Sec {self.seccion_num})")
        print(f"Estado: {self.estado}")
        if self.estado == "asignada" and self.bloque is not None and self.profesor is not None:
            dia, hora = self.bloque
            print(f"  Bloque: {dia} {hora}")
            print(f"  Profesor: {self.profesor.nombre} {self.profesor.apellido} (C.I. {self.profesor.cedula})")
            print(f"  Salón: {self.salon}")
        elif self.estado == "cerrada":
            print("  No se ha asignado.")
        elif self.estado == "pendiente":
            print("  Pendiente de asignar profesor y bloque.")