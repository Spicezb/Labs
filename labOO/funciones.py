# Elaborado por: Xavier Céspedes Alvarado y Luis GUillermo Alfaro Chacón
# Fecha de creación: 21/05/2025
# Última modificación: $$$
# Versión: 3.13.3

#Importación de librerías
from archivos import *
import re
import names
import random
from clasePersona import *

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
            cantMiembros=int(input("Ingrese la cantidad de personas en el equipo de trabajo: "))
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

def reporteTotal(lista):
    """
    Funcionamiento:
    - Imprime los datos de cada objeto en la base de datos.
    Entradas:
    - lista(list): Es la lista que contiene los objetos.
    Salidas:
    - Imprime los datos de todos los objetos.
    """
    existeAlguno=False
    for i in lista:
        if i.getEstado()==True:
            existeAlguno=True
            print(f"\n{i.getDatos()}")
    if existeAlguno==False:
        return print("No hay ningún miembro en el equipo.")
    return ""

def obtenerCedula(lista):
    """
    Funcionamiento:
    - Verifica la cédula y retorna el objeto.
    Entradas:
    - lista(list): Es la lista que contiene los objetos.
    Salidas:
    - Retorna el objeto.
    """
    cedulas=[]
    cedulasActivas=False
    while True:
        try:
            for i in lista:
                cedulas.append(i.getCedula())
                if i.getEstado()==True:
                    cedulasActivas=True
            if cedulas==[] or cedulasActivas==False:
                return False
            cedula=input("\nIngrese la cédula del miembro: ")
            if not re.match(r"[1-9]\d{8}$",cedula):
                raise TypeError
            elif cedula not in cedulas:
                raise ValueError
            objeto=lista[cedulas.index(cedula)]
            return objeto
        except ValueError:
            print("La cédula ingresada no se encuentra registrada.\n")
        except TypeError:
            print("Formato incorrecto.\nLa cedula debe de iniciar distinto a 0 y tener una longitud de 9.\n")

def reporteCedula(lista):
    """
    Funcionamiento:
    - Imprime los datos del miembro con dicha cédula.
    Entradas:
    - lista(list): Es la lista que contiene los objetos.
    Salidas:
    - Imprime los datos del miembro.
    """
    objeto=obtenerCedula(lista)
    if objeto==False:
        return print("No hay ningún miembro en el equipo.")
    if objeto.getEstado()==False:
        return print("La persona no forma parte del equipo.")
    print(f"\n{objeto.getDatos()}")
    return ""