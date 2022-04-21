class Casa:
    def __init__(self, _nroCuartos,_nroCocinas,_nroBanos):
        self.nroCuartos=_nroCuartos
        self.nroCocinas=_nroCocinas
        self.nroBanos=_nroBanos

    #Metodos clases
    def calcularVentanas(self):
        self.nroVentanas=2*self.nroCuartos

    def calcularPuertas(self):
        self.nroPuertas = self.nroCuartos + 1

    def crearCasa(self):
        self.calcularVentanas()
        self.calcularPuertas()
        
    def __str__(self) -> str:
        return (f'"Nro Cuartos: "{self.nroCuartos}"\n Nro Cocinas: "{self.nroCocinas}"\n Nro Baños: "{self.nroBanos} "\n Nro Puertas: "{self.nroPuertas} "\n Nro Ventanas: "{self.nroVentanas}')

class CasaGarage(Casa):
    def __init__(self,_nroCuartos,_nroCocinas,_nroBanos,_ancho,_largo):
        super().__init__(_nroCuartos,_nroCocinas,_nroBanos)
        self.crearCasa()
        self.crearPorton()
        self.ancho = _ancho
        self.largo= _largo
    def crearPorton(self):
        self.porton = 1
    def __str__(self):
        return  (f'{Casa.__str__(self)}"\nNro Portones: "{self.porton}')
    
class CasaPiscina(Casa):
    def __init__(self,_nroCuartos,_nroCocinas,_nroBanos,_ancho,_largo, _profundidad):
        super().__init__(_nroCuartos,_nroCocinas,_nroBanos)
        self.crearCasa()
        self.ancho = _ancho
        self.largo= _largo
        self.profundidad= _profundidad
        self.volumenPiscina()
        
    def volumenPiscina(self):
        self.volumen = self.ancho*self.largo*self.profundidad
    def __str__(self):
        return  (f'{Casa.__str__(self)}"\nPiscina: "{self.volumen}" m3"')   

casita = Casa(3,1,1)
casita.crearCasa()
print(casita)
print("---------------------------------")
casita = CasaGarage(3,1,1,8,15)
casita.crearCasa()
print(casita)
print("---------------------------------")
casita = CasaPiscina(3,1,1,7,10,1.8)
casita.crearCasa()
print(casita)
        