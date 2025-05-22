# Elaborado por: Xavier Céspedes Alvarado y Luis GUillermo Alfaro Chacón
# Fecha de creación: 21/05/2025
# Última modificación: $$$
# Versión: 3.13.3

#Importación de librerías
import re
import random
from funciones import *
from clasePersona import *

#Definición de funciones
def modificarNombreAux(lista):
    """
    Funcionamiento:
    - Valida el nuevo nombre y reemplaza el antiguo.
    Entradas:
    - lista(list): Es la lista que contiene todos los objetos.
    Salidas:
    - Llama a la función principal y retorna un str según corresponda.
    """
    objeto=obtenerCedula(lista)
    if objeto.getEstado()==False:
        return "No se puede modificar, pues el miembro no forma parte del equipo de trabajo."
    while True:
        try:
            nombre=tuple(input("Ingrese el nuevo nombre con sus dos apellidos: ").split())
            if len(nombre)!=3:
                raise ValueError("Debe ingresar un nombre con dos apellidos.\n")
            elif nombre==objeto.getNombre():
                raise ValueError("El nuevo nombre no puede ser igual al actual.\n")
            break
        except ValueError as e:
            print(e)
    if confirmar()==True:
        modificar(objeto,nombre,1)
        return "El nombre fue modificado"
    return "La acción fue cancelada y el nombre no se modificó."

def eliminarAux(lista):
    """
    Funcionamiento:
    - Valida el nombre y la cédula del miembro que se requiere modificar.
    Entradas:
    - lista(list): Es la lista que contiene todos los objetos.
    Salidas:
    - Llama a la función principal y retorna un str según corresponda.
    """
    objeto=obtenerCedula(lista)
    if objeto.getEstado()==True:
        if confirmar()==True:
            modificar(objeto,False,2)
            return "El miembro fue eliminado."
    else:
        return "Esta persona no forma parte del equipo de trabajo."
    return "La acción fue cancelada y el miembro no se eliminó."

def categorias(lista):
    """
    Funcionamiento:
    - Submenú de las categorías de la personalidad.
    Entradas:
    - lista(list): Es la lista que contiene todos los objetos.
    Salidas:
    - Retorna los miembros que pertenecen a la categoría correspondiente.
    """
    while True:
        try:
            conta=0
            opcion=0
            while opcion!=5:
                opcion=int(input("\n1) Analistas.\n2) Diplomáticos.\n3) Centinelas.\n" \
                                "4) Exploradores.\n5) Salir.\nOpcion: "))
                if opcion==1:
                    for i in lista:
                        if i.getCategoria()[0] == 1 and i.getEstado()==True:
                            print(i.getDatos())
                            conta+=1
                    if conta==0:
                        print("No hay ningún miembro en esta categoría.")
                    conta=0
                elif opcion==2:
                    for i in lista:
                        if i.getCategoria()[0] == 2 and i.getEstado()==True:
                            print(i.getDatos())
                            conta+=1
                    if conta==0:
                        print("No hay ningún miembro en esta categoría.")
                    conta=0
                elif opcion==3:
                    for i in lista:
                        if i.getCategoria()[0] == 3 and i.getEstado()==True:
                            print(i.getDatos())
                            conta+=1
                    if conta==0:
                        print("No hay ningún miembro en esta categoría.")
                    conta=0
                elif opcion==4:
                    for i in lista:
                        if i.getCategoria()[0] == 4 and i.getEstado()==True:
                            print(i.getDatos())
                            conta+=1
                    if conta==0:
                        print("No hay ningún miembro en esta categoría.")
                    conta=0
                elif opcion==5:
                    return ""
                else:
                    raise ValueError
        except ValueError:
            print("Debe ingresar una opción valida.")

def subMenu(lista):
    """
    Funcionamiento:
    - Submenú para mostrar la información en distintos formatos.
    Entradas:
    - lista(list): Es la lista que contiene todos los objetos.
    Salidas:
    - Retorna las funciones respectivas.
    """
    while True:
        try:
            opcion=0
            while opcion!=4:
                opcion=int(input("\n1) Información general.\n2) Información por categoría.\n3) Información por cédula.\n" \
                                "4) Salir.\nOpcion: "))
                if opcion==1:
                    reporteTotal(lista)
                elif opcion==2:
                    categorias(lista)
                elif opcion==3:
                    reporteCedula(lista)
                elif opcion == 4:
                    return ""
                else:
                    raise ValueError
        except ValueError:
            print("Debe ingresar una opción valida.")

def menu(lista):    
    """
    Funcionamiento:
    - Menú principal del programa.
    Entradas:
    - lista(list): Es la lista que contiene todos los objetos.
    Salidas:
    - Retorna la función correspondiente para cada acción.
    """
    while True:
        try:
            verificarBase("baseDeDatos")
            opcion=0
            while opcion!=5:
                opcion=int(input("\n1) Ingresar miembros.\n2) Modificar miembro.\n3) Eliminar miembro.\n" \
                                "4) Reportes.\n5) Salir.\nOpcion: "))
                if opcion==1:
                    lista=insertarMiembro(lista,"baseDeDatos")
                elif opcion==2:
                    print(modificarNombreAux(lista))
                elif opcion ==3:
                    print(eliminarAux(lista))
                elif opcion==4:
                    subMenu(lista)
                elif opcion==5:
                    grabar(lista,"baseDeDatos")
                    return print("Saliendo. . .")
                else:
                    raise ValueError
        except ValueError:
            print("Debe ingresar una opción valida.")

#Código principal
verificarBase("baseDeDatos")
lista=leer("baseDeDatos")
menu(lista)