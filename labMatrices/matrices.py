# Trabajo realizado por Luis Guillermo ALfaro y Xavier Cespedes Alvarado
# Fecha de creación 04/05/2025 21:45
## Ultima actualizacion:05/05/2025 21:20
# Versión de python 3.13.2

#Importación de librerías
from funcionesMatrices import *
import os                   # Se usa unicamente para limpiar pantalla

#Definición de funciones
def menu():
    """
    Funcionamiento:
    - Menu de funciones, depende de la opcion elegida, este hace la accion asignada.
    Entradas:
    - N/A
    Salidas:
    - Retorna el valor de la cada funcion.
    """
    while True:
        try:
            cantidadAparta()
            while True:
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
                            input("Presione enter para continuar.")
                        elif x == 6:
                            os.system("cls")
                            return "Saliendo. . ."
                        else:
                            raise TypeError
        except TypeError:
            os.system("cls")
            print("Debe indicar una opción válida.")
            input("Presione enter para reintentar. . .")

#Programa principal
print(menu())