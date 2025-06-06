import models.classes as c
import dao.functions as f

productos = f.ProductDao()

def menu():
    print("""
          1. Agregar
          2. Mostrar
          3. Actualizar
          6. Salir
          Digite una opcion: """)
    

def main():
    while(True):
        menu()
        option = input()
        if option == '1':
            nombre = input("Nombre del producto: ")
            precio = float(input("precio: "))
            existencia = int(input("existencia: "))
            producto = c.Product(nombre, precio, existencia)
            productos.add(producto)
        elif option == '2':
            print("productos")
            productos.show()
        elif option == '6':
            print("Adios")
            False
            break
    
        else:
            print("Opcion no valida, intente de nuevo")
            continue


