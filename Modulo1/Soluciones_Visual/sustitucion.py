#introduciomos el texto a cifrar

texto = input ("Ingrese texto a cifrar:" )

if texto==texto.upper() : #para mayusculas
    abc="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
else:
    abc="abcdefghijklmnñopqrstuvwxyz" #para minusculas

d= int(input("Valor de desplazamiento: "))
cifrado= ""

#realizamos cifrado

for a in texto:
    if a in abc:
        cifrado += abc [(abc.index(a)+d)%(len(abc))]
    else:
        cifrado+=a

#VISUALIZAMOS TEXTO CIFRADO
print ("texto cifrado: ", cifrado)