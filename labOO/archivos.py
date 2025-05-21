# Elaborado por: Xavier Céspedes Alvarado y Luis GUillermo Alfaro Chacón
# Fecha de creación: 21/05/2025
# Última modificación: $$$
# Versión: 3.13.3

#Importación de librerías
import pickle 

#Definición de funciones
def leer(archivo):
    """
    Funcionamiento:
    - Lee el diccionario con la informacion de los pokemones que se encuentra en el archivo.
    Entradas: 
    - archivo(str): Es el archivo que contiene el diccionario con la información de los pokemones.
    Salidas:
    - Retorna el diccionario.
    """
    base=open(archivo,"rb")
    dicc=pickle.load(base)
    base.close()
    return dicc

def grabar(dicc,archivo):
    """
    Funcionamiento:
    - Graba el diccionario actualizado en el archivo.
    Entradas:
    - dicc(dict): Es el diccionario a grabar.
    - archivo(str): Es el archivo que contiene el diccionario con la información de los pokemones.
    Salidas:
    - Graba el diccionario en el archivo y retorna un string vacío.
    """
    base=open(archivo,"wb")
    pickle.dump(dicc,base)
    base.close()
    return ""