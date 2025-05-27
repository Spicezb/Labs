# Elaborado por: Xavier Céspedes Alvarado y Luis Guillermo Alfaro Chacón
# Fecha de creación: 27/05/2025 8:00
# Última modificación: 27/05/2025
# Versión: 3.13.3

#Definición de funciones
#Reto #1: Los operadores del Lab - - - - - - - - - - - - - - - - - - - - - - - -






#Reto #3: Cambiemos la vista. - - - - - - - - - - - - - - - - - - - - - - - - -
def obtenerCodigo(lista): #Se utiliza para ordenar la matriz.
    return lista[0]

def convertirAMatriz(dicc):
    matriz=[]
    valores=list(dicc.values()) #Es una lista con los valores del diccionario
    codigos=[]
    for i in valores:
        for j in i:
            if j[0] not in codigos: #Si el codigo aún no existe en la matriz, se añade junto con su contenido.
                codigos.append(j[0])
                matriz.append([j[0],[j[1]]]) 
            else:
                matriz[codigos.index(j[0])][1].append(j[1]) #Se añade el string en la posición donde se encuentra su código si este se usa más de una vez.
    matriz.sort(key=obtenerCodigo) #Se ordena la matriz
    return matriz

#Código principal
#Reto #1: Los operadores del Lab - - - - - - - - - - - - - - - - - - - - - - - -
print("***** Reto #1: Los operadores del lab. *****\n")







#Reto #3: Cambiemos la vista. - - - - - - - - - - - - - - - - - - - - - - - - -
print("\n***** Reto #3: Cambiemos la vista. *****\n")
x={
"Lluvia": [
(10,"Lluvia de meteoros Táuridas del Sur"), (21,"Lluvia de meteoros Oriónidas")
],
"Conjunciones": [
(21,"Conjunción de la Luna con Júpiter"), (23,"Conjunción de la Luna con Marte")
],
"Otros": [
(2,"La luna pasará frente al sol"), (3,"Galaxia del escultor"),
(14,"Ocultación lunar"), (17,"Luna Llena"), (31,"El cúmulo doble de Perseo")
]
}
print(f"Para la entrada: {x}\n\nResultado:")
print(convertirAMatriz(x))