import csv
from sys import argv
import re


class DnaTest(object):

    def __init__(self):
        # obtener el nombre de archivo de la línea de comandos sin los nombres de directorio "base de datos" y "secuencia"
        self.sequence_argv = str(argv[2][10:])
        self.database_argv = str(argv[1][10:])

        # Abrir y cerrar automáticamente el archivo de la base de datos "database"
        with open(f"data/dna/databases/{self.database_argv}", 'r') as database_file:
            self.database_file = database_file.readlines()

        # Abrir y cerrar automáticamente el archivo de secuencia "sequence"
        with open(f"data/dna/sequences/{self.sequence_argv}", 'r') as sequence_file:
            self.sequence_file = sequence_file.readline()

        #Leer archivo CSV como diccionario, función: compare_database_with_sequence()
        self.csv_database_dictionary = csv.DictReader(self.database_file)
        # Leer archivo CSV para tomar la primera fila, función: get_str_list()
        self.reader = csv.reader(self.database_file)
        # diccionario calculado del archivo de secuencia
        self.dict_from_sequence = {}
        self.select_max = {}

    # returns the first row of the CSV file  (database file)
    def get_str_list(self):
        # get first row from CSV file
        keys = next(self.reader)

        # eliminar 'nombre' de la lista, obtener STR solo.
        keys.remove("name")
        return keys

    # devuelve el diccionario de STR calculados del archivo de secuencia(key(STR): value(count))
    def get_str_count_from_sequence(self):  # PROBLEM HERE AND RETURN DICTIONARY FROM IT !
        for str_key in self.get_str_list():
            regex = rf"({str_key})+"
            matches = re.finditer(regex, self.sequence_file, re.MULTILINE)

            # my code
            for match in matches:
                match_len = len(match.group())
                key_len = len(str_key)
                self.select_max[match] = match_len
                #  seleccione el valor máximo del diccionario de resultados (select_max)
                max_values = max(self.select_max.values())

                if max_values >= key_len:
                    result = int(max_values / key_len)
                    self.select_max[str_key] = result
                    self.dict_from_sequence[str_key] = result

            # Borrar diccionario de comparación para seleccionar una nueva clave
            self.select_max.clear()

    # comparar el diccionario calculado con los diccionarios de la base de datos y obtener el nombre de la persona
    def compare_database_with_sequence(self):
        # función de comparación entre el diccionario de base de datos y el diccionario de secuencia calculada
        def dicts_equal(from_sequence, from_database):
            """ return True if all keys and values are the same """
            return all(k in from_database and int(from_sequence[k]) == int(from_database[k]) for k in from_sequence) \
                and all(k in from_sequence and int(from_sequence[k]) == int(from_database[k]) for k in from_database)

        def check_result():
            for dictionary in self.csv_database_dictionary:
                dict_from_database = dict(dictionary)
                dict_from_database.pop('name')

                if dicts_equal(self.dict_from_sequence, dict_from_database):
                    dict_from_database = dict(dictionary)
                    print(dict_from_database['name'])
                    return True

        if check_result():
            pass
        else:
            print("No match")


# ejecutar la clase y sus funciones (control de programa)
if __name__ == '__main__':
    RunTest = DnaTest()
    RunTest.get_str_count_from_sequence()
    RunTest.compare_database_with_sequence()