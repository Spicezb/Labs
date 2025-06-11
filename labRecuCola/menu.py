# Elaborado por: Xavier Céspedes Alvarado y Luis GUillermo Alfaro Chacón.
# Fecha de creación: 10/06/2025 19:00
# Última modificación: 10/06/2025 21:30
# Versión: 3.13.3

# Importación

from funciones import *

# Código principal

# Reto 2. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print("\n***** Reto 2. Suma de cuadrados. *****")
print(f"\nPara la entrada: {4,7}\nResultado:")
print(obtenerSumCuadradosAux(4,7))
print(f"\nPara la entrada: {4.5,7}\nResultado:")
print(obtenerSumCuadradosAux(4.5,7))
print(f"\nPara la entrada: {7,4}\nResultado:")
print(obtenerSumCuadradosAux(7,4))
print(f"\nPara la entrada: {1,5}\nResultado:")
print(obtenerSumCuadradosAux(1,5))

# Reto 4. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print("\n***** Reto 4. Validar binario. *****")
print(f"\nPara la entrada: {1001019}\nResultado:")
print(esBinario(1001019))
print(f"\nPara la entrada: {0}\nResultado:")
print(esBinario(0))
print(f"\nPara la entrada: {5679}\nResultado:")
print(esBinario(5679))
print(f"\nPara la entrada: {10101}\nResultado:")
print(esBinario(10101))

# Reto 5. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print("\n***** Reto 5. Contar años Bisiestos. *****")
print(f"\nPara la entrada: {1500,1836}\nResultado:")
print(contarBisiestosAux(1500,1836))
print(f"\nPara la entrada: {2000,2025}\nResultado:")
print(contarBisiestosAux(2000,2025))
print(f"\nPara la entrada: {2022,2023}\nResultado:")
print(contarBisiestosAux(2022,2023))
print(f"\nPara la entrada: {2023,2020}\nResultado:")
print(contarBisiestosAux(2023,2020))
