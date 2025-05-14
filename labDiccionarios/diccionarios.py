#Elaborado por: Xavier Céspedes Alvarado y Luis Guillermo Alfaro
#Fecha de creación: 13/05/2025
#Última modificación: 13/05/2025
#Versión: 3.13.3

#Importación de librerías
from funcionesLabDiccionarios import *

#Definición de funciones
def verificarBase(archivo):
    """
    Funcionamiento:
    - Verifica la existencia de la base de datos, si no existe la crea.
    Entradas:
    - archivo(str): Es el archivo que contiene la base de datos de deportes.
    Salidas:
    - Llama a la función menu.
    """
    try:
        leer(archivo)
    except FileNotFoundError:
        diccionario={}
        grabar(diccionario,archivo)
    return menu(archivo)

def menu(archivo):
    """
    Funcionamiento:
    - Solicita al usuario la opción que requiere realizar.
    Entradas:
    - archivo(str): Es el archivo que contiene la base de datos de deportes.
    Salidas:
    - Realiza la opción y vuelve al menú, si el usuario selecciona la opción de salir, sale del programa y lo indica.
    """
    while True:
        try:
            x=0
            while x!=5:
                print("1. Registrar deporte.\n" \
                "2. Modificar deporte.\n" \
                "3. Eliminar deporte.\n" \
                "4. Buscar por.\n" \
                "5. Salir")
                x=int(input("Opción:\n"))
                if x == 1:
                    registrarDeporte(archivo)
                elif x == 2:
                    modificarDeporte(archivo)
                elif x == 3:
                    eliminarDeporte(archivo)
                elif x == 4:
                    subMenu(archivo)
                elif x == 5:
                    return "Saliendo. . ."
                else:
                    raise TypeError
        except TypeError:
            print("Debe indicar una opción válida.")

#Código principal
archivo="baseDeDatosDeportes"
print(verificarBase(archivo))