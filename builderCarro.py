
class Motor:
    def __init__(self,_marca,_cilindraje,_potencia, _combustible):
        self.marca = _marca
        self.cilindraje = _cilindraje
        self.potencia = _potencia
        self.combustible = _combustible

    def __str__(self):
        descripcion ='-----------------------------------------\n'
        descripcion +='Motor:\n'
        descripcion +=f'Marca: {self.marca} \n '
        descripcion +=f'Cilindraje: {self.cilindraje} cc \n '
        descripcion +=f'Potencia: {self.potencia} hp \n '
        descripcion +=f'Combustible: {self.combustible} \n '
        return descripcion

class Vehiculo:
    def __init__(self, _marca, _modelo,_tipo, _motor:Motor,_traccion, _caja, _color):
        self.marca = _marca
        self.modelo = _modelo
        self.tipo = _tipo
        self.motor = _motor
        self.traccion = _traccion
        self.caja = _caja
        self.color = _color

    def __str__(self):
        descripcion ='-----------------------------------------\n'
        descripcion +='Caracteristicas:\n'
        descripcion +=f'Marca: {self.marca} \n '
        descripcion +=f'Modelo: {self.modelo} \n '
        descripcion +=f'Tipo: {self.tipo} \n '
        descripcion +=f'Tracción: {self.traccion} \n '
        descripcion +=f'Caja: {self.caja} \n '
        descripcion +=f'Color: {self.color} \n '
        descripcion +=f'{self.motor}'
        return descripcion

class Radio:
    def __init__(self, _marca, _lectorCD, _gps, _camara, _vehiculo:Vehiculo):
        self.marca = _marca
        self.lectorCD = _lectorCD
        self.gps = _gps
        self.camara = _camara
        self.vehiculo = _vehiculo

    def __str__(self):
        descripcion =f'{self.vehiculo}'
        descripcion +='-----------------------------------------\n'
        descripcion +='Radio:\n'
        descripcion +=f'Marca: {self.marca} \n'
        descripcion +=f'Lector CD: {self.lectorCD} \n'
        descripcion +=f'GPS: {self.gps} \n'
        descripcion +=f'Camara: {self.camara} \n'
        return descripcion

class Llantas:
    def __init__(self, _rin,_marca,_referencia, _tipo, _vehiculo:Vehiculo):
        self.rin = _rin
        self.marca = _marca
        self.referencia = _referencia
        self.tipo = _tipo
        self.vehiculo = _vehiculo

    def __str__(self):
        descripcion =f'{self.vehiculo}'
        descripcion +='-----------------------------------------\n'
        descripcion +='Llantas:\n'
        descripcion +=f'Rin: {self.rin} \n'
        descripcion +=f'Marca: {self.marca} \n'
        descripcion +=f'Referencia: {self.referencia} \n'
        descripcion +=f'Tipo: {self.tipo} \n'
        return descripcion

if __name__ == "__main__":
    m1 = Motor('Honda', '1500', '125', 'Gasolina')
    v1 = Vehiculo('Honda', 'Civic', 'Sedan', m1, 'Delantera', 'Manual', 'Blanco')
    r1 = Radio('SONNY', 'SI', 'NO', 'NO', v1)
    l1 = Llantas('16', 'ChaoYang', '230/65r16', 'Pistera', v1)
    print(r1)
    print(l1)
    
    m2=Motor('Skoda', '1500', '125', 'Gasolina')
    v2=Vehiculo('Skoda', 'Octavia', 'Sedan', m2, 'Delantera', 'Manual', 'Blanco')
    r2= Radio('SONNY', 'SI', 'NO', 'NO', v2)
    l2= Llantas('16', 'ChaoYang', '230/65r16', 'Pistera', v2)
    print(r2)
    print(l2)
