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

def elegirDeporte(dicc):   
    activos=[]
    for i in dicc:
        if dicc[i][3]==True:
            activos.append(i)
            print(f"{i}: {dicc[i][0]}")
    while True:
        try:
            opcion=input("Seleccione el deporte:\n")
            if opcion not in activos:
                raise ValueError
            break
        except ValueError:
            print("\nDebe ingresar un código entre los mostrados anteriormente. Debe incluir las mayúsculas.\n")
    return opcion

def confirmar():   
    while True:
        try:
            confirmacion=input("¿Desea confirmar la eliminación?:\n1. Confirmar\n2.Cancelar\nDigite una opción:\n")
            if confirmacion not in ("1","2"):
                raise ValueError
            break
        except ValueError:
            print("\nDebe ingresar una de las opciones anteriores.\n")
    return confirmacion

def eliminarDeporte(archivo):  
    dicc=lee(archivo)
    elim=elegirDeporte(dicc)
    confirmacion=confirmar()
    if confirmacion=="1":
        dicc[elim][3]=False
        graba(dicc,archivo)
        print("\nDeporte eliminado satisfactoriamente.")
    else:
        print("El deporte no se eliminó.")
    return ""

def modificarDeporte(archivo):
    dicc=lee(archivo)
    modificar=elegirDeporte(dicc)
    confirmacion=confirmar()
    original=dicc[modificar][0]
    while True:
        try:
            nuevo=input("Ingrese el nuevo nombre que desea darle al deporte:\n")
            if nuevo==original:
                raise ValueError
            break
        except ValueError:
            print("\nEl nuevo nombre debe ser distinto al anterior.\n")
    if confirmacion == "1":
        dicc[modificar][0]=nuevo
        print(f"El nombre del deporte ha sido cambiado\nNombre anterior: {original}\nNuevo nombre: {nuevo}")
    else:
        print("El deporte no ha sido modificado.")