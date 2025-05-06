# Trabajo realizado por: Luis Guillermo Alfaro y Xavier Céspedes Alvarado
# Fecha de creación: 04/05/2025 21:45
# Ultima actualizacion:05/05/2025 21
# Versión de python: 3.13.2

# Importación de librerías                                                                     
import os                  # Se usa unicamente para limpiar pantalla

# Definición de funciones
def cantidadAparta():
    """
    Funcionamiento:
    - Pide la estructura de la matriz.
    Entradas:
    - N/A
    Salidas:
    - Los valores de la matriz.
    """
    while True:
        try:
            cantPisos= int(input("Digite la cantidad de pisos del edificio: "))
            cantAparta= int(input("Digite la cantidad de apartamentos en cada piso: "))
            return crearEdificio(cantPisos,cantAparta)
        except:
            os.system("cls")
            print("Ingrese un valor válido.")
            input("Presione enter para continuar.")
            os.system("cls")

def crearEdificio(cP,cA):
    """
    Funcionamiento:
    - Crea la matriz principal.
    Entradas:
    cP(int): Es la cantidad de pisos del edificio.
    cA(int): Es la cantidad de apartamentos del edificio.
    Salidas:
    - Retorna la matriz.
    """
    piso=[]
    for i in range(cP):
        aparta = []
        for n in range(cA):
            aparta.append(0)
        piso.append(aparta)
    return piso

def verificarAlquiler(lista):
    """
    Funcionamiento:
    - Verifica si existe algún apartamento alquilado.
    Entradas:
    lista(list): Es la matriz general del edificio.
    Salidas:
    - Retorna True si hay al menos un apartamento alquilado, y False si no.
    """
    for i in lista:
        for n in i:       
            if n!=0:
                return True
    return False

def alquilarAparta(edi):
    """
    Funcionamiento:
    - Registra los alquileres, si todos los apartamentos estan ocupados, lo notifica, y si se
    quiere registrar uno que tambien este ocupado, este tambien lo notifica.
    Entradas:
    edi(list): Es la matriz general del edificio.
    Salidas:
    - Retorna la matriz actualizada.
    """
    while True:
        try:
            if dispo(edi)==True:
                aparta=buscarApartamento(edi)
                if edi[aparta[0]-1][aparta[1]-1] == 0:
                    monto=int(input("Digite el monto del aquiler de este apartamento: "))
                    edi[int(aparta[0]-1)][int(aparta[1]-1)]=+monto
                    os.system("cls")
                    print("El apartamento ha sido alquilado.")
                    input("Presione enter para continuar.")
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
    """
    Funcionamiento:
    - Verifica si existe algún apartamento sin alquilar, este se utiliza en funciones que se necesita que solo
    retorne true al tener apartamentos libres, y no retornar nada si no.
    Entradas:
    edi(list): Es la matriz general del edificio.
    Salidas:
    - Retorna True si hay al menos un apartamento sin alquilar.
    """
    for i in range(len(edi)):
        for n in range(len(edi[i])):
            if edi[i][n]==0:
                return True

def modificarRenta(edi):
    """
    Funcionamiento:
    - Modifica los alquileres, si todos los apartamentos estan ocupados, lo notifica, y si se
    quiere registrar uno que tambien este ocupado, este tambien lo notifica, si se quiere modificar
    un apartamento y le ponen el mismo precio, este lo va a notificar tambien.
    Entradas:
    edi(list): Es la matriz general del edificio.
    Salidas:
    - Retorna la matriz actualizada.
    """
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
                    opcion=int(input(f"¿Desea modificar la renta del apartamento {aparta[1]} del piso {aparta[0]}?\n" \
                                    "1) Confirmar\n2) Cancelar\nOpcion: ")) 
                    if opcion == 1:
                        os.system("cls")
                        monto=int(input("Digite el monto a modificar de este apartamento: "))
                        if edi[aparta[0]-1][aparta[1]-1] != monto:
                            os.system("cls")
                            print("El monto del alquiler se modificó.\n" \
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
                    elif opcion != 2:
                        raise ValueError
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
    """
    Funcionamiento:
    - Busca el piso y el numero de apartamento.
    Entradas:
    edi(list): Es la matriz general del edificio.
    Salidas:
    - Retorna las direcciones del apartamento.
    """
    while True:
        try:
            os.system("cls")
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

def desalojarApartamento(edi):
    """
    Funcionamiento:
    - Elimina el monto de un apartamento y lo reinicia en 0.
    Entradas:
    edi(list): Es la matriz general del edificio.
    Salidas:
    - Retorna la matriz modificada.
    """
    if verificarAlquiler(edi)==False:
        return "No hay ningún apartamento alquilado."
    aparta=buscarApartamento(edi)
    edi[aparta[0]-1][aparta[1]-1] = 0
    os.system("cls")
    print("El apartamento ha sido desalojado.")
    input("Presione enter para continuar.")
    return edi

def infoAparta(piso,aparta,lista):
    """
    Funcionamiento:
    - Retorna el piso, el número de apartamento y el ingreso de un apartamento individual.
    Entradas:
    - lista(list): Es la matriz general del edificio.
    - piso(int): Es el número de piso.
    - aparta(int): Es el número de apartamento.
    Salidas:
    - Retorna el ingreso total del edificio.
    """
    if lista[piso-1][aparta-1]==0:
        os.system("cls")
        return f"Piso #{piso}\nApartamento #{aparta}\nEl apartamento no está alquilado."
    os.system("cls")
    return f"Piso #{piso}\nApartamento#{aparta}\nMonto de alquiler: ${lista[piso-1][aparta-1]}"

def ingresoApartamento(lista):
    """
    Funcionamiento:
    - Calcula el ingreso de un apartamenbto individual.
    Entradas:
    - lista(list): Es la matriz general del edificio.
    Salidas:
    - Retorna el ingreso del apartamento.
    """
    while True:
        try:
            piso = int(input("Ingrese el piso en el que se ubica el apartamento:"))
            aparta = int(input("Ingrese el número de apartamento:"))
            os.system("cls")
            if piso>len(lista) or aparta>len(lista[0]) or aparta<=0 or piso<=0:
                raise ValueError
            break
        except ValueError:
            os.system("cls")
            print("El apartamento ingresado no existe.\n")
            input("Presione enter para continuar.")
            os.system("cls")
    return infoAparta(piso,aparta,lista)

def ingresoPiso(lista):
    """
    Funcionamiento:
    - Calcula el ingreso total del piso e imprime el monto de cada apartamento.
    Entradas:
    - lista(list): Es la matriz general del edificio.
    Salidas:
    - Retorna el ingreso total del piso.
    """
    ingreso=0
    aparta=0
    while True:
        try:
            piso = int(input("Ingrese el piso del que desea saber los ingresos: "))
            if piso>len(lista):
                raise ValueError
            break
        except ValueError:
            os.system("cls")
            print("El piso ingresado no es válido.")
            input("Presione enter para continuar.")
    for i in lista[piso-1]:
        ingreso+=i
        aparta+=1
        os.system("cls")
        print(infoAparta(piso,aparta,lista))
    return f"El ingreso total en el piso {piso} es de: ${ingreso}."

def ingresoColumna(lista):
    """
    Funcionamiento:
    - Calcula el ingreso por columna e imprime el monto de cada apartamento.
    Entradas:
    - lista(list): Es la matriz general del edificio.
    Salidas:
    - Retorna el ingreso total de la columna.
    """
    ingreso=0
    while True:
        try:
            columna = int(input("Ingrese la columna de la que desea saber los ingresos: "))
            if columna>len(lista[0]) or columna<=0:
                raise ValueError
            break
        except ValueError:
            os.system("cls")
            print("La columna ingresada no es válida.")
            input("Presione enter para continuar.")
            os.system("cls")
    for i in enumerate(lista):
        ingreso+=lista[i[0]][columna-1]
        os.system("cls")
        print(infoAparta(i[0]+1,columna,lista))

    return f"El ingreso total en la columna {columna} es de: ${ingreso}."

def ingresoTotal(lista):
    """
    Funcionamiento:
    - Calcula el ingreso total del edificio e imprime el monto de cada apartamento.
    Entradas:
    - lista(list): Es la matriz general del edificio.
    Salidas:
    - Retorna el ingreso total del edificio.
    """
    ingreso=0
    for i,n in enumerate(lista):
        for j,m in enumerate(n):
            ingreso+=m
            os.system("cls")
            print(infoAparta(i+1,j+1,lista))
    return f"El ingreso total del edificio es de: ${ingreso}."

def ingresoAlquiler(lista):
    """
    Funcionamiento:
    - Imprime un menú con opciones para conocer la totalidad de ingresos en cierrtas partes del edificio o en su totalidad.
    Entradas: 
    - Lista(list): Es la matriz general del edificio.
    Salidas:
    - Llama a las diferentes funciones que calculan los ingresos del edificio.
    """
    while True:
        try:
            os.system("cls")
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
        os.system("cls")
        print(ingresoApartamento(lista))
        input("Presione enter para continuar.")
    elif opcion==2:
        os.system("cls")
        print(ingresoPiso(lista))
        input("Presione enter para continuar.")
    elif opcion==3:
        os.system("cls")
        print(ingresoColumna(lista))
        input("Presione enter para continuar.")
    elif opcion==4:
        os.system("cls")
        print(ingresoTotal(lista))
        input("Presione enter para continuar.")
        

def reporteTotal(lista):
    """
    Funcionamiento:
    - Cuenta los apartamentos alquilados e imprime los porcentajes de apartamentos ocupados y desocupados.
    Entradas:
    - lista(list): Es la matriz general del edificio.
    Salidas:
    - Retorna los porcentajes y la cantidad de apartamentos alquilados y desocupados.
    """
    totalApartas=len(lista[0])*len(lista)
    contador=0
    for i in lista:
        for n in i:
            if n!=0:
                contador+=1
    os.system("cls")
    return f"Total de apartamentos alquilados: {contador}, para un porcentaje de: {round(contador/totalApartas*100,2)}%\n" \
        f"Total de apartamentos desocupados: {totalApartas-contador}, para un porcentaje de: {100-round(contador/totalApartas*100,2)}%"