# Trabajo realizado por Luis Guillermo ALfaro y Xavier Cespedes Alvarado
# Fecha de creación 04/05/2025 21:45
#
# Versión de python 3.13.2
# Libreiras                                                                          
import os
# Funciones
def crearEdificio(cP,cA):
    piso=[]
    for i in range(cP):
        aparta = []
        for n in range(cA):
            aparta.append(0)
        piso.append(aparta)
    return piso

def alquilarAparta(edi):
    while True:
        try:
            if dispo(edi)==True:
                aparta=buscarApartamento(edi)
                print(aparta)
                if edi[aparta[0]-1][aparta[1]-1] == 0:
                    monto=int(input("Digite el monto del aquiler de este apartamento: "))
                    edi[int(aparta[0]-1)][int(aparta[1]-1)]=+monto
                    print("El apartamento ha sido alquilado.")
                    return edi
                else:
                    raise TypeError
            else:
                os.system("cls")
                print("No hay apartamentos disponibles")
                input("Presione enter para continuar.")
                return edi
        except ValueError :
            os.system("cls")
            print("Ingrese un valor valido.")
            input("Presione enter para reintentar. . .")
        except TypeError:
            os.system("cls")
            print("El apartamento está alquilado, por favor digite otro número de apartamento.")
            input("Presione enter para reintentar. . .")

def dispo(edi):
    for i in range(len(edi)):
        for n in range(len(edi[i])):
            if edi[i][n]==0:
                return True

def modificarRenta(edi):
    while True:
        try:
            piso=[]
            for i in range(len(edi)):
                aparta = []
                for n in range(len(edi[i])):
                    aparta.append(0)
                piso.append(aparta)
            if piso != edi:
                aparta=buscarApartamento(edi)
                if edi[aparta[0]-1][aparta[1]-1] != 0:
                    os.system("cls")
                    opcion=int(input(f"¿Desea aumentar o disminuir la renta del apartamento {aparta[1]} del piso{aparta[0]}\n" \
                                    "1) Confirmar\n2) Cancelar\nOpcion: "))
                    if opcion == 1:
                        os.system("cls")
                        monto=int(input("Digite el monto a modificar de este apartamento: "))
                        if edi[aparta[0]-1][aparta[1]-1] != monto:
                            os.system("cls")
                            print("El alquiler aumentó o disminuyó.\n" \
                                f"Precio anterior: ${edi[aparta[0]-1][aparta[1]-1]}\n" \
                                f"Precio nuevo: ${monto}")
                            input("Presione enter para continuar.")
                            edi[aparta[0]-1][aparta[1]-1]=monto
                            print(edi)
                            return edi
                        else:
                            os.system("cls")
                            print("Debe de ingresar un monto diferente al anterior.")
                            input("Presione enter para continuar.")
                    else:
                        os.system("cls")
                        print("El apartamento no ha sido alquilado.")
                        input("Presione enter para continuar.")
            else:
                os.system("cls")
                print("No hay apartamentos alquilados")
                input("Presione enter para continuar.")
                return edi
        except:
            os.system("cls")
            print("Ingrese un valor válido.")
            input("Presione enter para continuar.")

def buscarApartamento(edi):
    while True:
        try:
            os.system("cls")
            print(edi)
            piso=int(input("Ingrese el piso en el que se ubica el apartamento: "))
            aparta=int(input("Ingrese el número de apartamento: "))
            if piso-1>=len(edi) or aparta-1>=len(edi[0]) or piso-1<0 or aparta-1<0:
                raise ValueError
            return(piso,aparta)
        except:
            os.system("cls")
            print("El apartamento ingresado no existe.")
            input("Presione enter para reintentar. . .")

def subMenu():
    x=0
    while x != 0:
        print("1) Alquilar apartamento\n" \
            "2) Modificar renta\n" \
            "3) Desalojar")

def verificarAlquiler(lista):
    for i in lista:
        for n in i:
            if n!=0:
                return True
    return False

def desalojarApartamento(edi):
    aparta=buscarApartamento(edi)
    edi[aparta[0]-1][aparta[1]-1] = 0
    print("El apartamento ha sido desalojado.")
    return edi

def infoAparta(piso,aparta,lista):
    if lista[piso-1][aparta-1]==0:
        return f"\nPiso#{piso}\nApartamento#{aparta}\nEl apartamento no está alquilado."
    return f"\nPiso#{piso}\nApartamento#{aparta}\nMonto de alquiler: ${lista[piso-1][aparta-1]}"

def ingresoApartamento(lista):
    while True:
        try:
            piso = int(input("\nIngrese el piso en el que se ubica el apartamento:\n"))
            aparta = int(input("\nIngrese el número de apartamento:\n"))
            if piso>len(lista) or aparta>len(lista[0]) or aparta<=0 or piso<=0:
                raise ValueError
            elif type(piso)!=int or type(aparta)!=int:
                raise TypeError
            break
        except ValueError:
            print("El apartamento ingresado no existe.\n")
        except TypeError:
            print("El piso y el apartamento deben ser valores enteros.\n")
    return infoAparta(piso,aparta,lista)

def ingresoPiso(lista):
    ingreso=0
    aparta=0
    while True:
        try:
            piso = int(input("\nIngrese el piso del que desea saber los ingresos:\n"))
            if piso>len(lista):
                raise ValueError
            elif type(piso)!=int:
                raise TypeError
            break
        except ValueError:
            print("El piso ingresado no es válido.\n")
        except TypeError:
            print("El piso debe ser un valor entero.\n")
    for i in lista[piso-1]:
        ingreso+=i
        aparta+=1
        print(infoAparta(piso,aparta,lista))
    return f"\nEl ingreso total en el piso {piso} es de: ${ingreso}."

def ingresoColumna(lista):
    ingreso=0
    while True:
        try:
            columna = int(input("\nIngrese la columna de la que desea saber los ingresos:\n"))
            if type(columna)!=int:
                raise TypeError
            elif columna>len(lista[0]) or columna<=0:
                raise ValueError
            break
        except ValueError:
            print("La columna ingresada no es válida.\n")
        except TypeError:
            print("La columna debe ser un valor entero.\n")
    for i in enumerate(lista):
        ingreso+=lista[i[0]][columna-1]
        print(infoAparta(i[0]+1,columna,lista))
    return f"\nEl ingreso total en la columna {columna} es de: ${ingreso}."

def ingresoTotal(lista):
    ingreso=0
    for i,n in enumerate(lista):
        for j,m in enumerate(n):
            ingreso+=m
            print(infoAparta(i+1,j+1,lista))
    return f"\nEl ingreso total del edificio es de: ${ingreso}."

def ingresoAlquiler(lista):
    while True:
        try:
            opcion=int(input("1. Ingreso por apartamento.\n" \
                            "2. Ingreso por piso.\n" \
                            "3. Ingreso por columna.\n" \
                            "4. Ingreso total\n"
                            "Opción:\n"))
            if opcion not in (1,2,3,4):
                raise ValueError
            break
        except ValueError:
            print("\nDebe indicar una opción válida.\n")
    if opcion==1:
        return print(ingresoApartamento(lista))
    elif opcion==2:
        return print(ingresoPiso(lista))
    elif opcion==3:
        return print(ingresoColumna(lista))
    elif opcion==4:
        return print(ingresoTotal(lista))
    
