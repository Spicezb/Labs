#laborado por: Luis Guillermo Alfaro Chacón y Xavier Céspedes Alvarado
#Fecha de creación: 30/04/2025 16:30
#Última modificación: 01/05/2025 21:30
#Versión: 3.13.2

#Importación de librerías. - - - - - - 
import os                             # Se utilizó unicamente para los os.system("cls"). Para poder borrar la consola.
import re

#Definición de funciones. - - - - - -
def subMenu(lista):
    """
    Funcionamiento:
    - Es el submenú para la funcion obtenerDonadores.
    - Se le pide al usuario una opción, y dependiendo de su elección, se realiza la acción.
    Entradas:
    - N/A
    Salidas:
    - Retorna la opción que se eligió.
    """
    print("Indique la provincia a buscar\n1) San José\n2) Alajuela\n3) Cartago\n4) Heredia\n" \
    "5) Guanacaste\n6) Puntarenas\n7) Limón\n8) Nacionalizado/naturalizado (Extranjero)\n" \
    "9) Partida especial de nacimiento (Casos especiales)")
    prov=int(input("Provincia: "))
    try:
        if not re.match(r"[1-9]$",str(prov)):
            raise ValueError
        else:
            os.system("cls")
            return obtenerDonadores(prov,lista)
    except ValueError:
                os.system("cls")
                return("Debe de ingresar una opción válida.")

def agregarDonador(lista):
    """
    Funcionamiento:
    - Le solicita al usuario la cantidad de donadores que desea ingresar y
    luego le pide los números de cédula uno por uno.
    Entradas:
    - lista(list): Es la lista que guarda los números de cédula de los donadores.
    Salidas:
    - Retorna la lista con los donadores agregados.
    """
    try:
        os.system("cls")
        cantidad=int(input("Ingrese la cantidad de usuarios que desea agregar:\n"))
        for i in range(cantidad):
            while True:
                os.system("cls")
                cedula=input("Ingrese el número de cédula del donador:\n")
                if not re.match(r"[1-9]{1}\d{8}$",cedula):
                    raise TypeError
                if cedula in lista:
                    raise TypeError
                lista.append(cedula)
                print("El donador ha sido agregado.")
                input("Presione enter para continuar...")
                break
    except TypeError:
        print("El número de cédula ingresado no es válido.")
    except ValueError:
        print("Debe de ingresar una cantidad válida.")
    return lista

def decodificarDonador(lista):
    """
    Funcionamiento:
    - Le solicita al usuario el número de cédula de un donador para decodificarla. En caso de
    que no esté registrado, explica la situación.
    Entradas:
    - lista(list): Es la lista que guarda los números de cédula de los donadores.
    Salidas:
    - Retornas la decodificación de la cédula o dice si la persona no está registrada.
    """
    cedulas=[(1,"San José"),(2,"Alajuela"),(3,"Cartago"),(4,"Heredia"),(5,"Guanacaste"),
            (6,"Puntarenas"),(7,"Limón"),(8,"Nacionalizado o naturalizado"),(9,"Partida especial de nacimiento")]
    while True:
        try:
            donador=input("Ingrese el número de cédula que desea buscar:\n")
            if not re.match(r"[1-9]{1}\d{8}$",donador):
                raise ValueError
            break
        except ValueError:
            "Debe ingresar un número de cédula válido.\n"
    if donador in lista:
        return f"\nEl donador es de {cedulas[int(donador[0])-1][1]}, está registrado en el tomo {donador[1:5]} y el asiento {donador[5:]}."
    else:
        return "La persona no está registrada como donadora.\n"

def obtenerDonadores(provincia,lista):
    """
    Funcionamiento:
    - Obtiene las cédulas de los donadores por provincia.
    Entradas:
    - lista(list): Es la lista que guarda los números de cédula de los donadores.
    - provincia(int): Es el dígito que identifica cada provincia.
    Salidas:
    - Retornas los números de cédula de los donadores en la provincia.
    """
    donadores="\n"
    cantidad=0
    cedulas=[(1,"San José"),(2,"Alajuela"),(3,"Cartago"),(4,"Heredia"),(5,"Guanacaste"),
            (6,"Puntarenas"),(7,"Limón"),(8,"Nacionalizado o naturalizado"),(9,"Partida especial de nacimiento")]
    for i in lista:
        if int(i[0])==provincia:
            cantidad+=1
            donadores += i + "\n"
    if cantidad==0:
        return "Aún no hay personas donadoras de esa naturalización.\n"
    return f"Los donadores de {cedulas[provincia-1][1]}, son {cantidad} con las cédulas:{donadores}"
