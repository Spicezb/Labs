#laborado por: Luis Guillermo Alfaro Chacón y Xavier Céspedes Alvarado
#Fecha de creación: 30/04/2025 16:30
#Última modificación: 01/05/2025 11:28
#Versión: 3.13.2
#Importación de librerías. - - - - - - 
import os                             # Se utilizó unicamente para los os.system("cls"). Para poder borrar la consola.
import re
from funcionesLabListas import *

#Definición de funciones. - - - - - -
def mainMenu(lista):
    """
    Funcionamiento:
    - Es el menú principal del programa.
    - Se le pide al usuario una opción, y dependiendo de su elección, se realiza la acción.
    Entradas:
    - lista(list): Es la lista que contiene los números de cédula de los donadores.
    Salidas:
    - Retorna los resultados de cada proceso por separado.
    """
    while True:
        os.system("Cls")
        print("1) Agregar convalientes donadores del día.\n" \
                "2) Decodificar donador.\n" \
                "3) Listar donadores segun el Registro de Naturalizaciones.\n" \
                "4) Donadores totales del pais.\n" \
                "5) Donadores no tipicos.\n" \
                "6) Salir.")
        try:
            option=int(input("Opcion: "))
            if not re.match(r"[1-6]$",str(option)):
                raise ValueError
        except ValueError:
                os.system("cls")
                print("Debe de ingresar una opción válida.")
                input("Presione enter para continuar...")
                os.system("cls")
        os.system("Cls")
        if option == 1:
            agregarDonador(lista)
        elif option == 2:
            print(decodificarDonador(lista))
            input("Presione enter para continuar...")
            os.system("cls")
        elif option == 3:
            print(subMenu(lista))
            input("Presione enter para continuar...")
        elif option == 4:
            for i in range(1,10):
                print(obtenerDonadores(i,lista))
            input("Presione enter para continuar...")
            os.system("cls")
        elif option == 5:
            for i in range(8,10):
                print(obtenerDonadores(i,lista))
            input("Presione enter para continuar...")
            os.system("cls")
        elif option ==6:
            print("Gracias por donar su sangre, ahora fuiste tú, luego espero poder ser yo.")
            break

#Definición de la lista
recuperadosDonantes=["303500621","101110218","412340987","267893456",
                    "154 328765","534561234","187674329","265437654",
                    "243214321","187654321","1876 59870","687659870",
                    "887659870","945659823"]
#Programa principal
mainMenu(recuperadosDonantes)
