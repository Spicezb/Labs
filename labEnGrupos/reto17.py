def analizarNotas(lista,listaT=[]):
    if lista==[]:
        return listaT
    for i,j,k in enumerate(listaT):
        if j==lista[0]:
            listaT[i][1]+=1
    return analizarNotas(lista[1:],listaT)

analizarNotas([100, 875, 480, 560, 480, 875, 100, 100, 575, 480, 480])