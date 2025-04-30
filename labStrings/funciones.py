def verificarVarilla(varilla):
    """
    Funcionamiento:
    - Verifica la nomenclatura de la varilla y asigna cada característica a las variables que retorna.
    Entradas:
    - varilla(str): Es el str que se evalúa para saber las características de la varilla.
    Salidas:
    - fabricante(str): Es el fabricante de la varilla.
    - diametro(str): Es el diámetro de la varilla.
    - proceso(str): Es el proceso de fabricación.
    - grados(str): Son los grados de acero.
    """
    fabricante=varilla[:2]
    if varilla[2]=="3":
        diametro="3/8 pulgadas"
    elif varilla[2]=="4":
        diametro="1/2 pulgadas"
    elif varilla[2]=="5":
        diametro="5/8 pulgadas"
    elif varilla[2]=="6":
        diametro="3/4 pulgadas"
    else:
        diametro="1 pulgada"
    if varilla[3]=="S":
        proceso="Acero al carbono no soldable a temperatura ambiente."
    else:
        proceso="Acero al carbono soldable a temperatura ambiente."
    if varilla[5:]=="40":
        grados="2800 kgf/cm2"
    elif varilla[4:]=="60":
        grados="4200 kgf/cm2"
    else:
        grados="5000 kgf/cm2"
    return fabricante,diametro,proceso,grados