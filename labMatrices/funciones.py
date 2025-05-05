# Trabajo realizado por Luis Guillermo ALfaro y Xavier Cespedes Alvarado
# Fecha de creación 04/05/2025 21:45
#
# Versión de python 3.13.2
# Libreiras                                                                          

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
    piso=buscarApartamento()
    if edi[int(piso[0])][int(piso[1])] == 0:
        monto=int(input("Digite el monto del aquiler de este apartamento: "))
        for i in range(len(edi)):
            if i == int(piso[0]):
                for n in range(len(edi[i])):
                    if n == int(piso[1]):
                        edi[i][n]+=monto
        #edi[int(piso[0])][int(piso[1])] += monto
        print(edi)

def buscarApartamento():
    piso=input("Digite el piso del apartamento a buscar: ")
    aparta=input("Digite el número del apartamento a buscar: ")
    return(piso,aparta)

def menu():
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

def desalojarApartamento(lista):
    while True:
        try:
            piso = int(input("Ingrese el piso en el que se ubica el apartamento:\n\n"))
            aparta = int(input("Ingrese el número de apartamento:\n\n"))
            if piso>len(lista) or aparta>len(lista[0]):
                raise ValueError
            break
        except ValueError:
            print("El apartamento ingresado no existe.\n\n")
    lista[piso-1][aparta-1] = 0
    print("El apartamento ha sido desalojado.")
    return lista

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
    

lista=[[1,2,3,4],[1,2,3,4],[1,2,3,0]]
ingresoAlquiler(lista)
