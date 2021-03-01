#importa pandas
import pandas as pd

# Crea una Serie de los numeros 10, 20 and 10.
numeros=["10","20","10"]
print ("Primera Serie creada:\n", numeros)
# Crea una Serie con tres objetos: 'rojo', 'verde', 'azul'
colores=["rojo","verde","azul"]
print ("Segunda Serie creada:\n",colores)
# Crea un dataframe vacío llamado 'df'
df = pd.DataFrame()
# Crea una nueva columna en el dataframe, y asignale la primera serie que has creado
df['numeros'] = numeros
print ("Dataframe con primera serie\n",df)

# Crea otra columna en el dataframe y asignale la segunda Serie que has creado
df['colores'] = colores
print ("Dataframe con las dos series:\n",df)
# Lee el archivo llamado 'avengers.csv" localizado en la carpeta "data" y crea un DataFrame, llamado 'avengers'. 
# El archivo está localizado en "data/avengers.csv"
avengers = pd.read_csv("data/pandas/avengers.csv")
# Muestra las primeras 5 filas del DataFrame.
print ("las primeras 5 filas del DataFrame",avengers.head(5))
# Muestra las primeras 10 filas del DataFrame. 
print ("las primeras 10 filas del DataFrame",avengers.head(10))
# Muestra el tamaño del DataFrame
print ("El tamaño del DataFrame: ")
print (avengers.shape)
# Muestra los data types del dataframe
print ("Data types DataFrame: ")
print (avengers.dtypes)
# Cambia el indice a la columna "fecha_inicio".
print ("La columna 'fecha_inicio' es el indice: ")
df2 = avengers.set_index("fecha_inicio")
print (df2)
# Ordena el índice de forma descendiente
print ("Indice de forma descendiente")
by_year = df2.sort_values('fecha_inicio',ascending=False)
print (by_year)
# Resetea el índice
print ("Indice reseteado")
df2 = df2.reset_index(drop=True)
print (df2)
