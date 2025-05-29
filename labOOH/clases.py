# Elaborado por: Xavier Céspedes Alvarado y Luis GUillermo Alfaro Chacón
# Fecha de creación: 24/05/2025 14:32
# Última modificación: 24/05/2025 22:13
# Versión: 3.13.3

#Importación de librerías

#Definición de Clases
class Herramienta:
    # Definición de atributos
    ides=0
    durabi=0
    metales=""
    color=0
    estado=True

    def __init__(self):
        self.ides=0
        self.durabi=0
        self.metales=""
        self.color=0
        self.estado=True
    
    def setIdes(self,pides):
        self.ides=pides

    def setDurabilidad(self,pdurab):
        self.durabi=pdurab

    def setMetal(self,pmetal):
        self.metales=pmetal

    def setColor(self,pcolor):
        self.color=pcolor

    def setEstado(self,nestado):
        self.estado=nestado
    
    def getIdes(self):
        return self.ides
    
    def getDurabilidad(self):
        return self.durabi
    
    def getMetal(self):
        return self.metales
    
    def getColor(self):
        return self.color
    
    def getEstado(self):
        return self.estado
    
    def getInfoTotal(self):
        return (self.ides,self.durabi,self.metales,self.color,self.estado)
    
class Arma(Herramienta):
    # Definición de atributos
    danno=0
    velocidadAtaque=0.0
    #Definción de los métodos
    def __init__(self):
        self.danno=0
        self.velocidadAtaque=0.0

    def setDanno(self,ndanno):
        self.danno=ndanno
    
    def setVelocidadAtaque(self,nvelocidadAtaque):
        self.velocidadAtaque=nvelocidadAtaque

    def getDanno(self):
        return self.danno
    
    def getVelocidadAtaque(self):
        return self.velocidadAtaque
    
    def getInfo(self):
        return Herramienta.getInfoTotal(self),self.danno,self.velocidadAtaque
    
class Armadura(Herramienta):
    # Definición de atributos
    defensa=0
    #Definción de los métodos
    def __init__(self):
        self.defensa=0

    def setDefensa(self,ndefensa):
        self.defensa=ndefensa
    
    def getDefensa(self):
        return Herramienta.getInfoTotal(self),self.defensa