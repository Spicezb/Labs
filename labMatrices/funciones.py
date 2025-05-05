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
