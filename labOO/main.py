# Elaborado por: Xavier Céspedes Alvarado y Luis GUillermo Alfaro Chacón
# Fecha de creación: 21/05/2025
# Última modificación: $$$
# Versión: 3.13.3

#Importación de librerías
import re
import random
from funciones import *
from clasePersona import*

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
                raise TypeError
            for i in lista:
                cedulas.append(i.getCedula())
            if cedula not in cedulas:
                raise ValueError
            objeto=lista[cedulas.index(cedula)]
            break
        except ValueError:
            print("La cédula ingresada no se encuentra registrada.\n")
        except TypeError:
            print("Formato incorrecto.\nLa cedula debe de iniciar distinto a 0 y tener una longitud de 9.\n")
    while True:
        try:
            nombre=tuple(input("Ingrese el nuevo nombre con sus dos apellidos: ").split())
            if len(nombre)!=3:
                raise ValueError
            break
        except:
            print("Debe ingresar un nombre con dos apellidos.\n")
    if confirmar()==True:
        modificar(objeto,nombre,1)
        return print("El nombre fue modificado\n")
    return print("La acción fue cancelada y el nombre no se modificó.\n")

def eliminarAux(lista):
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
            cedula=input("Ingrese la cédula del miembro que desea eliminar: ")
            if not re.match(r"[1-9]\d{8}$",cedula):
                raise TypeError
            for i in lista:
                cedulas.append(i.getCedula())
            if cedula not in cedulas:
                raise ValueError
            objeto=lista[cedulas.index(cedula)]
            if objeto.getEstado()==True:
                if confirmar()==True:
                    modificar(objeto,False,2)
                    return print("El miembro fue eliminado.\n")
            else:
                return print("Esta en estado inactivo.\n")
            break
        except ValueError:
            print("La cédula ingresada no se encuentra registrada.\n")
        except TypeError:
            print("Formato incorrecto.\nLa cedula debe de iniciar distinto a 0 y tener una longitud de 9.\n")
    return "La acción fue cancelada y el miembro no se eliminó.\n"

def insertarMiembro(lista,archivo):
    """
    Funcionamiento:
    - Se le pide al ususario la cantidad de miembros de trabajo, para crearlos ficticiamente.
    - Se crea la cantidad de personas indicada.
    Entradas:
    - lista(list): Es la lista que contiene todos los objetos.
    - archivo(str): Es el nombre del archivo donde se guarda la lista.
    Salidas:
    - Retorna un mensaje indicando que se agregaron crearon exitosamente.
    """
    lstCed=[]
    lstTrabajos=["Software Developer","Analyst","Engineer","Game designer","Web designer","Designer","Game programmer","Webmaster",
                "Web developer","Network administrator","Software Engineer","Scientist","Video game developer","Data Engineer",
                "Strategist","Web Application Developer","Java Developer"]
    while True:
        try:
            cantMiembros=int(input("Ingrese la cantidad de personas en el equiopo de trabajo: "))
            if cantMiembros<=0:
                raise TypeError
            break
        except ValueError:
            print("Debe ingresar un valor númerico\n")
        except TypeError:
            print("Debe ingresar un valor mayor a 0\n")
    for i in range(cantMiembros):
        miembro=Persona()
        nombre=crearNombres()
        cedula=random.randint(100000000,999999999)
        if cedula in lstCed:
            while cedula in lstCed:
                cedula=random.randint(100000000,999999999)
        lstCed.append(cedula)
        categoria=random.randint(1,4)
        perso=random.randint(1,4)
        trab=random.randint(0,len(lstTrabajos)-1)
        persoDefini=determinarPerso(categoria,perso)

        miembro.setNombre(nombre)
        miembro.setCedula(str(cedula))
        miembro.setCategoria([categoria,persoDefini])
        miembro.setProfesion(lstTrabajos[trab])
        miembro.setEstado(random.choice([True,False]))
        annadir(miembro,lista,archivo)
    print("Los miembros se crearon exitosamente.")
    return lista 

def categorias(lista):
    while True:
        try:
            opcion=0
            while opcion!=5:
                opcion=int(input("1) Analistas.\n2) Diplomáticos.\n3) Centinelas.\n" \
                                "4) Exploradores.\n5) Salir.\nOpcion: "))
                if opcion==1:
                    for i in lista:
                        if i.getCategoria()[0] == 1 and i.getEstado()==True:
                            print(i.getDatos())
                elif opcion==2:
                    for i in lista:
                        if i.getCategoria()[0] == 2 and i.getEstado()==True:
                            print(i.getDatos())
                elif opcion==3:
                    for i in lista:
                        if i.getCategoria()[0] == 3 and i.getEstado()==True:
                            print(i.getDatos())
                elif opcion==4:
                    for i in lista:
                        if i.getCategoria()[0] == 4 and i.getEstado()==True:
                            print(i.getDatos())
                elif opcion==5:
                    break
                else:
                    ValueError
            break
        except ValueError:
            print("Debe ingresar una opción valida.")

def subMenu(lista):
    while True:
        try:
            opcion=0
            while opcion!=5:
                opcion=int(input("1) Información general.\n2) Información por categoría.\n3) Información por cédula.\n" \
                                "4) Salir.\nOpcion: "))
                if opcion==2:
                    categorias(lista)
        except ValueError:
            print("Debe ingresar una opción valida.")

def menu(lista):
    while True:
        try:
            verificarBase("baseDeDatos")
            opcion=0
            while opcion!=5:
                opcion=int(input("1) Ingresar miembros.\n2) Modificar miembro.\n3) Eliminar miembro.\n" \
                                "4) Reportes.\n5) Salir.\nOpcion: "))
                print("")
                if opcion==1:
                    lista=insertarMiembro(lista,"baseDeDatos")
                elif opcion==2:
                    modificarNombreAux(lista)
                elif opcion ==3:
                    eliminarAux(lista)
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