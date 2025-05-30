# Elaborado por: Xavier Céspedes Alvarado y Luis GUillermo Alfaro Chacón
# Fecha de creación: 24/05/2025 14:32
# Última modificación: 26/05/2025 22:20
# Versión: 3.13.3

#Importación de librerías
from funciones import *
from archivos import *

#Definición de funciones
def desgastarArmaAux(lista):
    """
    Funcionamiento:
    - Verifica el arma que se va a desgastar.
    Entradas:
    - lista(list): Es la lista donde se guardan las nuevas herramientas.
    Salidas:
    - Llama a la función principal.
    """
    hayActiva=False
    for i in lista[0]:
        if i.getEstado()==True:
            hayActiva=True
    if hayActiva==False:
        print("\nNo hay ningún arma para desgastar.")
        return lista
    while True:
        try:
            id=float(input("\nIngrese el id del arma que desea desgastar o digite -1 para regresar: "))
            if int(id)==-1:
                return lista
            if id%int(id)!=0:
                raise ValueError
        except ValueError:
            print("\nEl id debe ser un número entero.")
            continue
        try:
            id=int(id)
            yaExiste=False
            for i in lista[0]:
                if id==i.getIdes():
                    yaExiste=True
                    objeto=lista[0].index(i)
            if yaExiste==False:
                raise ValueError
            break
        except ValueError:
            print("\nEl id ingresado no se encuentra registrado como arma.")
            continue
    if lista[0][objeto].getEstado()==False:
        print("El arma correspondiente al id ingresado fue eliminada.")
        return lista
    return desgastarArma(lista,objeto)

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
                lista=desgastarArmaAux(lista)
                grabar(lista,arch)
            elif opcion==4:
                lista=eliminarEquipo(lista)
                grabar(lista,arch)
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