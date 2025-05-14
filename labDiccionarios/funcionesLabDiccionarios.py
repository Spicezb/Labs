#Elaborado por: Xavier Céspedes Alvarado y Luis Guillermo Alfaro
#Fecha de creación: 13/05/2025
#Última modificación: 13/05/2025
#Versión: 3.13.3

#Importación de librerías
import pickle

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
            confirmacion=input("¿Desea confirmar la eliminación?:\n1. Confirmar\n2.Cancelar\nDigite una opción:\n")
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
        print("\nDeporte eliminado satisfactoriamente.")
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
    confirmacion=confirmar()
    original=dicc[modificar][0]
    while True:
        try:
            nuevo=input("Ingrese el nuevo nombre que desea darle al deporte:\n")
            if nuevo==original:
                raise ValueError
            break
        except ValueError:
            print("\nEl nuevo nombre debe ser distinto al anterior.\n")
    if confirmacion == "1":
        dicc[modificar][0]=nuevo
        print(f"El nombre del deporte ha sido cambiado\nNombre anterior: {original}\nNuevo nombre: {nuevo}")
    else:
        print("El deporte no ha sido modificado.")
    return ""