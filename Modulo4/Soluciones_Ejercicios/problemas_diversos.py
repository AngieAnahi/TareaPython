from modulo import datos
import re
print ("Ejercicio 1:")
n = int(input('Introduce un número entero entre 1 y 10: '))
file_name = 'tabla-' + str(n) + '.txt'
f = open(file_name, 'w')
for i in range(1, 11):
    f.write(str(n) + ' x ' + str(i) + ' = ' + str(n * i) + '\n')
f.close()
print ("Se creo el fichero del número: {}".format(n))

print ("----------------- \nEjercicio 2:")
n = int(input('Introduce un número entero entre 1 y 10: '))
file_name = 'tabla-' + str(n) + '.txt'
try: 
    f = open(file_name, 'r')
except FileNotFoundError:
    print('No existe el fichero con la tabla del', n)
else:
    print(f.read())

print ("----------------- \nEjercicio 3:")
path = './data/re/short_tweets.csv'
analisis_sentimientos = datos.read_pandas(path,780,782)
regex = r"\w+.txt"  # complete aqui
for tweet in analisis_sentimientos:
    print (re.findall(regex, tweet))

print ("----------------- \nEjercicio 4:")
# Escriba una expresión regular para validar un correo
regex = r"\w+[._]\w+[._]\w+@\w+.com" 
regex2 = r"\w+@\w+.com"

emails = ['n.john.smith@gmail.com', '87victory@hotmail.com', '!#mary-=@msca.net']
for example in emails:
    if re.match(regex, example):
        print("The email {email_example} is a valid email".format(email_example=example))
    elif re.match(regex2, example):
        print("The email {email_example} is a valid email".format(email_example=example))
    else:
        print("The email {email_example} is invalid".format(email_example=example))   
