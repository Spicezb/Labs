import pickle

def leer(archivo):
    base=open(archivo,"rb")
    herramientas=pickle.load(base)
    return herramientas

def grabar(datos,archivo):
    base=open(archivo,"wb")
    pickle.dump(datos,base)
    base.close
    return ""