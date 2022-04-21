from pydoc import describe


class Casa:
    def __init__(self,_nroCuartos,_nroCocinas,_nroBanos):
        self.nroCuartos=_nroCuartos
        self.nroCocinas=_nroCocinas
        self.nroBanos=_nroBanos
        self.nroVentanas=0
        self.nroPuertas=0
    def calcularVentanas(self):
        self.nroVentanas=2*self.nroCuartos
    def calcularPuertas(self):
        self.nroPuertas=self.nroCuartos+1
    def crearCasa(self):
        self.calcularVentanas()
        self.calcularPuertas()
    def __str__(self) :
        descripcion='-----------------------------------------\n'
        descripcion +=f'Numero de cuartos: {self.nroCuartos}\n'
        descripcion +=f'Numero de baños: {self.nroBanos}\n'
        descripcion +=f'Numero de cocinas: {self.nroCocinas}\n'
        descripcion +=f'Numero de puertas: {self.nroPuertas}\n'
        descripcion +=f'Numero de ventanas: {self.nroVentanas}\n'
        descripcion+='-----------------------------------------\n'

        return descripcion
    


class Garage:
    def __init__(self,area) :
        self.area=area
    def __str__(self) :
        descripcion ='-----------------------------------------\n'
        descripcion +='Tiene garage \n'
        descripcion +=f'Area del garage: {self.area} m^2 \n '
        return descripcion
class Pisscina:
    def __init__(self, area, profuncdidad):
        self.area=area
        self.prof=profuncdidad
    def __str__(self) :
        descripcion ='-----------------------------------------\n'
        descripcion +='Tiene piscina \n'
        descripcion +=f'Area de la piscina: {self.area} m^2\n '
        descripcion +=f'Profundidad de la piscina: {self.prof} m \n '
        return descripcion

class CasaGarage(Casa):
    def __init__(self, _nroCuartos, _nroCocinas, _nroBanos, garage:Garage):
        super().__init__(_nroCuartos, _nroCocinas, _nroBanos)
        self.garage=garage
    def __str__(self):
        describe='Casa con Garage\n'
        describe+=super().__str__()
        describe+=f'{garage}'
        return describe
class CasaPiscina(Casa):
    def __init__(self, _nroCuartos, _nroCocinas, _nroBanos, piscina:Pisscina):
        super().__init__(_nroCuartos, _nroCocinas, _nroBanos)
        self.crearCasa()
        self.piscina=piscina
    def __str__(self):
        describe='Casa con piscina\n'
        describe+=super().__str__()
        describe+=f'{self.piscina}'
        return describe

casita=Casa(3,1,1)
casita.crearCasa()
print(casita)

garage=Garage(40)
casaGarage=CasaGarage(3,1,1,garage)
casaGarage.crearCasa()
print(casaGarage)


pisscina=Pisscina(100,3)
casaPiscina=CasaPiscina(3,1,1,pisscina)
print(casaPiscina)