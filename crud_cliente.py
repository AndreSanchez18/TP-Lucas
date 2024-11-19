class Cliente:

    def __init__(self,dni:int,nomyape:str,fecha_nacimiento:str):
        self.dni = dni
        self.cliente = nomyape
        self.fecha_nacimiento = fecha_nacimiento

    def __str__(self):
        return f"{self.dni}, {self.cliente}, {self.fecha_nacimiento}"
    

class gestorCliente:

    lista_clientes = []
    lista_dni = []


########################## VALIDACIONES ################################ 
    def validar_dni(self,dni):

        try:
            dni = int(dni)
        except ValueError:
            print("ERROR : EL numero de documento debe ser un entero")
            return False
            
        if dni <= 0:
            print ("ERROR : El numero de documento no puede ser negativo")
            return False
        elif dni in self.lista_dni:
            print ("ERROR : Ya hay un usuario registrado con ese numero de documento")
            return False
        else:
            return True
        

    def validar_cliente(self, cliente):
        if cliente.isnumeric():
            print("ERROR : El nombre y apellido no pueden ser numeros")
            return False
        elif len(cliente) > 50:
            print ("ERROR : El nombre del cliente no debe pasar los 50 caracteres")
            return False
        else:
            return True

        
    def validar_dia(self,dia):
        try:
            dia = int(dia)
        except ValueError:
            print("El dia debe ser un numero entero")
            return False
        
        if dia>31 or dia<1:
            print ("ERROR : El dia de la fecha debe estar entre el 1-31")
            return False
        else:
            return True
        

    def valiar_mes(self,mes):

        try:
            mes = int(mes)
        except ValueError:
            print("El mes debe ser un numero entero")
            return False
        
        if mes>12 or mes<1:
            print ("ERROR : El mes de la fecha debe estar entre el 1-12")
            return False
        else:
            return True
        

    def validar_anio(self,anio):

        try:
            anio = int(anio)
        except ValueError:
            print("El año debe ser un numero entero")
            return False

        if 0>anio:
            print ("ERROR : El año del fecha debe ser mayor a 0")
            return False
        elif len(str(anio))<4:
            print ("ERROR : El año debe llevar 4 numeros")
            return False
        else:
            return True
        

###################### CRUD CLIENTE ###############################

    def crear_cliente(self, dni, cliente, fecha_nacimiento):
            self.lista_clientes.append(Cliente(dni,cliente,fecha_nacimiento))
            print("Cliente creado exitosamente")

    def mostrar_clientes(self):
        for cliente in self.lista_clientes:
            print(cliente)

    def modificar_cliente(self, index, dni, cliente, fecha_nacimiento):
        self.modificar_clientes()

        while True:
            dni = input("Ingrese el dni del cliente que desea modificar: ")

            if dni not in [self.lista_dni]:
                print("El DNI debe pertenecer a un cliente")
            else:
                break
            
        dni_nuevo = input("Ingrese el nuevo DNI: ")
        cliente_nuevo = input("Ingrese el nuevo nombre y apellido: ")

        print("Ingrese la fecha de nacimiento (DD/MM/AAAA)")
        print()

        while True:
            dia = input("Ingrese el dia: ")
            if self.validar_dia(dia):
                break


        while True:
            mes = input(f"Ingrese el mes ({dia}/MM/AAAA) :      ")
            if self.valiar_mes(mes):
                break


        while True:
            anio = input(f"Ingrese el año ({dia}/{mes}/AAAA) :        ")
            if self.validar_anio(anio):
                self.crear_cliente(dni, nombreyapellido, f"{dia}/{mes}/{anio}")
                break
        


        
        

