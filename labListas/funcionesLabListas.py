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
            except:
                print("El número de cédula ingresado no es válido.\n")
    return lista