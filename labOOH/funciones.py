from archivos import *
import random
from clases import *

def verificarBase(archivo):
    """
    Funcionamiento:
    - Verifica la existencia de la base de datos.
    Entradas:
    - archivo(str): Es el nombre del archivo que contiene la base de datos.
    Salidas:
    - Retorna True o False dependiendo del resultado.
    """
    try:
        base=open(archivo,"rb")
        base.close
        return True
    except:
        print("No existe registro de ninguna herramienta, por favor comience insertando una.")
        return False

def confirmar():
    """
    Funcionamiento:
    - Pide una confirmación al usuario.
    Entradas:
    - N/A
    Salidas:
    - Retorna 1 o 2 dependiendo de la confirmación.
    """
    while True:
        try:
            conf=input("\nDesea confirmar?\n" \
            "1. Confirmar\n" \
            "2. Cancelar\n" \
            "Opción: ")
            if conf not in ("1","2"):
                raise ValueError
            break
        except ValueError:
            print("\nDebe ingresar una de las opciones anteriores.")
    return conf

def infoGen(lista):  
    """
    Funcionamiento:
    - Pide las características de las herramientas nuevas.
    Entradas:
    - lista(list): Es la lista donde se guardan las nuevas herramientas
    Salidas:
    - Retorna las características de la herramienta.
    """
    while True:
        try:
            id=float(input("\nIngrese el id: "))
            if id%int(id)!=0:
                raise ValueError
            elif id<0:
                raise ValueError
        except ValueError:
            print("\nEl id debe ser un número entero positivo.")
            continue
        try:
            id=int(id)
            for i in lista:
                for j in i:
                    if id == j.getIdes():
                        raise ValueError
            break
        except ValueError:
            print("\nEl id ingresado ya está registrado.")
            continue
    while True:        
        try:
            metal=input("\nSeleccione el metal de la herramienta:\n1. Hierro\n2. Diamante\n3. Oro\nOpción: ")
            if metal not in ("1","2","3"):
                raise ValueError
            if metal =="1":
                metal="Hierro"
            elif metal=="2":
                metal="Diamante"
            else:
                metal="Oro"
            break
        except ValueError:
            print("\nDebe seleccionar una de las opciones mostradas anteriormente.")
    while True:        
        try:
            color=input("\nSeleccione el color\n1. Azul\n2. Amarillo\n3. Gris\nOpción: ")
            if color not in ("1","2","3"):
                raise ValueError
            if color =="1":
                color="Azul"
            elif color=="2":
                color="Amarillo"
            else:
                color="Gris"
            break
        except ValueError:
            print("\nDebe seleccionar una de las opciones mostradas anteriormente.")
    durabilidad=random.randint(1,100)
    return id,durabilidad,metal,color

def insertarArma(lista):
    """
    Funcionamiento:
    - Permite insertar un nuevo arma a la base de datos.
    Entradas:
    - lista(list): Es la lista donde se guardan las nuevas herramientas
    Salidas:
    - Retorna la lista actualizada.
    """
    id,durabilidad,metal,color=infoGen(lista)
    while True:
                    try:
                        danno=int(input("\nIngrese el daño: 7, 8 o 9: "))
                        if danno not in (7,8,9):
                            raise ValueError
                        break
                    except:
                        print("\nEl daño debe ser 7, 8 o 9.")
    while True:
        try:
            veloAtaq=float(input("\nIngrese la velocidad de ataque 0.1-0.3: "))
            if veloAtaq<0.1 or veloAtaq>0.3:
                raise ValueError
            break
        except ValueError:
            print("\nLa velocidad de ataque debe estar entre 0.1 y 0.3")
    arma=Arma()
    arma.setIdes(id)
    arma.setDurabilidad(durabilidad)
    arma.setMetal(metal)
    arma.setColor(color)
    arma.setEstado(True)
    arma.setDanno(danno)
    arma.setVelocidadAtaque(veloAtaq)
    lista[0].append(arma)
    print("\nEl arma ha sido agregada.")
    return lista

def insertarArmadura(lista):
    """
    Funcionamiento:
    - Permite insertar una nueva armadura a la base de datos.
    Entradas:
    - lista(list): Es la lista donde se guardan las nuevas herramientas
    Salidas:
    - Retorna la lista actualizada.
    """
    id,durabilidad,metal,color=infoGen(lista)
    while True:
        try:
            defen=int(input("\nIngrese la defensa 4, 5 o 6: "))
            if not defen in (4,5,6):
                raise ValueError
            break
        except:
            print("\nLa defensa debe ser 4, 5 o 6.")
    armadura= Armadura()
    armadura.setIdes(id)
    armadura.setDurabilidad(durabilidad)
    armadura.setMetal(metal)
    armadura.setColor(color)
    armadura.setEstado(True)
    armadura.setDefensa(defen)
    lista[1].append(armadura)
    print("\nLa armadura ha sido agregada.")
    return lista

def desgastarArma(lista):
    """
    Funcionamiento:
    - Desgasta la durabilidad de un arma de 25 en 25.
    Entradas:
    - lista(list): Es la lista donde se guardan las nuevas herramientas.
    Salidas:
    - Desgasta las armas y retorna strs vacíos.
    """
    hayActiva=False
    for i in lista[0]:
        if i.getEstado()==True:
            hayActiva=True
    if hayActiva==False:
        print("\nNo hay ningún arma para desgastar.")
        return ""
    while True:
        try:
            id=float(input("\nIngrese el id del arma que desea desgastar o digite -1 para regresar: "))
            if int(id)==-1:
                return ""
            if id%int(id)!=0:
                raise ValueError
        except ValueError:
            print("\nEl id debe ser un número entero.")
            continue
        try:
            id=int(id)
            yaExiste=False
            for i in lista[0]:
                if id==i.getIdes():
                    yaExiste=True
                    arma=i
            if yaExiste==False:
                raise ValueError
            break
        except ValueError:
            print("\nEl id ingresado no se encuentra registrado como arma.")
            continue
    if arma.getEstado()==False:
        print("El arma correspondiente al id ingresado fue eliminada.")
        return ""
    while True:
        arma.setDurabilidad(arma.getDurabilidad()-25)
        if arma.getDurabilidad()<=0:
            arma.setEstado(False)
            print("\nEl arma fue desgastada en su totalidad y se eliminó.")
            break
        print("\nEl arma ha sido desgastada.")
        try:
            continuar=input("\nDesea volver a desgastar el arma?\n" \
            "1. Sí\n" \
            "2. No\n" \
            "Opción: ")
            if continuar not in ("1","2"):
                raise ValueError
        except ValueError:
            print("\nDebe ingresar una de las opciones mostradas.")
        if continuar=="2":
            return ""

def eliminarEquipo(lista):
    """
    Funcionamiento:
    - Simula la eliminación de herramientas cambiando su estado.
    Entradas:
    - lista(list): Es la lista donde se guardan las nuevas herramientas
    Salidas:
    - Modifica el estado y retorna strs vacíos.
    """
    hayActivos=False
    for i in lista:
        for j in i:
            if j.getEstado()==True:
                hayActivos=True
    if hayActivos==False:
        print("\nNo hay herramientas que eliminar.")
        return ""
    while True:
        try:
            id=float(input("\nIngrese el id del arma que desea desgastar o digite -1 para regresar: "))
            if int(id)==-1:
                return ""
            if id%int(id)!=0:
                raise ValueError
        except ValueError:
            print("\nEl id debe ser un número entero.")
            continue
        try:
            id=int(id)
            yaExiste=False
            for i in lista:
                for j in i:
                    if id==j.getIdes():
                        yaExiste=True
                        arma=j
            if yaExiste==False:
                raise ValueError
            break
        except ValueError:
            print("\nEl id ingresado no se encuentra registrado.")
            continue
    if arma.getEstado()==False:
        print("\nEl arma ya fue eliminada.")
    elif confirmar()=="1":
        arma.setEstado(False)
        print("\nEl arma fue eliminada.")
    else:
        print("\nLa acción fue cancelada.")
    return ""