import pickle

def lee(archivo):
    base=open(archivo,"rb")
    dicc=pickle.load(base)
    base.close
    return dicc

def graba(dicc,archivo):
    base=open(archivo,"wb")
    pickle.dump(dicc,base)
    base.close
    return ""