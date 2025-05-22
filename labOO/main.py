# Elaborado por: Xavier Céspedes Alvarado y Luis GUillermo Alfaro Chacón
# Fecha de creación: 21/05/2025
# Última modificación: $$$
# Versión: 3.13.3

#Importación de librerías
import re
from funciones import *

#Definición de funciones
def modificarNombreAux(lista):
    """
    Funcionamiento:
    - Valida el nombre y la cédula del miembro que se requiere modificar.
    Entradas:
    - lista(list): Es la lista que contiene todos los objetos.
    Salidas:
    - Llama a la función principal y retorna un str según corresponda.
    """
    cedulas=[]
    while True:
        try:
            cedula=input("Ingrese la cédula del miembro que desea modificar: ")
            if not re.match(r"[1-9]\d{8}$",cedula):
                raise ValueError
            for i in lista:
                cedulas.append(i.getCedula())
            if cedula not in cedulas:
                raise ValueError
            objeto=lista[cedulas.index(cedula)]
            break
        except ValueError:
            print("La cédula ingresada no se encuentra registrada.")
    while True:
        try:
            nombre=tuple(input("Ingrese el nuevo nombre con sus dos apellidos: ").split())
            if len(nombre)!=3:
                raise ValueError
            break
        except:
            print("Debe ingresar un nombre con dos apellidos.")
    if confirmar()==True:
        modificarNombre(objeto,nombre)
        return "El nombre fue modificado"
    return "La acción fue cancelada y el nombre no se modificó."