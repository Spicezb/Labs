import re

def clasificarOperadores(lista):
    contaGen=0
    conta=0
    listaconta=[]
    generaciones=[]
    mayores=[]
    dic={}
    for i in lista:
        if int(i[0:4]) not in dic:
            generaciones.append(int(i[0:4]))
            dic[int(i[0:4])]=[i]
        else:
            dic[int(i[0:4])].append(i)
    for j in dic:
        contaGen+=1
        for x in dic[j]:
            conta+=1
        listaconta.append(conta)
        conta=0
    cantidadM=max(listaconta)
    for i,j in enumerate(listaconta):
        if j == cantidadM:
            mayores.append(generaciones[i])
    print(dic)
    print(f"Tenemos {contaGen} generaciones.")
    if len(mayores)==1:
        print(f"Pero hay más operadores del {mayores[0]}")
    else:
        print(f"Pero hay más operadores del {mayores[0]} y del {mayores[1]}")
    return ""

def clasificarOperadoresAux(lista):
    for i in lista:
        if type(i)!=str:
            print("Debe ingresar únicamente valores de tipo strings")
        elif not re.match(r"[0-9]{10}$",i):
            print("Todos los carnets deben ser textos con 10 valores que representen números.")
    return clasificarOperadores(lista)

clasificarOperadores(["2022011234","2023015432","2022017654"]) 