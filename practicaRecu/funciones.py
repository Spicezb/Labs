# Trabajo realizado por: Luis Guillermo Alfaro y Xavier Céspedes Alvarado
# Fecha de creación: 29/05/2025 20:00
# Ultima actualizacion:29/05/2025 22:00
# Versión de python: 3.13.3

def multiNumerosImp(num,lst=None):
    """
    Funcionamiento: Desmenuza el numero original y guarda cada valor en una lista, para luego ir evaluando numero por numero e ir multiplicando los impares.
    Entradas:
    num(int): Es el numero a evaluar.
    lst(list): Es la lista donde se van guardando los numeros.
    Salidas:
    Se retorna el resultado de la multiplicacion de los numeros impares.
    """
    if lst==None:
        lst=[]
    res=1
    lstIm=[]
    num2=num
    if num2>0:
        num2%=10
        lst.append(num2)
    else:
        for i in lst:
            if i%2!=0:
                lstIm.append(i)
        if lstIm==[]:
            return print(0)
        for i in lstIm:
            res*=i
        return print(res)
    multiNumerosImp(num//10,lst)

def determinarDigitos(num,busc,lst=None):
    """
    Funcionamiento: Desmenuza el numero original y guarda cada valor en una lista, para luego ir evaluando numero por numero.
    Entradas:
    num(int): Es el numero a evaluar.
    busc(int): Es el digito que vamos a buscar.
    lst(list): Es la lista donde se van guardando los numeros.
    Salidas:
    Se retorna el resultado de veces encontradas del numero a buscar.
    """
    if lst==None:
        lst=[]
    res=0
    num2=num
    if num2>0:
        num2%=10
        lst.append(num2)
    else:
        for i in lst:
            if i == busc:
                res+=1
        return print(res)
    determinarDigitos(num//10,busc,lst)