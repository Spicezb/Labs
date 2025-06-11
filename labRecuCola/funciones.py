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