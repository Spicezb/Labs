# Elaborado por: Xavier Céspedes Alvarado y Luis GUillermo Alfaro Chacón
# Fecha de creación: 28/05/2025 14:32
# Última modificación: 29/05/2025 22:20
# Versión: 3.13.3
import pickle

def leer(archivo):
    """
    Funcionamiento:
    - Lee el archivo de la base de datos.
    Entradas:
    - archivo(str): Es el nombre del archivo que contiene la base de datos.
    Salidas:
    - Retorna la información leída.
    """
    base=open(archivo,"rb")
    herramientas=pickle.load(base)
    return herramientas

def grabar(datos,archivo):
    """
    Funcionamiento:
    - Graba los datos en el archivo.
    Entradas:
    - archivo(str): Es el nombre del archivo que contiene la base de datos.
    - datos(list): Son los datos a guardar.
    Salidas:
    - Guarda los datos y retorna un str vacío.
    """
    base=open(archivo,"wb")
    pickle.dump(datos,base)
    base.close
    return ""