#laborado por: Luis Guillermo Alfaro Chacón y Xavier Céspedes Alvarado
#Fecha de creación: 30/04/2025 16:30
#Última modificación: 
#Versión: 3.13.2
from funcionesLabListas import *

recuperadosDonantes=["303500621","101110218","412340987","267893456",
                    "154 328765","534561234","187674329","265437654",
                    "243214321","187654321","1876 59870","687659870",
                    "887659870","945659823"] 
def mainMenu(lista):
    print("1) Agregar convalientes donadores del dia\n" \
            "2) Decodificar donador\n" \
            "3) Listar donadores segun el Registro de Naturalizaciones\n" \
            "4) Donadores totales del pais\n" \
            "5) Donadores no tipicos\n" \
            "6) Salir")
    
    option=int(input("Opcion: "))

    if option == 1:
        print(agregarDonador(lista))
        mainMenu(lista)
    elif option == 2:
        print(decodificarDonador(lista))
        mainMenu(lista)
    elif option == 3:
        print(obtenerDonadores(subMenu(),lista))
        mainMenu(lista)
    elif option == 4:
        for i in range(1,8):
            print(obtenerDonadores(i,lista))
        mainMenu(lista)
    elif option == 5:
        for i in range(8,10):
            print(obtenerDonadores(i,lista))
        mainMenu(lista)
    else:
        return print("Gracias por donar su sangre")

mainMenu(recuperadosDonantes)
