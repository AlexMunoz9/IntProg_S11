#sumar dos numeros
def sumar(num1, num2):
    return num1 + num2

n1= int(input("Ingrese un numero: "))
n2= int(input("Ingrese otro numero: "))
suma = sumar(n1, n2)
print(f"{n1} + {n2} = {suma}")