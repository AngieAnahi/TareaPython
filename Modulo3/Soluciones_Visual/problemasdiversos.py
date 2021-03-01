def cantidad():
    n=int(input("Ingrese cantidad de alumnos:"))
    print (n)
    return n

def nota():
    nota = float(input("Introduce la nota(0 - 10): "))
    return nota

def validar_nota(nota):
    try:
        c=nota()
        if c >=0 and c <= 10:
            return c  # Importante romper la iteración si todo ha salido bien
        else:
            print('nota fuera del rango')
            print("Ingrese nota nuevamente:")
            na = float(input("Introduce la nota(0 - 10): "))
            return na

    except:
        print("Ha ocurrido un error, introduce bien la nota")

def ingresar_alumnos(n):
    promedio=0
    aprobados=0
    desaprobados=0
    total = 0
    lista_alumnos = []
    lista =[]
    for i in range (n):
        alumno ={}
        nom = input("Ingrese el nombre del alumno {}:".format(i+1))
        alumno['nombre']=nom
        alumno['nota1']=validar_nota(nota)
        alumno['nota2']=validar_nota(nota)
        alumno['nota3']=validar_nota(nota)
        alumno['prom']=round(((alumno['nota1']+alumno['nota2']+alumno['nota3'])/3),2)
        promedio = alumno['prom']
        dato = str(promedio) + ", corresponde al alumno: " + nom
        if promedio>=4:
            alumno['estado']="aprobado"
            aprobados+=1
            total+=promedio
        else:
            alumno['estado']="desaprobado"
            desaprobados+=1
            total+=promedio
            # agregando alumno a lista alumnos
        lista_alumnos.append(alumno)
        lista.append(dato)
    print(lista_alumnos)
    return (aprobados,desaprobados,total,n,lista)
    
def imprimir(x,y,z,n,lista):
    prom_cur=round(float(z/n),2)
    print ("La cantidad de aprobados son: {} \nLa cantidad de desaprobados son: {} \nEl promedio total del curso es: {} ".format(x,y,prom_cur))
    return lista
    
def promedios (lista):
    lista.sort() #se ordena la lista
    print('El Máximo Promedio es:',lista[-1])
    print('El Mínimo Promedio es:',lista[0])

print ("Modulo 3 \nProblemas diversos \nEjercicio1:")
n=cantidad()
aprobados,desaprobados,total,n,lista=ingresar_alumnos(n)
print ("Modulo 3 \nProblemas diversos \nEjercicio2 y Ejercicio 3:")
lista=imprimir(aprobados,desaprobados,total,n,lista)
print ("Modulo 3 \nProblemas diversos \nEjercicio 4:")
promedios (lista)