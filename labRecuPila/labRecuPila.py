# Elaborado por: Xavier Céspedes Alvarado y Luis Guillermo Alfaro Chacón
# Fecha de creación:
# Última modificación:
# Versión:

#Definición de funciones

#Reto 1. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
def contarDigitos(num):
    cont=0
    while num>0:
        cont+=1
        num//=10
    return cont

def esPar(num):
    if num%2==0:
        return True
    return False

def esDigitoPar(num1,num2,pos):
    if contarDigitos(num2)==pos:
        if esPar(num2)==True:
            return True
        return False
    if contarDigitos(num2)-contarDigitos(num1)==pos-1:
        if esPar(num1)==True:
            return True
        else:
            return False
    return esDigitoPar(num1//10,num2,pos)

def esDigitoParAux(num,pos):
    if contarDigitos(num)<pos:
        return "El número no posee el índice solicitado."
    elif pos<1 or pos>9:
        return "La posición tiene que ser un entero entre 1 y 9."
    elif type(pos)!=int or type(num)!=int:
        return "El número y la posición deben ser enteros."
    elif num<0:
        return "El número debe ser un entero positivo."
    return esDigitoPar(num,pos)

#Reto 7. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
def sumaDivisores(num,div):
    if div==0:
        return 0
    if num%div==0:
        return div + sonCercanos(num,div-1)
    return sonCercanos(num,div-1)

def sonCercanos(a,b):
    if sumaDivisores(a,a-1)==sumaDivisores(b,b-1):
        return True
    return False

def sonCercanosAux(a,b):
    if a<1 or b<1 or type(a)!=int or type(b)!=int:
        return "Los números deben ser enteros mayores o iguales que 1."
    return sonCercanos(a,b)

#Código principal
#Reto 1. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
print("\n***** Reto #1. *****")
x,y=6700,3
print(f"\nPara la entrada: {x,y}")
print("Resultado:")
print(esDigitoParAux(x,y))
x,y=9255,4
print(f"\nPara la entrada: {x,y}")
print("Resultado:")
print(esDigitoParAux(x,y))
x,y=80,3
print(f"\nPara la entrada: {x,y}")
print("Resultado:")
print(esDigitoParAux(x,y))
x,y=94,1
print(f"\nPara la entrada: {x,y}")
print("Resultado:")
print(esDigitoParAux(x,y))

#Reto 2. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
print("\n***** Reto #2. *****")
x,y=13,7
print(f"\nPara la entrada: {x,y}")
print("Resultado:")
print(sonCercanosAux(x,y))
x,y=18,51
print(f"\nPara la entrada: {x,y}")
print("Resultado:")
print(sonCercanosAux(x,y))
x,y=98,175
print(f"\nPara la entrada: {x,y}")
print("Resultado:")
print(sonCercanosAux(x,y))
x,y=220,562
print(f"\nPara la entrada: {x,y}")
print("Resultado:")
print(sonCercanosAux(x,y))