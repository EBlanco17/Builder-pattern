class Usuario:

    def __init__(self, nombre, cedula, sexo, estadoCivil, direccion,deportes, entretenimiemto, vehiculo):

        self.nombre = nombre
        self.cedula = cedula
        self.codGenero(sexo)
        self.codificarEstadocivil(estadoCivil)
        self.direccion = direccion
        self.deportes = deportes
        self.entretenimiemto = entretenimiemto
        self.vehiculo = vehiculo
     

    #metodos de clase

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    # def setCedula(self, cedula):
    #     self.cedula = cedula
    # def getCedula(self):
    #     return self.cedula

    def codGenero(self,genero):
        generos ={'':None,'M':32,'F':16,'L':8,'G':4,'B':2,'T':1}
        self.genero = generos[genero]

    def codificarEstadocivil(self,estadoCivil):
        estados = {'':None,'S':4,'C':2, 'U':1}
        self.estadoCivils = estados[estadoCivil]

    def setTipoVehiculo(self,tipoVehiculo):
        self.vehiculo['tipo'] = tipoVehiculo

    def getTipoVehiculo (self):
        return self.vehiculo['tipo']

    def verDeportes(self):
        nombres = ["Extremo", "Competencia","Contacto"]
        indice = 0
        deportesAprobados = ""
        for deporte in self.deportes:
            if(deporte == True):
                deportesAprobados += nombres[indice]+","
            indice += 1
        return deportesAprobados

    def verUsuario(self):
        print("-----------------------------------------------")
        print(" Nombre: ", self.nombre)
        print(" Cedula: ", self.cedula)
        print(" Genero: ", self.genero)
        print(" Estado Civil: ", self.estadoCivils)
        print(" Direccion: ", self.direccion)
        print("Deportes del agrado del usuario: ")
        dep = self.verDeportes()
        print(dep)

        if self.vehiculo['tipo'] != "Ninguno":
            print(" Tipo de vehiculo: ", self.vehiculo['tipo'])
            print(" Marca: ", self.vehiculo['marca'])
            print(" Modelo: ", self.vehiculo['modelo'])
            print(" Placa: ", self.vehiculo['placa'])
            print("-----------------------------------------------")

# juan = Usuario("Juan Sanchez", "123456789", 'M','U',"Avenida siempreviva 123", [False,False,False],
#             {"Peliculas":["Zombieland","El regreso de los muertos vivientes","El crepusculo de los muertos", "La bella durmiente"]
#             ,"Deportes": ["Ninguno"],
#             "Libros":["Algebra de baldor","Calculo de Pourcell"]
#             },
#             {"tipo":"Bicicleta",
#             "marca": "Quintana",
#             "modelo": "Deportivo",
#             "placa": "acb123"
#             })

# juan.verUsuario()