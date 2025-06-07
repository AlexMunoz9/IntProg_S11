class estudiante:
    def __init__(self, nombres, apellidos , año , carrera, promedio):
        self.nombres = nombres
        self.apellidos = apellidos
        self.año = año
        self.carrera = carrera
        self.promedio = promedio

    def __str__(self):
        return f"Nombres={self.nombres}, apellidos={self.apellidos} año={self.año}, carrera={self.carrera}, promedio={self.promedio})" 