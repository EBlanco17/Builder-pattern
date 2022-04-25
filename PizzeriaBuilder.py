from Pizzeria import *

class PizzeriaBuilder:
    def __init__(self):
        self.Tamanio = ""
        self.Tipo = ""
        self.Domicilio = ""
        self.Direccion = ""
        self.Ingredientes = []

    @staticmethod
    def pizza():
        return PizzeriaBuilder()
    
    def setTamanio(self, _tamanio):
        self.Tamanio = _tamanio
        return self
    
    def setTipo(self,_tipo):
        self.Tipo = _tipo
        return self
    
    def setDomicilio(self,_domicilio):
        self.Domicilio = _domicilio
        return self
    
    def setDireccion(self, _direccion):
        self.Direccion = _direccion
        return self
    
    def setIngredientes(self, _ingredientes):
        self.Ingredientes = _ingredientes
        return self

    def build(self):
        return Pizzeria(self.Tamanio, self.Tipo, self.Domicilio, self.Direccion, self.Ingredientes)


if __name__ == "__main__":
    p1 = PizzeriaBuilder().pizza()
    dom = p1.setTamanio("Large").setTipo("Mexicana").setDomicilio("Si").setDireccion("Calle Falsa 123").setIngredientes(["Lechuga", "Aguacate"]).build()
    dom.verPizzaFinal()

    p2 = PizzeriaBuilder.pizza()
    dom2 = p2.setTamanio("Small").setTipo("Hawaiana").setDomicilio("No").build()
    dom2.verPizzaFinal()