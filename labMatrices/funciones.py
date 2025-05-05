# Trabajo realizado por Luis Guillermo ALfaro y Xavier Cespedes Alvarado
# Fecha de creación 04/05/2025 21:45
#
# Versión de python 3.13.2

# Libreiras                                                                          

# Funciones
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