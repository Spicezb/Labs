# Trabajo realizado por: Luis Guillermo Alfaro y Xavier Céspedes Alvarado
# Fecha de creación: 29/05/2025 20:00
# Ultima actualizacion:29/05/2025 22:00
# Versión de python: 3.13.3

#Definición de funciones
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

def esPar(num):
    """
    Funcionamiento:
    - Verifica si un número es par.
    Entradas:
    - num(int): Es el número que se evalúa.
    Salidas:
    - Retorna True si el número es par y False si no lo es.
    """
    if num%2==0:
        return True
    return False

def formarNumero(num,res=0,cont=0):
    """
    Funcionamiento:
    - Forma un número con los dígitos pares de otro.
    Entradas:
    - num(int): Es el número del que se sacan los dígitos.
    - res(int): Es el resultado, por defecto es 0.
    - cont(int): Cuenta los dígitos agregados, por defecto es 0.
    Salidas:
    - Retorna el número formado.
    """
    if esPar(num%10)==True:
        res+=(num%10)*(10**cont)
        cont+=1
    if num//10==0:
        return res
    return formarNumero(num//10,res,cont)

def sumarDigitosMultiplos(num,dig,res=0):
    """
    Funcionamiento:
    - Suma los digitos de un número que son múltiplos de un dígito.
    Entradas:
    - num(int): Es el número que se va a evaluar.
    - dig(int): Es el dígito con el que se evalúan los dígitos del número.
    Salidas:
    - Retorna la suma.
    """
    if (num%10)%dig==0:
        res+=num%10
    if num//10==0:
        return res
    return sumarDigitosMultiplos(num//10,dig,res)