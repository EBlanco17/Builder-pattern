import json
class Pizzeria:
    def __init__(self,_tamanio,_tipo,_domicilio,_direccion, _ingredientes):
        self.Tamanio = _tamanio
        self.Tipo = _tipo
        self.Domicilio = _domicilio
        self.Direccion = _direccion
        self.Ingredientes = _ingredientes
        
        self.nombre = None
        self.seleccionarTipo()
        
        self.agregarIngrediente()
        self.calcularQueso()
        self.calcularPrecio()
        self.calcularDomicilio()

    def calcularPrecio(self):
        precios = {'Small':25000, 'Medium':37000,'Large':50000}
        self.Precio = precios[self.Tamanio]
    
    def calcularDomicilio(self):
        if self.Domicilio == 'Yes':
            self.Precio += 4500
        else:
            self.Precio = self.Precio
    
    def calcularQueso(self):
        tamanios = {'Small':'200gr', 'Medium':'400gr','Large':'600gr'}
        self.Queso = tamanios[self.Tamanio]

    def seleccionarTipo(self):
        tipos = {'Hawaiana' : Hawaina, 'Pepperoni': Pepperoni, 'Vegetariana': Vegetariana, 'Mexicana': Mexicana}
        self.nombre = tipos.get(self.Tipo)
        
    def verIngredientes(self):
        tipo = self.nombre
        self.Ingredientes = tipo().verIngredientes()
    
    def agregarIngrediente(self):
        tipo = self.nombre
        tipo().agregarIngrediente(self.Ingredientes)

    def verPizzaFinal(self):
        print('-'*30)
        print(" Tamanio: ", self.Tamanio)
        print(" Queso: ", self.Queso)
        self.verIngredientes()
        print(f' Tipo: {self.Tipo} \n Ingredientes: {json.dumps(self.Ingredientes,sort_keys=False,indent=4)}')
        print(" Precio: ", self.Precio)
        print(" Domicilio: ", self.Domicilio)
        if self.Domicilio != 'No':
            print(" Direccion: ", self.Direccion)
        print('-'*30)


class Pizza:
    _ingredientes = []

    def agregarIngrediente(self, ingrediente):
        self._ingredientes.extend(ingrediente) 
    
    def verIngredientes(self):
        return self._ingredientes


class Hawaina(Pizza):
    _ingredientes = ["Pina","Jamon","Queso","Salchichas"]

class Pepperoni(Pizza):
    _ingredientes = ["Pepperoni"]

class Vegetariana(Pizza):
    _ingredientes = ["Tomate","Lechuga","Cebolla","Pimiento"]

class Mexicana(Pizza):
    _ingredientes = ["Pimiento","Chile","Queso","Pavo","Salchichas"]


