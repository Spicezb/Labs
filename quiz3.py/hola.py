import re

def clasificarOperadores(lista):
    contaGen=0
    conta=0
    listaconta=[]
    dic={}
    for i in lista:
        if i[0:4] not in dic:
            dic[i[0:4]]=[i]
        else:
            dic[i[0:4]].append(i)
    for j in dic:
        contaGen+=1
        for x in dic[j]:
            conta+=1
        listaconta.append(conta)
        conta=0
    cantidadM=max(listaconta)
    print(cantidadM)
    for x in listaconta:
        if x == cantidadM:
            print(x.index())
    print(f"Tenemos {contaGen} generaciones.")
            


def clasificarOperadoresAux(lista):
    for i in lista:
        if type(i)!=str:
            print("Debe ingresar únicamente valores de tipo strings")
        elif not re.match(r"[0-9]{10}$",i):
            print("Todos los carnets deben ser textos con 10 valores que representen números.")
    clasificarOperadores(lista)

clasificarOperadores( ["2022011234","2023015432","2021017654","2024017654","2024017765","2020016543"])