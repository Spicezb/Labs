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
                mostrarHerramientas(lista)
            elif opcion==6:
                mostrarArmasMetal(lista)
            elif opcion==7:
                mostrarElimiados(lista)
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