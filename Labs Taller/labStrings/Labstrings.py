# Elaborado por: Xavier Céspedes Alvarado
# Fecha de creación: 22/4/2025 09:11
# Última modificación: 
# Versión: 3.13.2

# Importación de librerías 
from funciones import *
import re

# Reto#1: Nomenclatura de una varilla de construcción - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def verificarVarillaAux(varilla):
    """
    Funcionamiento:
    - Verifica que el str ingresado sea válido para evaluar las características de la varilla.
    Entradas:
    - varilla(str): Es el str que se evalúa para saber las características de la varilla.
    Salidas:
    - Los diferentes errores al ingresar el código de la varilla.
    - Llama a la función principal e imprime un str con los resultados.
    """
    diametro="34568"
    proceso="SW"
    grados=("40","60","70")
    if len(varilla)!=6:
        return "Debe indicar 6 valores exactamente."
    elif varilla[:2].isupper()==False:
        return "Los dos primeros caracteres deben ser mayúsculas."
    elif varilla[2] not in diametro:
        return "El diámetro de entrada no es un valor permitido."
    elif varilla[3] not in proceso:
        return "El proceso de fabricación indicado no es permitido."
    elif varilla[4:] not in grados:
        return "El grado del acero no es un valor permitido."
    else:
        fabricante,diametro,proceso,grados=verificarVarilla(varilla)
        return f"""El fabricante es {fabricante}
El diámetro de la varilla es {diametro}
Proceso de fabricación: {proceso}
Grados de acero: {grados}
"""

def verificarVarillaES(varilla):
    """
    Funcionamiento:
    - Recibe el código de la varilla que será evaluado.
    Entradas:
    - varilla(str): Es el str que se evalúa para saber las características de la varilla.
    Salidas:
    - La excepción si lo ingresado no es un str.
    - Imprime la función auxiliar.
    """
    try:
        print(verificarVarillaAux(varilla))
    except ValueError:
        print("Debe ingresar una cadena de 6 caracteres")
    return ""

#Reto#1: Nomenclatura de una varilla de construcción. Con expresiones regulares - - - - - - - - - - - - - -
def verificarVarillaAuxER(varilla):
    if not re.match ("[A-Z]{2}(3|4|5|6|8)(S|W)(40|60|70)",varilla):
        return "Debe ingresar un código de varilla válido"
    else:
        fabricante,diametro,proceso,grados=verificarVarilla(varilla)
        return f"""El fabricante es {fabricante}
El diámetro de la varilla es {diametro}
Proceso de fabricación: {proceso}
Grados de acero: {grados}
"""

def verificarVarillaESER(varilla):
    """
    Funcionamiento:
    - Recibe el código de la varilla que será evaluado.
    Entradas:
    - varilla(str): Es el str que se evalúa para saber las características de la varilla.
    Salidas:
    - La excepción si lo ingresado no es un str.
    - Imprime la función auxiliar.
    """
    try:
        print(verificarVarillaAuxER(varilla))
    except ValueError:
        print("Debe ingresar una cadena de 6 caracteres")
    return ""

#Programa principal - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Reto#1: Nomenclatura de una varilla de construcción. - - - - - - - - - - - - - - 
print("\nReto#1: Nomenclatura de una varilla de construcción.\n")
x="SV5S6"
print("Para la entrada:",x)
print(verificarVarillaES(x))
x="SV9S60" 
print("Para la entrada:",x)
print(verificarVarillaES(x))
x="SV5S55" 
print("Para la entrada:",x)
print(verificarVarillaES(x))
x="SV5S60"
print("Para la entrada:",x)
print(verificarVarillaES(x))

# Reto#1: Nomenclatura de una varilla de construcción. Con expresiones regulares. - - - - - - - - - - - - - - 
print("\nReto#1: Nomenclatura de una varilla de construcción. Con expresiones regulares.\n")
x="SV5S6"
print("Para la entrada:",x)
print(verificarVarillaESER(x))
x="SV9S60" 
print("Para la entrada:",x)
print(verificarVarillaESER(x))
x="SV5S55" 
print("Para la entrada:",x)
print(verificarVarillaESER(x))
x="SV5S60"
print("Para la entrada:",x)
print(verificarVarillaESER(x))