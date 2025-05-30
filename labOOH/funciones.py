# Elaborado por: Xavier Céspedes Alvarado y Luis GUillermo Alfaro Chacón
# Fecha de creación: 28/05/2025 14:32
# Última modificación: 29/05/2025 22:20
# Versión: 3.13.3

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

def menuMetales():
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
                return metal
            except ValueError:
                print("\nDebe seleccionar una de las opciones mostradas anteriormente.")

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
            id=int(input("\nIngrese el id: "))
            if id<0:
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
    metal=menuMetales()
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

def desgastarArma(lista,objeto):
    """
    Funcionamiento:
    - Desgasta la durabilidad de un arma de 25 en 25.
    Entradas:
    - lista(list): Es la lista donde se guardan las nuevas herramientas.
    - objeto(int): Es el índice donde se encuentra el objeto.
    Salidas:
    - Desgasta las armas y retorna la lista actualizada.
    """
    arma=lista[0][objeto]
    while True:
        arma.setDurabilidad(arma.getDurabilidad()-25)
        if arma.getDurabilidad()<=0:
            arma.setEstado(False)
            print("\nEl arma fue desgastada en su totalidad y se eliminó.")
            return lista
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
            return lista

def eliminarEquipo(lista):
    """
    Funcionamiento:
    - Simula la eliminación de herramientas cambiando su estado.
    Entradas:
    - lista(list): Es la lista donde se guardan las nuevas herramientas
    Salidas:
    - Modifica el estado y retorna la lista actualizada.
    """
    hayActivos=False
    for i in lista:
        for j in i:
            if j.getEstado()==True:
                hayActivos=True
    if hayActivos==False:
        print("\nNo hay herramientas que eliminar.")
        return lista
    while True:
        try:
            id=int(input("\nIngrese el id del arma que desea desgastar o digite -1 para regresar: "))
            if int(id)==-1:
                return lista
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
                        herramienta=j
            if yaExiste==False:
                raise ValueError
            break
        except ValueError:
            print("\nEl id ingresado no se encuentra registrado.")
            continue
    if herramienta.getEstado()==False:
        print("\nEl arma ya fue eliminada.")
    elif confirmar()=="1":
        herramienta.setEstado(False)
        print("\nEl arma fue eliminada.")
    else:
        print("\nLa acción fue cancelada.")
    return lista

def mostrarElimiados(lista):
    """
    Funcionamiento:
    - Muestra las herramientas donde su estado este en inactivo.
    Entradas:
    - lista(list): Es la lista donde se guardan las herramientas.
    Salidas:
    - Se muestran todos los eliminados.
    """
    conta=0
    if lista==[[],[]]:
        return print("\nNo hay herramientas registradas.")
    for i in range(len(lista)):
        for x in lista[i]:
            if i == 0:
                if x.getInfo()[0][4]==False:
                    print("\nTipo: Arma")
                    mostrarArma(x)
                    conta+=1
            else:
                if x.getDefensa()[0][4]==False:
                    print("\nTipo: Armadura")
                    mostrarArmadura(x)
                    conta+=1
    if conta==0:
        return print("\nNo hay armas eliminadas\n")

def mostrarArmasMetal(lista):
    """
    Funcionamiento:
    - El usuario elige una opcion de metal, y se buscan las armas que esten hechas por este material.
    Entradas:
    - lista(list): Es la lista donde se guardan las herramientas.
    Salidas:
    - Muestra la informacion de las armas que esten hechas por este material.
    """
    conta=0
    if lista[0]==[]:
        return print("\nNo hay armas Registradas.")
    metal=menuMetales()
    for x in lista[0]:
        if x.getInfo()[0][2]==metal:
            if x.getInfo()[0][4]==True:
                conta+=1
                mostrarArma(x)
    if conta==0:
        return print("\nNo hay armas registradas con este tipo de metal\n")

def mostrarHerramientas(lista):
    """
    Funcionamiento:
    - Muestra todas las armas que esten registradas.
    Entradas:
    - lista(list): Es la lista donde se guardan las herramientas.
    Salidas:
    - Muestra la informacion de las herramientas que esten registradas.
    """
    conta=0
    if lista==[[],[]]:
        return print("\nNo hay armas Registradas.")
    print("\nHerramientas\n")
    for i in range(len(lista)):
        for x in lista[i]:
            if i == 0:
                if x.getInfo()[0][4]==True:
                    print("Tipo: Arma")
                    mostrarArma(x)
                    conta+=1
            else:
                if x.getDefensa()[0][4]==True:
                    print("Tipo: Armadura")
                    mostrarArmadura(x)
                    conta+=1
    if conta==0:
        return print("\nNo hay armas registradas en activo\n")
    return True

def mostrarArma(arma):
    """
    Funcionamiento:
    - Muestra la informacion de un arma en concreto.
    Entradas:
    - arma(objc): es el objeto que se quiere saber la informacion.
    Salidas:
    - muestra la informacion del objeto.
    """
    estado=""
    if arma.getInfo()[0][4]==True:
        estado+="Activo"
    else:
        estado+="Inactivo"
    print(f"ID: {arma.getInfo()[0][0]}\n" \
        f"Durabilidad: {arma.getInfo()[0][1]}\n" \
        f"Metal: {arma.getInfo()[0][2]}\n" \
        f"Color: {arma.getInfo()[0][3]}\n" \
        f"Estado: {estado}\n" \
        f"Daño: {arma.getInfo()[1]}\n"\
        f"Velocidad de ataque: {arma.getInfo()[2]}")
    return True

def mostrarArmadura(armadura):
    """
    Funcionamiento:
    - Muestra la informacion de una armadura en concreto.
    Entradas:
    - armadura(objc): es el objeto que se quiere saber la informacion.
    Salidas:
    - muestra la informacion del objeto.
    """    
    estado=""
    if armadura.getDefensa()[0][4]==True:
        estado+="Activo"
    else:
        estado+="Inactivo"
    print(f"ID: {armadura.getDefensa()[0][0]}\n" \
        f"Durabilidad: {armadura.getDefensa()[0][1]}\n" \
        f"Metal: {armadura.getDefensa()[0][2]}\n" \
        f"Color: {armadura.getDefensa()[0][3]}\n" \
        f"Estado: {estado}\n" \
        f"Defensa: {armadura.getDefensa()[1]}")
    return True