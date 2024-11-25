import pickle

class Producto:

	def __init__(self, codigo, nombre, precio):

		self.codigo = codigo
		self.nombre = nombre
		self.precio = precio

	def __str__(self):
		return f"{self.codigo}, {self.nombre}, {self.precio}"


class gestorProducto:

	lista_productos = []


#######################  CRUD PRODUCTO ################################

	def crear_producto(self, codigo, nombre, precio):
		self.lista_productos.append(Producto(codigo, nombre, precio))
		print("Producto creado exitosamente")

	def mostrar_producto(self):
		for idx, p in enumerate(self.lista_productos):
			print(f"{idx} : {p}")

	def modificar_producto(self, index, codigo, nombre, precio):

		self.lista_productos[index].codigo = codigo
		self.lista_productos[index].nombre = nombre
		self.lista_productos[index].precio = precio
		print("Producto modificado correctamente")

	def eliminar_producto(self, index):
		self.lista_productos.pop(index)
		print("Producto eliminado exitosamente")

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
