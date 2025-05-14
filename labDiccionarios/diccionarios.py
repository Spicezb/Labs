#Elaborado por: Xavier Céspedes Alvarado y Luis Guillermo Alfaro
#Fecha de creación: 13/05/2025
#Última modificación: 13/05/2025
#Versión: 3.13.3

#Importación de librerías
from funciones import *

#Definición de funciones
def verificarBase(archivo):
    try:
        base=open(archivo,"rb")
        base.close
    except FileNotFoundError:
        diccionario={}
        graba(diccionario,archivo)
    return menu(archivo)

def menu(archivo):
    while True:
        try:
            x=0
            while x!=5:
                print("1. Registrar deporte.\n" \
                "2. Modificar deporte.\n" \
                "3. Eliminar deporte.\n" \
                "4. Buscar por.")
                x=int(input("Opción: "))
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
archivo="deportesTec"
print(menu(archivo))