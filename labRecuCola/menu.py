# Elaborado por: Xavier Céspedes Alvarado y Luis GUillermo Alfaro Chacón.
# Fecha de creación: 10/06/2025 19:00
# Última modificación: 10/06/2025 21:30
# Versión: 3.13.3

# Importación

from funciones import *

# Código principal

# Reto 2. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print("\n***** Reto 2. Suma de cuadrados. *****")
x,y = 4,7
print(f"\nPara la entrada: {x,y}")
print("Resultado:")
print(obtenerSumCuadradosAux(x,y))
x,y = 4.5,7
print(f"\nPara la entrada: {x,y}")
print("Resultado:")
print(obtenerSumCuadradosAux(x,y))
x,y = 7,4
print(f"\nPara la entrada: {x,y}")
print("Resultado:")
print(obtenerSumCuadradosAux(x,y))
x,y = 1,5
print(f"\nPara la entrada: {x,y}")
print("Resultado:")
print(obtenerSumCuadradosAux(x,y))

# Reto 4. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print("\n***** Reto 4. Validar binario. *****")
x = 1001019
print(f"\nPara la entrada: {x}")
print("Resultado:")
print(esBinario(x))
x = 0
print(f"\nPara la entrada: {x}")
print("Resultado:")
print(esBinario(x))
x = 5679
print(f"\nPara la entrada: {x}")
print("Resultado:")
print(esBinario(x))
x = 10101
print(f"\nPara la entrada: {x}")
print("Resultado:")
print(esBinario(x))