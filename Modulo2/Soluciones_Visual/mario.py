print ("#Problema 1 - Mario:")
n=int(input("Ingrese un numero:"))
while n<=0 or n>=9:
    print("¡Ha escrito un fuera del rango! Inténtelo de nuevo")
    n = int(input("Escriba un número positivo: "))
for i in range (n+1):
        print(" " * (n-i) + "#" * i)
