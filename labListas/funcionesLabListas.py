#laborado por: Luis Guillermo Alfaro Chacón y Xavier Céspedes Alvarado
#Fecha de creación: 30/04/2025 16:30
#Última modificación: 
#Versión: 3.13.2

#Importación de librerías. - - - - - - 
import re

#Definición de funciones. - - - - - -
def agregarDonador(lista):
    cantidad=int(input("Ingrese la cantidad de usuarios que desea agregar:\n"))
    for i in range(cantidad):
        while True:
            try:
                cedula=input("\nIngrese el número de cédula del donador:\n")
                if not re.match(r"[1-9]{1}\d{8}$",cedula):
                    raise ValueError
                if cedula in lista:
                    raise ValueError
                lista.append(cedula)
                print("\nEl donador ha sido agregado.\n")
                break
            except ValueError:
                print("El número de cédula ingresado no es válido.\n")
    return lista

def obtenerDonadores(provincia,lista):
    donadores="\n"
    cantidad=0
    cedulas=[(1,"San José"),(2,"Alajuela"),(3,"Cartago"),(4,"Heredia"),(5,"Guanacaste"),
            (6,"Puntarenas"),(7,"Limón"),(8,"Nacionalizado o naturalizado"),(9,"Partida especial de nacimiento")]
    for i in lista:
        if int(i[0])==provincia:
            cantidad+=1
            donadores += i + "\n"
    if cantidad==0:
        return "Aún no hay personas donadoras de esa naturalización"
    return f"Los donadores de {cedulas[provincia-1][1]}, son {cantidad} con las cédulas:{donadores}"