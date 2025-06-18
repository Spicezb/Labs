def analizarNotas(lista,listaT=[]):
    esta=False
    if lista==[]:
        return listaT
    for i,j in enumerate(listaT):
        if j[0]==lista[0]:
            esta=True
            listaT[i]=(j[0],j[1]+1)
    if esta==False:
        listaT.append((lista[0],1))
    return analizarNotas(lista[1:],listaT)

print(analizarNotas([100, 875, 480, 560, 480, 875, 100, 100, 575, 480, 480]))