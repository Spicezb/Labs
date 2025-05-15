#Elaborado por: Xavier Céspedes Alvarado y Luis Guillermo Alfaro
#Fecha de creación: 13/05/2025 19:00
#Última modificación: 14/05/2025 21:10
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

def buscarEnDic(codigo,archivo):
    """
    Funcionamiento:
    - Busca en las llaves del diccionario, a ver si el codigo ingresado esta disponible.
    Entradas:
    - codigo(str): Es el código escrito por el usuario
    - archivo(str): Es el archivo que contiene la base de datos de deportes.
    Salidas:
    - Retorna True o False dependiendo si el codigo está en el diccionario.
    """
    baseDatos=leer(archivo)
    cods=baseDatos.keys()
    if codigo in cods:
        return True
    return False

def registrarDeporte(archivo):
    """
    Funcionamiento:
    - Le pide la información de cada Deporte y la guarda dentro de la base de Datos.
    Entradas:
    - archivo(str): Es el archivo que contiene la base de datos de deportes.
    Salidas:
    - Retorna True al terminar el proceso, pero este no se utiliza.
    """
    try:
        x=leer(archivo)
    except:
        grabar({},archivo)
        x=leer(archivo)
    while True:
        try:
            os.system("cls")
            codDepo=input("Ingrese el código del deporte: ")
            if not re.match(r"TEC\d{2}$",codDepo):
                raise ValueError
            elif buscarEnDic(codDepo,archivo) == True:
                raise TypeError
            break
        except TypeError:
            os.system("cls")
            print("El código ya está en uso.\nIngrese un nuevo código.")
            input("Presione enter para continuar.")
            os.system("cls")
        except ValueError:
            os.system("cls")
            print("El código tiene formato incorrecto.\nDebe de Iniciar por TEC, seguido de 2 números.\nEjemplo: TEC96")
            input("Presione enter para continuar.")
            os.system("cls")
    while True:
        try:
            nomDepo=input("Ingrese el nombre del deporte: ")
            if not re.match(r"\w{6,}",nomDepo):
                raise ValueError
            break
        except ValueError:
            os.system("cls")
            print("El nombre del deporte debe de tener más de 5 caracteres.")
            input("Presione enter para continuar.")
            os.system("cls")
            print(f"Ingrese el código del deporte: {codDepo}")
    while True:
        try:
            expliDepo=input("Ingrese una expliación corta del deporte: ")
            if not re.match(r"[\w\s]{6,250}$",expliDepo):
                raise ValueError
            break
        except ValueError:
            os.system("cls")
            print("La expliación debe de tener más de 5 caracteres y menos de 250 caracteres.")
            input("Presione enter para continuar.")
            os.system("cls")
            print(f"Ingrese el código del deporte: {codDepo}")
            print(f"Ingrese el nombre del deporte: {nomDepo}")
    while True:
        try:
            lugarDepo=input("Ingrese el lugar donde se desarrolla: ")
            if not re.match(r"[\w\s]{6,50}$",lugarDepo):
                raise ValueError
            break
        except:
            os.system("cls")
            print("El nombre del lugar debe de tener más de 5 caracteres y menos de 50 caracteres.")
            input("Presione enter para continuar.")
            os.system("cls")
            print(f"Ingrese el código del deporte: {codDepo}")
            print(f"Ingrese el nombre del deporte: {nomDepo}")
            print(f"Ingrese una expliación corta del deporte: {expliDepo}")
    estaDepo=True
    x[codDepo]=[nomDepo,expliDepo,lugarDepo,estaDepo]
    grabar(x,archivo)
    os.system("cls")
    print("Deporte registrado correctamente.")
    input("Presione enter para continuar.")
    os.system("cls")
    return True



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
    os.system("cls")
    while True:
        try:
            for i in dicc:
                if dicc[i][3]==True:
                    activos.append(i)
            print(f"{i}: {dicc[i][0]}")
            opcion=input("Seleccione un deporte ingresando su código: ")
            if opcion not in activos:
                raise ValueError
            break
        except ValueError:
            os.system("cls")
            print("Debe ingresar un código entre los mostrados anteriormente. Debe incluir las mayúsculas.")
            input("Presione enter para continuar.")
            os.system("cls")
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
            os.system("cls")
            confirmacion=input("¿Desea confirmar?:\n1. Confirmar\n2. Cancelar\nDigite una opción: ")
            os.system("cls")
            if confirmacion not in ("1","2"):
                raise ValueError
            break
        except ValueError:
            os.system("cls")
            print("Debe ingresar una de las opciones anteriores.")
            input("Presione enter para continuar.")
            os.system("cls")
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
        print("Deporte eliminado satisfactoriamente.")
    else:
        print("El deporte no se eliminó.")
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
            os.system("cls")
            nuevo=input("Ingrese el nuevo nombre que desea darle al deporte: ")
            if nuevo==original:
                raise ValueError
            break
        except ValueError:
            os.system("cls")
            print("El nuevo nombre debe ser distinto al anterior.")
            input("Presione enter para continuar.")
            os.system("cls")
    confirmacion=confirmar()
    if confirmacion == "1":
        dicc[modificar][0]=nuevo
        print(f"El nombre del deporte ha sido cambiado.\nNombre anterior: {original}\nNuevo nombre: {nuevo}\n")
        input("Presione enter para continuar.")
        grabar(dicc,archivo)
    else:
        print("El deporte no ha sido modificado.")
    return ""

def eliminados(archivo):
    """
    Funcionamiento:
    - Busca a todos los deportes que su estado sea False.
    Entradas:
    - archivo(str): Es el archivo que contiene la base de datos de deportes.
    Salidas:
    - Retorna la información de todos los deportes Inactivos.
    """
    conta=0
    lol=leer(archivo)
    os.system("cls")
    print("Deportes Eliminados:\n")
    for i in lol:
        x=lol.get(i)
        if x[3] == False:
            for n in range(len(x)-1):
                print(x[n])
                conta+=1
        print("")
    input("Presione enter para continuar.")
    os.system("cls")
    if conta==0:
        os.system("cls")
        print("No hay deportes eliminados")
        input("Presione enter para continuar.")
        os.system("cls")
    return True

def buscarLugar(archivo):
    """
    Funcionamiento:
    - Busca a todos los deportes relacionados con el lugar o un fragmetno de texto que indique el usuario.
    Entradas:
    - archivo(str): Es el archivo que contiene la base de datos de deportes.
    Salidas:
    - Retorna la información de los deportes que coinsidan con el lugar.
    """
    while True:
        try:
            conta=0
            lol=leer(archivo)
            lugar=input("Ingrese el lugar del deporte: ")
            if not lugar != "":
                raise ValueError
            os.system("cls")
            print(f"Resultados relacionados con '{lugar}'")
            for i in lol:
                x=lol.get(i)
                if re.search(lugar.lower(), x[2].lower()):
                    conta+=1
                    for n in range(len(x)-1):
                        print(x[n])
                    if x[-1]==True:
                        print("Estado Activo")
                    else:
                        print("Estado Inactivo")
                    print("")
            if conta==0:
                os.system("cls")
                print(f"No existe deportes registrados por el TEC en el lugar {lugar} que usted especifica.")
            input("Presione enter para continuar.")
            os.system("cls")
            return True
        except:
            os.system("cls")
            print("Debe de indicar una ubicación")
            input("Presione enter para continuar.")
            os.system("cls")

def buscarSubMEnu(archivo):
    """
    Funcionamiento:
    - Muestra un Submenú con los deportes activos, para ver la información especifica del deporte que se escoge.
    Entradas:
    - archivo(str): Es el archivo que contiene la base de datos de deportes.
    Salidas:
    - Retorna True al finalizar el proceso, pero este no se utiliza en ningún momento.
    - Se le muestra al usuario la información especifica del deporte que escogió.
    """
    conta=0
    lol=leer(archivo)
    print("Codigos")
    for i in lol:
        x=lol.get(i)
        if x[-1]==True:
            conta+=1
            print(f"{conta}) {i} {x[0]}")
    if conta!=0:
        opcion=input("Ingrese el codigo correspondiente: ")
        os.system("cls")
        for n in lol[opcion][:-1]:
            print(n)
        input("Presione enter para continuar.")
        os.system("cls")
    else:
        os.system("cls")
        print("No hay Deportes en activo.")
        input("Presione enter para continuar.")
        os.system("cls")
    return True

def buscarPor(archivo):
    """
    Funcionamiento:
    - Busca a todos los deportes ingresados, no importa su estado, y los muestra al usuario.
    Entradas:
    - archivo(str): Es el archivo que contiene la base de datos de deportes.
    Salidas:
    - Retorna la información de todos los deportes.
    """
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
    print("")
    input("Presione enter para continuar.")
    os.system("cls")
    return True

def subMenu(archivo):
    """
    Funcionamiento:
    - Muestra un Submenú donde se elige de que forma ver la información de los deportes.
    Entradas:
    - archivo(str): Es el archivo que contiene la base de datos de deportes.
    Salidas:
    - Retorna True al finalizar el proceso, pero este no se utiliza en ningún momento.
    """
    opcion=0
    while opcion != 5:
        try:
            os.system("cls")
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
            os.system("cls")
            print("Debe de ingresar una opcion valida.")
            input("Presione enter para continuar.")
            os.system("cls")
    return True