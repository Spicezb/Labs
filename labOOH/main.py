# Elaborado por: Xavier Céspedes Alvarado y Luis GUillermo Alfaro Chacón
# Fecha de creación: 24/05/2025 14:32
# Última modificación: 24/05/2025 22:13
# Versión: 3.13.3

#Importación de librerías
from funciones import *
from archivos import *

#Definición de funciones
def menu(lista,archivo):
    """
    Funcionamiento:
    - Muestra el menú principal y permite elegir las opciones.
    Entradas:
    - lista(list): Es la lista donde se guardan las nuevas herramientas.
    - archivo(str): Es el nombre del archivo donde se tienen que guardar los datos.
    Salidas:
    - Llama a la función necesaria según cada opción.
    """
    while True:
        try:
            opcion=int(input("\n1) Insertar arma\n" \
                        "2) Insertar armadura\n" \
                        "3) Desgastar arma\n" \
                        "4) Eliminar equipo\n" \
                        "5) Mostrar todas las herramientas\n" \
                        "6) Mostrar armas por metal\n" \
                        "7) Mostrar herramientas eliminadas\n" \
                        "8) Salir\n"
                        "opcion: "))
            if opcion==1:
                lista=insertarArma(lista)
                grabar(lista,archivo)
            elif opcion==2:
                lista=insertarArmadura(lista)
                grabar(lista,archivo)
            elif opcion==3:
                desgastarArma(lista)
            elif opcion==4:
                lista=eliminarEquipo(lista)
            elif opcion==5:
                lista=insertarArmadura(lista)
            elif opcion==6:
                lista=insertarArmadura(lista)
            elif opcion==7:
                lista=insertarArmadura(lista)
            elif opcion==8:
                return print("Saliendo")
            else:
                raise ValueError
        except ValueError:
            print("\nDebe ingresar una de las opciones mostradas.")

#Código principal
arch="herramientasMinecraft"
if verificarBase(arch)==True:
    lista=leer(arch)
    menu(lista,arch)
else:
    menu([[],[]],arch)



#Le guardé esto pa para las de mostrar

#Arma
# idBusc=int(input("\nIngrese el ID del arma: "))
# for i in range(0,len(lista[0]-1)):
#     if lista[0][i].getIdes()== idBusc:
#         print(f"ID: {lista[0][i].getInfo()[0][0]}\n" \
#             f"Durabilidad: {lista[0][i].getInfo()[0][1]}\n" \
#             f"Metal: {lista[0][i].getInfo()[0][2]}\n" \
#             f"Color: {lista[1][i].getInfo()[0][3]}\n" \
#             f"Daño: {lista[0][i].getInfo()[1]}\n"\
#             f"Velocidad de ataque: {lista[0][i].getInfo()[2]}")

#Armadura
# existe=False
# idBusc=int(input("\nIngrese el ID del arma: "))
# for i in range(0,len(lista[1]-1)):
#     if lista[1][i].getIdes()==idBusc:
#         existe=True
#         print(f"ID: {lista[1][i].getDefensa()[0][0]}\n" \
#             f"Durabilidad: {lista[1][i].getDefensa()[0][1]}\n" \
#             f"Metal: {lista[1][i].getDefensa()[0][2]}\n" \
#             f"Color: {lista[1][i].getDefensa()[0][3]}\n" \
#             f"Defensa: {lista[1][i].getDefensa()[1]}")
# if existe==False:
#     print("\n El Id ingresado, no se encuentra registrado.")