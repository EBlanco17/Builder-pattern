from builderCliente import *

class UsuarioBuilder:
    def __init__(self):
        self.nombre=""
        self.cedula=""
        self.genero=""
        self.estadoCivil=""

        self.direccion=""
        self.deportes=[]
        self.entretenimiento={}
        self.vehiculo={"tipo":None, "modelo":None, "placa":None, "marca":None}
    
    @staticmethod
    def usuario():
        return UsuarioBuilder()
    def setNombre(self, nombre):
        self.nombre = nombre
        return self
    def setGenero(self, genero):
        self.genero = genero
        return self
    def setCedula(self, cedula):
        self.cedula = cedula
        return self
    def setEstadoCivil(self, estadoCivil):
        self.estadoCivil = estadoCivil
        return self

    def setDireccion(self, direccion):
        self.direccion = direccion
        return self

    def setDeportes(self, deportes):
        self.deportes = deportes.copy()
        return self

    def setEntretenimiento(self, entretenimiento):
        self.entretenimiento = entretenimiento.copy()
        return self
    def setVehiculo(self, vehiculo):
        self.vehiculo = vehiculo.copy()
        return self
    
    def build(self):
        return Usuario(self.nombre, self.cedula, self.genero, self.estadoCivil, self.direccion, self.deportes, self.entretenimiento, self.vehiculo)

usuario = UsuarioBuilder.usuario()  
juan = usuario.setNombre("Juan").setCedula("123456789").setGenero("M").setEstadoCivil("S").build() 
juan.verUsuario() 