import pickle
from crud_cliente import gestorCliente

class Pedido:

	def __init__(self, id_pedido, productos, cliente, fecha_creacion):
		self.id_pedido = id_pedido
		self.productos = productos
		self.cliente = cliente
		self.fecha_creacion = fecha_creacion

	def __str__(self):
			return f"{self.id_pedido}, {self.productos}, {self.cliente}, {self.fecha_creacion}"

class gestorPedido:

	primer_pedido=0
	lista_pedidos = []

	def crear_pedido(self, id_pedido, productos, cliente, fecha_creacion):
		self.lista_pedidos.append(Pedido(id_pedido, productos, cliente, fecha_creacion))
		print("Pedido creado exitosamente")

	def mostrar_pedidos(self):

		for p in self.lista_pedidos:
			print(p)

	def modificar_pedido(self, index, productos, cliente, fecha_actualizacion):

		self.lista_pedidos[index].fue_actualizado = True
		self.lista_pedidos[index].productos = productos
		self.lista_pedidos[index].cliente = cliente
		self.lista_pedidos[index].fecha_actualizacion = fecha_actualizacion
		print("Pedido actualizado exitosamente")

	def eliminar_pedido(self, index):
		self.lista_pedidos.pop(index)
		print("Pedido eliminado extiosamente")

	def sincronizar_binario(self,bin_file):
		with open(bin_file,"wb") as b_fin:
			b_fin.write(pickle.dumps(self.lista_productos))

	def cargar_binario(self, bin_file):
		try:
			with open(bin_file, "rb") as b_file:
				self.lista_productos=pickle.load(b_file)
		except (FileNotFoundError, EOFError):
			with open(bin_file, "wb") as b_file:
				b_file.write(self.lista_productos)





		