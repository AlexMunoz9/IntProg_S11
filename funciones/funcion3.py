#Calcular el area de un circulo
""" Formula area = pi * r^2 """
import math

def area_circulo(radio):
    area = math.pi * (radio ** 2)
    return area

def main():
    radio = float(input("Ingrese el radio del circulo: "))
    area = area_circulo(radio)
    print(f"El area del circulo con radio {radio} es: {area:.2f}")


main()
