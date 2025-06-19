# Elaborado por Luis Guillermo Alfaro, Xavier Céspedes Alvarado, José David Ruiz, Matias Benavides y Esteban Calderon
# Grupo 2
# Fecha de inicio 12/06/2025 12:54
# Ultima modificacion 18/06/2025 18:00
# Version de Python 3.13.2

# Reto 2
def eliminarTodas(num, lista):
    """
    Funcionamiento:
    - Elimina todas las apariciones del número especificado dentro de una lista.
    - Usa recursión para recorrer cada elemento de la lista y construir una nueva sin el número dado.
    Entradas:
    - num(int): elemento que se desea eliminar de la lista.
    - lista(list): lista original que puede contener múltiples apariciones de 'num'.
    Salidas:
    - list: una nueva lista que contiene todos los elementos de la original excepto las apariciones de 'num'.
    """
    if not lista:
        return []
    if lista[0] == num:
        return eliminarTodas(num, lista[1:])
    else:
        return [lista[0]] + eliminarTodas(num, lista[1:])

# Reto 7
def separar(lista,impar=False):
    """
    Funcionamiento: Toma una lista y la divide en una lista con dos listas: una conteniendo los elementos en posiciones pares, y la otra conteniendo los elementos en posiciones impares.
    Entradas:
    -lista (lista): La lista a separar.
    -impar (bool): Indica si el elemento actual está en una posición par o impar. False por default.
    Salidas:
    -(list): La lista conteniendo las listas con los elementos separados por posición.
    """
    if lista==[]:
        return [[],[]]
    listas=separar(lista[1:],not impar)
    if impar:
        return [[lista[0]]+listas[0],listas[1]]
    else:
        return [listas[0],[lista[0]]+listas[1]]

def validarSeparar(lista):
    """
    Funcionamiento: Verifica la entrada para separar.
    Entradas:
    -lista: En teoría, la lista a separar.
    Salidas:
    -separar (lista) si lista es una lista no vacía, un string de error en otro caso.
    """
    if type(lista)==list:
        if lista!=[]:
            return separar(lista)
        return "La lista no puede ser vacía."
    return "La entrada debe der ser una lista."

# Reto 12
def crearMatrizUnitaria(cantidad,lista=[],conta=0):
    """
    Funcionamiento:
    - Crea recursivamente una matriz unitaria.
    - La matriz contiene 1 en la diagonal principal y 0 en el resto de posiciones.
    Entradas:
    - cantidad (int): Tamaño de la matriz (filas y columnas).
    - lista (list): Lista acumuladora donde se agregan las filas. Por defecto es una lista vacía.
    - conta (int): Contador recursivo que representa la fila actual. Por defecto empieza en 0.
    Salidas:
    - Retorna una lista de listas que representa la matriz identidad de tamaño `cantidad x cantidad`.
    """
    list=[]
    if conta==cantidad:
        return lista
    for i in range(cantidad):
        list.append(0)
    list[conta]=1
    conta+=1
    lista.append(list)
    return crearMatrizUnitaria(cantidad,lista,conta)

def crearMatrizUnitariaAux(cantidad):
    """
    Funcionamiento:
    - Valida que la entrada cantidad sea un número entero mayor a cero.
    - Si la validación es exitosa, llama a la función 'crearMatrizUnitaria' para generar la matriz.
    - Si la validación falla, retorna un mensaje de error.
    Entradas:
    - cantidad(int): valor entero positivo que representa el tamaño de la matriz unitaria a crear.
    Salidas:
    - list: matriz unitaria de tamaño 'cantidad x cantidad', si la entrada es válida.
    - str: mensaje de error si la entrada no es un entero positivo.
    """
    if type(cantidad)!=int or cantidad<=0:
        return "Debe de ingresar un numero entero mayor a 0."
    return crearMatrizUnitaria(cantidad)
# Reto 17
def analizarNotas(lista,listaT=[]):
    """
    Funcionamiento:
    - Analiza los elementos de una lista y devuelve una lista de tuplas que indican cuántas veces aparece cada elemento.
    - Cada tupla tiene la forma (elemento, cantidad de repeticiones).
    - Usa recursión y una lista acumuladora para construir el resultado.
    Entradas:
    - lista(list): lista de elementos que se desea analizar.
    - listaT(list): acumulador de tuplas con formato. Por defecto es una lista vacía.
    Salidas:
    - list: lista de tuplas donde cada una representa un elemento único y cuántas veces aparece en 'lista'.
    """
    esta=False
    if lista==[]:
        return listaT
    for i,j in enumerate(listaT):
        if j[0]==lista[0]:
            esta=True
            listaT[i]=(j[0],j[1]+1)
    if esta==False:
        listaT.append((lista[0],1))
    return analizarNotas(lista[1:],listaT)