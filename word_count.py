#
# Escriba la función load_input que recive como parámetro un folder y retorna
# una lista de tuplas donde el primer elemento de cada tupla es el nombre del
# archivo y el segundo es una línea del archivo. La función convierte a tuplas
# todas las lineas de cada uno de los archivos. La función es genérica y debe
# leer todos los archivos de folder entregado como parámetro.
#
# Por ejemplo:
#   [
#     ('text0'.txt', 'Analytics is the discovery, inter ...'),
#     ('text0'.txt', 'in data. Especially valuable in ar...').
#     ...
#     ('text2.txt'. 'hypotheses.')
#   ]
#
import glob # permite leer contenido de directorios
import fileinput # permite iterar y operar en archivos 


def load_input(input_directory):
    sequence=[] # lista vacia 
    filenames = glob.glob(input_directory + "/*") # lee el contenido del directorio
    print(filenames)

    with fileinput.input (files=(filenames)) as f: # abre los archivos y con el with cierra los archivos
        for line in f:
            sequence.append((fileinput.filename(),line))# concatena el nombre del archivo y su linea correspondiente en una tupla

    return sequence
filenames=load_input("input") # el "input" es la dirreccion donde se encuentran los archivos files
print(filenames)









#
# Escriba una función llamada maper que recibe una lista de tuplas de la
# función anterior y retorna una lista de tuplas (clave, valor). En este caso,
# la clave es cada palabra y el valor es 1, puesto que se está realizando un
# conteo.
#
#   [
#     ('Analytics', 1),
#     ('is', 1),
#     ...
#   ]
#

def mapper(sequence):
    new_sequence=[] # lista vacia
    for _, text in sequence: # raya el piso sirve para que deje el ultimo valor de la dupla 
        words=text.split() # separa las palabras y quedan alojadas  en una lista 
        for word in words:
            word=word.replace(",","")
            word=word.lower()
            new_sequence.append((word,1))# aloja la dupla en una lista, en este caso la palabra y el numero 1
    return new_sequence
filenames=load_input("input")
filenames=mapper(filenames)

#print(filenames)





#
# Escriba la función shuffle_and_sort que recibe la lista de tuplas entregada
# por el mapper, y retorna una lista con el mismo contenido ordenado por la
# clave.
#
#   [
#     ('Analytics', 1),
#     ('Analytics', 1),
#     ...
#   ]
#
def shuffle_and_sort(sequence):
    sorted_sequence=sorted(sequence, key=lambda x: x[0])
    return sorted_sequence

#print(sequence)


#
# Escriba la función reducer, la cual recibe el resultado de shuffle_and_sort y
# reduce los valores asociados a cada clave sumandolos. Como resultado, por
# ejemplo, la reducción indica cuantas veces aparece la palabra analytics en el
# texto.
#
# def reducer(sequence):
#     diccionario={}
#     for key,value in sequence:
#         if key not in diccionario.keys():
#             diccionario[key]=[]
#         diccionario[key].append(value)
#     new_sequence=[]
#     for key, value in diccionario.items():
#         tupla=(key,sum(value))
#         new_sequence.append(tupla)
#     return new_sequence

def reducer(sequence):
    diccionario={}
    for key,value in sequence:
        if key not in diccionario.keys():
            diccionario[key]=[]
        diccionario[key].append(value)
    new_sequence=[]
    for key, value in diccionario.items():
        tupla=(key,sum(value))
        new_sequence.append(tupla)
    return new_sequence
        




#
# Escriba la función create_ouptput_directory que recibe un nombre de directorio
# y lo crea. Si el directorio existe, la función falla.
#
# def create_ouptput_directory(output_directory):
#     pass

# import os #proporciona una interfaz para interactuar con el sistema operativo

# def create_output_directory(output_directory):
#     try:
#         os.mkdir(output_directory)# crea el directorio
#         print(f"Directorio '{output_directory}' creado exitosamente.")
#     except FileExistsError:
#         print(f"Error: El directorio '{output_directory}' ya existe.")
#         raise

# directory_name = "output_directory"
# create_output_directory(directory_name)

import os.path

def create_output_directory(output_directory):
    
    if os.path.exists(output_directory):
        raise FileExistsError(f"The directory '{output_directory} 'alredy exists.")
    os.makedirs(output_directory)




#
# Escriba la función save_output, la cual almacena en un archivo de texto llamado
# part-00000 el resultado del reducer. El archivo debe ser guardado en el
# directorio entregado como parámetro, y que se creo en el paso anterior.
# Adicionalmente, el archivo debe contener una tupla por línea, donde el primer
# elemento es la clave y el segundo el valor. Los elementos de la tupla están
# separados por un tabulador.
#
# def save_output(output_directory, sequence):
#     pass
def save_output(output_directory, sequence):
    with open(output_directory + "/part-0000", "w") as file:
        for key, value in sequence:
            file.write(f"{key}\t{value}\n")
   
   

# import os
# def save_output(output_directory, reduced_result):
#     output_file_path = os.path.join(output_directory, "part-00000") # crea el archivo
#     with open(output_file_path, "w") as output_file:
#         for key, value in reduced_result.items():
#             output_line = f"{key}\t{value}\n" 
#             output_file.write(output_line)

# Ejemplo de uso:
# sequence= load_input("input")

# sequence=mapper(sequence)
# sequence= shuffle_and_sort(sequence)

# reduced_result = reducer(sequence)
# output_directory = "output_directory"
# save_output(output_directory, reduced_result)
            



#
# La siguiente función crea un archivo llamado _SUCCESS en el directorio
# entregado como parámetro.
#

def create_market(output_directory):
    with open(output_directory + "/ -SUCCES","w") as file:
        file.write("")


#
# Escriba la función job, la cual orquesta las funciones anteriores.
#
def job(input_directory, output_directory):
    
    sequence = load_input(input_directory)
    sequence = mapper(sequence)
    sequence = shuffle_and_sort(sequence)
    sequence = reducer(sequence)
    create_output_directory(output_directory)
    save_output(output_directory, sequence)
    create_market(output_directory)

if __name__ == "__main__":
    job(
        "input",
        "output",
    )
