# Elaborado por: Xavier Céspedes Alvarado y Luis GUillermo Alfaro Chacón
# Fecha de creación: 21/05/2025 16:45
# Última modificación: 21/05/2025 21:53
# Versión: 3.13.3

class Persona:
# Definicion de atributos
    nombre=""
    cedula=""
    categoria=""
    profesion=""
    estado=True
# Definicion de los metodos
    def __init__(self):
        self.nombre=""
        self.cedula=""
        self.categoria=""
        self.profesion=""
        self.estado=True
    
    def setNombre(self, pnombre):
        self.nombre=pnombre
        return self.nombre
    
    def setCedula(self, pcedula):
        self.cedula=pcedula
        return self.cedula
    
    def setCategoria(self, pcategoria):
        self.categoria=pcategoria
        return self.categoria
    
    def setProfesion(self, pprofesion):
        self.profesion=pprofesion
        return self.profesion
    
    def setEstado(self, pestado):
        self.estado=pestado
        return self.estado
    
    def getNombre(self):
        return self.nombre
    
    def getCedula(self):
        return self.cedula
    
    def getCategoria(self):
        return self.categoria
    
    def getProfesion(self):
        return self.profesion
    
    def getEstado(self):
        return self.estado
    
    def getDatos(self):
        return f"Cédula: {self.cedula}, Nombre: {self.nombre}, Categoría: {self.categoria}, Profesión: {self.profesion}, Estado: {self.estado}"