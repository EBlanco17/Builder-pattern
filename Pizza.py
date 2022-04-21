import json
class Pizza:
    def __init__(self,tamanio,borde,tipo,precio,domicilio,direccion,costoAdicional):
        self.codTamanio(tamanio)
        self.borde = borde
        self.tipo = tipo
        self.precio = precio
        self.domicilio = domicilio
        self.direccion = direccion
        self.costoAdicional = costoAdicional
        self.tipos = {}
    def codTamanio(self,tamanio):
        tamanios = {'':None,'S':4,'M':2,'L':1}
        self.tamanio = tamanios[tamanio]

    def verTipos(self,tipo):
        self.tipos = {'Hawaiana':["Pina","Jamon","Queso","Salchichas"],'Pepperoni':["Pepperoni"],'Vegetariana':["Tomate","Lechuga","Cebolla","Pimiento"], 'Mexicana':["Pimiento","Chile","Queso","Pavo","Salchichas"]}                        
        self.ingredientes = self.tipos[tipo]
    
    
    
    def verPizza(self):
        print("-----------------------------------------------")
        print(" Tamanio: ", self.tamanio)
        print(" Borde: ", self.borde)
        self.verTipos(self.tipo)
        print(f'" Tipo: "{self.tipo}; {json.dumps(self.ingredientes,sort_keys=False,indent=4)}"')
        print(" Precio: ", self.precio)
        print(" Domicilio: ", self.domicilio)
        print(" Direccion: ", self.direccion)
        print(" Costo Adicional: ", self.costoAdicional)
        print("-----------------------------------------------")