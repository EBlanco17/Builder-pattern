from Pizza import *

class PizzaBuilder:
    def __init__(self):
        self.tamanio=""
        self.borde=""
        self.tipo={}
        self.precio=""
        self.domicilio=""
        self.direccion=""
        self.costoAdicional=""

    @staticmethod
    def pizza():
        return PizzaBuilder()
    def setTamanio(self, tamanio):
        self.tamanio = tamanio
        return self
    def setBorde(self, borde):
        self.borde = borde
        return self
    def setTipo(self, tipo):
        self.tipo = tipo
        return self
    def setPrecio(self, precio):
        self.precio = precio
        return self
    def setDomicilio(self, domicilio):
        self.domicilio = domicilio
        return self
    def setDireccion(self, direccion):
        self.direccion = direccion
        return self
    def setCostoAdicional(self, costoAdicional):
        self.costoAdicional = costoAdicional
        return self
    def build(self):
        return Pizza(self.tamanio, self.borde, self.tipo, self.precio, self.domicilio, self.direccion, self.costoAdicional)

p1 = PizzaBuilder.pizza()
dom =p1.setTamanio("S").setBorde("C").setTipo("Hawaiana").setPrecio("$10").setDomicilio("Si").setDireccion("Calle 1").setCostoAdicional("$2").build()
dom.verPizza()

p2 = PizzaBuilder.pizza()
dom2 = p2.setTamanio("M").setBorde("C").setTipo("Mexicana").setPrecio("$15").setDomicilio("Si").setDireccion("Calle 2").setCostoAdicional("$3").build()
dom2.verPizza()