# Elaborado por: Xavier Céspedes Alvarado y Luis GUillermo Alfaro Chacón
# Fecha de creación: 21/05/2025
# Última modificación: $$$
# Versión: 3.13.3

#Importación de librerías
from archivos import *
import re
import names
import random
# import clasePersona

#Definición de funciones
def verificarBase(archivo):
    """
    Funcionamiento:
    - Verifica que la base de datos exista, y si no existe la crea.
    Entradas:
    - archivo(str): Es el nombre del archivo de la base de datos.
    Salidas:
    - Si la base existe retorna un str vacío, y si la crea retorna un string explicando.
    """
    try:
        base=open(archivo,"rb")
        base.close
    except:
        grabar([],archivo)
        return "La base de datos ha sido creada."
    return ""

def annadir(objeto,lista,archivo):
    """
    Funcionamiento:
    - Añade un objeto a la base de datos.
    Entradas:
    - objeto(): El el objeto que se añade a la lista.
    - lista(list): Es la lista que contiene todos los objetos.
    - archivo(str): Es el nombre del archivo donde se guarda la lista.
    Salidas:
    - Retorna la lista actualizada.
    """
    lista.append(objeto)
    grabar(lista,archivo)
    return lista

def confirmar():
    """
    Funcionamiento:
    - Permite al usuario confirmar la acción.
    Entradas:
    - N/A
    Salidas:
    - Retorna True o False dependiendo de la confirmación.
    """
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

def crearNombres():
    """
    Funcionamiento:
    Se crean nombres de manera aleatoria, gracias a la libreia names y random, donde se le asigna un genero al nombre,
    y se crea el nombre dependiendo del genero dado. Luego la informacion se almacena por separado.
    Entradas:
    N/A
    Salidas:
    Se retorna una lista con una tupla que contiene el nombre y los apellidos, y el genero por aparte, este de manera Booleana
    """
    genero=random.choice(("male","female"))             # Se pide que escoja un genero para que cree los nombres basados a este género.
    persona=names.get_first_name(gender=genero)         # Se crea el nombre.
    primerApe=names.get_last_name()                     
    segundoApe=names.get_last_name()                    # Se crean los 2 apellidos
    return(persona, primerApe, segundoApe)

def determinarPerso(pcate,pperso):
    """
    Funcionamiento:
    - Determina la personalidad de cada persona.
    Entradas:
    - pcate(int): contiene el valor de la categoria de la personalidad.
    - pperso(int): contiene el valor de la personalida de la persona.
    Salidas:
    - Se retorna la personalidad correspondiente.
    """
    lstAnalist=["ar","ló","co","in"]
    lstDiploma=["ab","me","pr","ac"]
    lstCentine=["lo","de","ej","có"]
    lstExplora=["vi","av","em","an"]
    if pcate==1:
        return lstAnalist[pperso-1]
    elif pcate==2:
        return lstDiploma[pperso-1]
    elif pcate==3:
        return lstCentine[pperso-1]
    else:
        return lstExplora[pperso-1]

def modificar(objeto,datoNuevo,opcion):
    """
    Funcionamiento:
    - Modifica el atributo de un objeto.
    Entradas:
    - objeto(): Es el objeto al que se le modifica un atributo.
    - datoNuevo(str o bool): Es el nuevo dato que se le da al atributo del objeto.
    - opcion(int): Es el atributo que se le modifica al objeto. 1=Nombre y 2=Estado.
    Salidas:
    - Cambia el atributo y retorna un str vacío.
    """
    if opcion==1:
        objeto.setNombre(datoNuevo)
    else:
        objeto.setEstado(datoNuevo)
    return ""