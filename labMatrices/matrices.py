# Trabajo realizado por Luis Guillermo ALfaro y Xavier Cespedes Alvarado
# Fecha de creación 04/05/2025 21:45
#
# Versión de python 3.13.2

#Importación de librerías
from funcionesMatrices import *
import os 

#Definición de funciones
def menu():
    cantPisos= int(input("Digite la cantidad de pisos del edificio: "))
    cantAparta= int(input("Digite la cantidad de apartamentos en cada piso: "))
    edi=crearEdificio(cantPisos,cantAparta)
    while True:
        try:
            x=0
            while x != 6:
                os.system("cls")
                print("1) Alquilar apartamento\n" \
                    "2) Modificar renta\n" \
                    "3) Desalojar\n" \
                    "4) Indicar ingreso por alquiler\n" \
                    "5) Reporte total del edificio\n" \
                    "6) Salir de la aplicacion")
                x=int(input("Opción: "))
                if x == 1:
                    edi=alquilarAparta(edi)
                elif x == 2:
                    edi=modificarRenta(edi)
                elif x == 3:
                    edi=desalojarApartamento(edi)
                elif x == 4:
                    print(ingresoAlquiler(edi))
                elif x == 5:
                    print(reporteTotal(edi))
                else:
                    raise ValueError
        except ValueError:
            os.system("cls")
            print("Debe indicar una opción válida.")
            input("Presione enter para reintentar. . .")

#Programa principal
print(menu())