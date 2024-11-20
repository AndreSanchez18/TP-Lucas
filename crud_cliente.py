import pickle

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
        elif len(str(dni))!=8:
            print("ERROR : El DNI debe contener 8 numeros")
        else:
            return True
        

    def validar_cliente(self, nombre, apellido):

        cliente = nombre+apellido

        if not cliente.isalpha():
            print("ERROR : El nombre y apellido solo pueden contener letras")
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

        if anio<1900:
            print ("ERROR : El año debe estar por encima de 1900")
            return False
        elif len(str(anio))>4:
            print("ERROR : Solo puede contener 4 digitos")
            return False
        else:
            return True
        

###################### CRUD CLIENTE ###############################

    def crear_cliente(self, dni, cliente, fecha_nacimiento):
            self.lista_clientes.append(Cliente(dni,cliente,fecha_nacimiento))
            self.lista_dni.append(dni)
            print("Cliente creado exitosamente")

    def mostrar_clientes(self):
        cont=1
        for cliente in self.lista_clientes:
            print(f"{cont} : {cliente}")
            cont+=1

    def modificar_cliente(self, index, dni, cliente, fecha_nacimiento):

            self.lista_clientes[index].dni = dni
            self.lista_clientes[index].cliente = cliente
            self.lista_clientes[index].fecha_nacimiento = fecha_nacimiento

            print("Cliente modificar exitosamente")

    def eliminar_cliente(self, index):
        self.lista_clientes.pop(index)
        print("Cliente eliminado exitosamente")
    

######################### SINCRONIZACION CON BINARIO #############################
        

    def sincronizar_binario(self, contenido)

        with open("clientes.bin", "w+b") as archivo:
            archivo.write(pickle.dump(self.lista_clientes))