import re

numero_tarjeta = list(input("Ingresar el número de tarjeta: "))


digito_control = numero_tarjeta.pop()

numero_tarjeta.reverse()

procesar_digitos = []

for index, digito in enumerate (numero_tarjeta):
    if index % 2 == 0:
        doble_digito = int(digito)*2
        if doble_digito > 9:
            doble_digito = doble_digito - 9
        procesar_digitos.append(doble_digito)
    else:
        procesar_digitos.append(int(digito))

total = int(digito_control) + sum(procesar_digitos)

if total % 10 == 0:
    print ("¡Numero de Tarjeta - Valido!")
    for example in numero_tarjeta:
        regex = r"^[3]"
        regex2 = r"^[4]"
        regex3 = r"^[5]"
    if re.match(regex, example):
        print("EL número de tarjeta es AMEX")
    elif re.match(regex2, example):
        print("EL número de tarjeta es VISA")
    elif re.match(regex3, example):
        print("EL número de tarjeta es MASTERCARD")
    
else: 
    print("¡ ¡Numero de Tarjeta - Invalido!")