# Elaborado por: Xavier Céspedes Alvarado y Luis GUillermo Alfaro Chacón.
# Fecha de creación: 10/06/2025 19:00
# Última modificación: 10/06/2025 21:30
# Versión: 3.13.3

# Definición de funciones

# Reto 2. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def obtenersumCuadrados(m,n,res=0):
    if m == n:
        return res + n**2
    res += m**2 
    return obtenersumCuadrados(m+1,n,res)

def obtenerSumCuadradosAux(m,n):
    if n<m:
        return -1
    if type(n)!= int or type(m)!=int:
        return -1
    return obtenersumCuadrados(m,n)

# reto 4. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def esBinario(num):
    if num%10!=0 and num%10!=1:
        return False
    if num==0:
        return True
    return esBinario(num//10)

# reto 5. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def contarBisiestos(pNum1,pNum2,conta):
    """
    Funcionamiento:
    - Recorre recursivamente el rango de años entre pNum1 y pNum2 y cuenta cuántos de esos años son bisiestos.
    Entradas:
    - pNum1 (int): Año inicial del rango.
    - pNum2 (int): Año final del rango.
    - conta (int): Acumulador que lleva la cuenta de los años bisiestos encontrados.
    Salidas:
    - Retorna un entero con la cantidad total de años bisiestos entre pNum1 y pNum2 (inclusive).
    """
    if pNum1<=pNum2:
        if pNum1%4==0 and ((pNum1%100!=0) or (pNum1%400==0)):
            pNum1+=1
            conta+=1
            return contarBisiestos(pNum1,pNum2,conta)
        pNum1+=1    
        return contarBisiestos(pNum1,pNum2,conta)
    return conta

def contarBisiestosAux(pNum1,pNum2):
    """
    Funcionamiento:
    - Verifica que ambos valores ingresados sean enteros positivos.
    - Además, valida que el año inicial sea menor o igual al año final.
    - Si todo es válido, llama a la función recursiva 'contarBisiestos' para contar los años bisiestos en ese rango.
    Entradas:
    - pNum1 (int): Año inicial del rango.
    - pNum2 (int): Año final del rango.
    Salidas:
    - Retorna un mensaje de error si alguno de los valores no es válido.
    - Si todo es correcto, retorna la cantidad de años bisiestos entre pNum1 y pNum2 (inclusive).
    """
    if (type(pNum1)!=int or pNum1<0) or (type(pNum2)!=int or pNum2<0):
        return "Los valores deben de ser números enteros positivos mayores a 0."
    elif pNum1>pNum2:
        return "El año inicial debe ser debe ser menor que el año final."
    return contarBisiestos(pNum1,pNum2,0)