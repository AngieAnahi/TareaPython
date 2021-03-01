from math import sqrt
print("Ejercicio 1 - Problemas diversos:")
m = float (input("Ingrese cantidad a ahorrar:"))
c = (m * 0.04)+m
c2 = (c * 0.04)+c
c3 = (c2 * 0.04)+c2
print ("La cantidad ahorrada en el 1er año es:", round (c,2))
print ("La cantidad ahorrada en el 2do año es:", round (c2,2))
print ("La cantidad ahorrada en el 3er año es:", round (c3,2))


print("----------------------------------------------")
print("Ejercicio 2 - Problemas diversos:")
A = int(input("Ingrese el coeficiente de la variable cuadrática\n"))
B = int(input("Ingrese el coeficiente de la variable lineal\n"))
C = int(input("Ingrese el término independiente\n"))
discriminante = (B**2)-(4*A*C)

if (discriminante) < 0:
    print ("El discriminante es:", discriminante)
    print("No tiene solución real")
else:
  print ("El discriminante es:", discriminante)
  x1 = (-B+sqrt(B**2-(4*A*C)))/(2*A)
  x2 = (-B-sqrt(B**2-(4*A*C)))/(2*A)
  print("Las soluciones de la ecuación son:")
  print(x1)
  print(x2)