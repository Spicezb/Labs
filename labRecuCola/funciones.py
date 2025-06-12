# Elaborado por: Xavier Céspedes Alvarado y Luis GUillermo Alfaro Chacón.
# Fecha de creación: 10/06/2025 19:00
# Última modificación: 10/06/2025 21:30
# Versión: 3.13.3

# Definición de funciones

# Reto 2. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def obtenersumCuadrados(m,n,res=0):
    """
    Funcionamiento:
    - Calcula la suma de los cuadrados entre m y n de forma recursiva.
    Entradas:
    - m(int): Límite inferior.
    - n(int): Límite superior.
    - res(int): Acumulador de la suma.
    Salidas:
    - Retorna la suma de los cuadrados entre m y n.
    """
    if m == n:
        return res + n**2
    res += m**2 
    return obtenersumCuadrados(m+1,n,res)

def obtenerSumCuadradosAux(m,n):
    """
    Funcionamiento:
    - Verifica que los valores sean válidos y llama a la función que suma cuadrados.
    Entradas:
    - m(int): Límite inferior.
    - n(int): Límite superior.
    Salidas:
    - Retorna la suma de los cuadrados entre m y n, o -1 si hay error.
    """
    if n<m:
        return -1
    if type(n)!= int or type(m)!=int:
        return -1
    return obtenersumCuadrados(m,n)

# Reto 3. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def obtenerParesImpares(pNum,contaP,contaI):
    """
    Funcionamiento:
    - Recorre recursivamente cada dígito del número ingresado, y va contando cuántos dígitos son pares y cuántos son impares.
    Entradas:
    - pNum (int): Número entero positivo que se desea evaluar.
    - contaP (int): Contador acumulador para los dígitos pares.
    - contaI (int): Contador acumulador para los dígitos impares.
    Salidas:
    - Retorna una tupla (contaP, contaI) con la cantidad de dígitos pares e impares del número.
    """
    if pNum>0:
        if (pNum%10)%2==0:
            contaP+=1
            pNum//=10
            return obtenerParesImpares(pNum,contaP,contaI)
        else:
            pNum//=10
            contaI+=1
            return obtenerParesImpares(pNum,contaP,contaI)
    return (contaP,contaI)

def obtenerParesImparesAux(pNum):
    """
    Funcionamiento:
    - Verifica que el número ingresado sea un entero. Si es negativo, lo convierte a positivo, si el número es 0, lo reconoce como un dígito par.
    - Llama a la función recursiva 'obtenerParesImpares' para contar los dígitos pares e impares del número.
    Entradas:
    - pNum (int): Número entero que se desea evaluar.
    Salidas:
    - Retorna un mensaje de error si el valor no es un entero.
    - Si es unicamente 0, retorna la tupla (1, 0) ya que el 0 es considerado par.
    - En cualquier otro caso, retorna una tupla con la cantidad de dígitos pares e impares.
    """
    if type(pNum)!=int:
        return ()
    elif pNum<0:
        pNum-=pNum*2
    elif pNum ==0:
        return (1,0)
    return obtenerParesImpares(pNum,0,0)

# reto 4. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def esBinario(num):
    """
    Funcionamiento:
    - Verifica que un número sea binario.
    Entradas:
    - num(int): Número que se va a evaluar.
    Salidas:
    - Retorna True si el número es binario y False si no.
    """
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