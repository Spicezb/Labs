#Elaborado por: Xavier Céspedes Alvarado y Luis Guillermo Alfaro
#Fecha de creación: 13/05/2025
#Última modificación: 13/05/2025
#Versión: 3.13.3

#Importación de librerías
import pickle
import re
import os

#Definición de funciones
def leer(archivo):
    """
    Funcionamiento:
    - Lee el diccionario en la base de datos.
    Entradas:
    - archivo(str): Es el archivo que contiene la base de datos de deportes.
    Salidas:
    - Retorna el diccionario que se encuentra en la base de datos.
    """
    base=open(archivo,"rb")
    dicc=pickle.load(base)
    base.close
    return dicc

def grabar(dicc,archivo):
    """
    Funcionamiento:
    - Graba los cambios realizados en la base de datos.
    Entradas:
    - archivo(str): Es el archivo que contiene la base de datos de deportes.
    - dicc(dict): Es el diccionario actualizado que se va a grabar en la base de datos.
    Salidas:
    - Graba los cambios y cierra el archivo.
    """
    base=open(archivo,"wb")
    pickle.dump(dicc,base)
    base.close
    return ""

def registrarDeporte(archivo):
    try:
        x=leer(archivo)
    except:
        grabar({},archivo)
        x=leer(archivo)
    regisDepor={}
    codDepo=input("Ingrese el codigo del deporte: ")
    nomDepo=input("Ingrese el nombre del deporte: ")
    ExpliDepo=input("Ingrese una expliación corta del deporte: ")
    lugarDepo=input("Ingrese el lugar donde se desarrolla: ")
    estaDepo=True
    x[codDepo]=[nomDepo,ExpliDepo,lugarDepo,estaDepo]
    grabar(x,archivo)

def elegirDeporte(dicc):
    """
    Funcionamiento:
    - Imprime las opciones de deportes activos para que el usuario seleccione el necesario.
    Entradas:
    - dicc(dict): Es el diccionario que contiene todos los deportes.
    Salidas:
    - Retorna el código del deporte elegido por el usuario.
    """
    activos=[]
    print()
    for i in dicc:
        if dicc[i][3]==True:
            activos.append(i)
            print(f"{i}: {dicc[i][0]}")
    while True:
        try:
            opcion=input("Seleccione un deporte ingresando su código:\n")
            if opcion not in activos:
                raise ValueError
            break
        except ValueError:
            print("\nDebe ingresar un código entre los mostrados anteriormente. Debe incluir las mayúsculas.\n")
    return opcion

def confirmar():  
    """
    Funcionamiento:
    - Solicita una confirmación al usuario para proceder con una acción que requiera de esta.
    Entradas:
    - N/A
    Salidas:
    - Retorna la decisión del usuario.
    """
    while True:
        try:
            confirmacion=input("\n¿Desea confirmar?:\n1. Confirmar\n2. Cancelar\nDigite una opción:\n")
            if confirmacion not in ("1","2"):
                raise ValueError
            break
        except ValueError:
            print("\nDebe ingresar una de las opciones anteriores.\n")
    return confirmacion

def eliminarDeporte(archivo):  
    """
    Funcionamiento:
    - Simula la eliminación de un deporte, pero en realidad este solo se oculta.
    Entradas:
    - archivo(str): Es el archivo que contiene la base de datos de deportes.
    Salidas:
    - En caso de que el deporte se elimine, lo indica, y si la acción fue cancelada también.
    """
    dicc=leer(archivo)
    elim=elegirDeporte(dicc)
    confirmacion=confirmar()
    if confirmacion=="1":
        dicc[elim][3]=False
        grabar(dicc,archivo)
        print("\nDeporte eliminado satisfactoriamente.\n")
    else:
        print("El deporte no se eliminó.\n")
    return ""

def modificarDeporte(archivo):
    """
    Funcionamiento:
    - Modifica el nombre de un deporte si el usuario lo solicita.
    Entradas:
    - archivo(str): Es el archivo que contiene la base de datos de deportes.
    Salidas:
    - Indica el cambio si este se realizó, y de lo contrario también indica la situación.
    """
    dicc=leer(archivo)
    modificar=elegirDeporte(dicc)
    original=dicc[modificar][0]
    while True:
        try:
            nuevo=input("Ingrese el nuevo nombre que desea darle al deporte:\n")
            if nuevo==original:
                raise ValueError
            break
        except ValueError:
            print("\nEl nuevo nombre debe ser distinto al anterior.\n")
    confirmacion=confirmar()
    if confirmacion == "1":
        dicc[modificar][0]=nuevo
        print(f"\nEl nombre del deporte ha sido cambiado.\nNombre anterior: {original}\nNuevo nombre: {nuevo}\n")
        grabar(dicc,archivo)
    else:
        print("El deporte no ha sido modificado.")
    return ""

def eliminados(archivo):
    conta=0
    lol=leer(archivo)
    for i in lol:
        x=lol.get(i)
        if x[2] == False:
            conta+=1
            os.system("cls")
            print(x)
            input("Presione enter para continuar.")
            os.system("cls")
    if conta==0:
        os.system("cls")
        print("No hay deportes eliminados")
        input("Presione enter para continuar.")
        os.system("cls")

def buscarLugar(archivo):
    lol=leer(archivo)
    lugar=input("Ingrese el lugar del deporte: ")
    os.system("cls")
    print(f"Resultados relacionados con '{lugar}'")
    for i in lol:
        x=lol.get(i)
        if re.search(lugar.lower(), x[2].lower()):
            for n in range(len(x)-1):
                print(x[n])
                if x[-1]==True:
                    print("Estado Activo")
                else:
                    print("Estado Inactivo")
            print("")
    input("Presione enter para continuar.")
    os.system("cls")

def buscarSubMEnu(archivo):
    conta=0
    lol=leer(archivo)
    print("Codigos")
    for i in lol:
        conta+=1
        x=lol.get(i)
        if x[-1]==True:
            print(f"{conta}) {i} {x[0]}")
    opcion=input("Ingrese el codigo correspondiente: ")
    os.system("cls")
    for n in lol[opcion][:-1]:
        print(n)
    input("Presione enter para continuar.")
    os.system("cls")

def buscarPor(archivo):
    lol=leer(archivo)
    print("INFORMACIÓN:")
    for i in  lol:
        print("")
        x=lol.get(i)
        print(f"Clave: {i}")
        for j in range(len(x)-1):
            print(x[j])
        if x[-1]==True:
            print("Estado Activo")
        else:
            print("Estado Innactivo")
    input("Presione enter para continuar.")
    os.system("cls")
    return True

def subMenu(archivo):
    opcion=0
    while opcion != 5:
        try:
            opcion=int(input("1) Información completa de todos los deportes.\n" \
                    "2) Información de un deporte.\n" \
                    "3) Deportes según lugar.\n" \
                    "4) Lista de deportes eliminados.\n" \
                    "5) Salir\n" \
                    "Opción: "))
            os.system("cls")
            if opcion == 1:
                buscarPor(archivo)
            elif opcion == 2:
                buscarSubMEnu(archivo)
            elif opcion == 3:
                buscarLugar(archivo)
            elif opcion == 4:
                eliminados(archivo)
            elif opcion == 5:
                print("")
            else:
                raise ValueError
        except:
            print("Debe de ingresar una opcion valida.")