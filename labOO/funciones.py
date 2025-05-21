# Elaborado por: Xavier Céspedes Alvarado y Luis GUillermo Alfaro Chacón
# Fecha de creación: 21/05/2025
# Última modificación: $$$
# Versión: 3.13.3

#Importación de librerías
from archivos import *
# import clasePersona

#Definición de funciones

def verificarBase(archivo):
    try:
        base=open(archivo,"rb")
        base.close
    except:
        grabar([],archivo)
    return "La base de datos ha sido creada."

def annadir(objeto,lista,archivo):
    """
    Funcionamiento:
    - Añade un objeto a la base de datos.
    Entradas:
    - objeto()
    - lista(list): Es la lista que contiene todos los objetos.
    - archivo(str): Es el nombre del archivo donde se guarda la lista.
    Salidas:
    - Retorna la lista actualizada.
    """
    lista.append(objeto)
    grabar(lista,archivo)
    return lista

def confirmar():
    while True:
        try:
            confirmacion=input("1. Confirmar\n2. Cancelar\nDigite una opción: ")
            if confirmacion not in ("1","2"):
                raise ValueError
            break
        except ValueError:
            print("Debe escoger una de las opciones anteriores")
    if confirmacion=="1":
        return True
    else:
        return False

def modificarNombre(objeto,nombre):
    objeto.setNombre(nombre)
    return ""

# def modificarNombreAux(lista):
#     while True:
#         try:
#             cedula=input("Ingrese la cédula del miembro que desea modificar: ")
#             for i in lista:
#                 if i.getCedula==cedula:
#                     nombre=input("Ingrese el nuevo nombre: ")
#                     if confirmar()==True:
#                         modificarNombre(i,nombre)
#                         return
