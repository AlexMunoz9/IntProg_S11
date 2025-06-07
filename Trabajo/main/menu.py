import models.classes as c
import dao.functions as f

estudiantes = f.InfoDao()

def menu():
    print("""
          1. Agregar Datos
          2. Mostrar Datos
          3. Actualizar Datos
          6. Salir
          Digite una opcion: """)
    
def main():
    while True:
        menu()
        opcion = input()
        
        if opcion == '1':
            nombres = input("Ingrese los nombres del estudiante: ")
            apellidos = input("Ingrese el apellidos del estudiante: ")
            año = int(input("Ingresar año en que cursa el estudiante: "))
            carrera = input("Ingrese la carrera del estudiante: ")
            promedio = float(input("Ingrese el promedio del estudiante: "))
            estudiante = c.estudiante(nombres, apellidos , año , carrera , promedio)
            estudiantes.add(estudiante)
        
        elif opcion == '2':
            print("Informacion")
            estudiantes.show()
        
        elif opcion == '6':
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")