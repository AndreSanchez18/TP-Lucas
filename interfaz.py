import menus as mn
import crud_cliente
import crud_producto
import crud_pedidos
import pickle






def main():


    while True:
        opc = mn.menu_general()

        #Productos
        if opc == "1":
                    bin_file = "productos.bin" 
                    gestor_producto = crud_producto.gestorProducto()
                    gestor_producto.cargar_binario(bin_file)

                    while True:
                        
                        opc = mn.menu_producto()

                        if opc == "1":

                            codigo = input("Codigo de barra: ")
                            nombre = input("Nombre: ")
                            precio = input("Precio: ")

                            gestor_producto.crear_producto(codigo, nombre, precio)

                        elif opc == "2":
                            gestor_producto.mostrar_producto()
                        elif opc == "3":
                            gestor_producto.mostrar_producto()

                            index = input("Ingrese el indice del producto que desea modificar: ")

                            nuevo_codigo = input("Codigo: ")
                            nuevo_nombre = input("Nombre: ")
                            nuevo_precio = input("Precio: ")

                            gestor_producto.modificar_producto(index, nuevo_codigo, nuevo_nombre, nuevo_precio)
                            gestor_producto.sincronizar_binario(bin_file)

                        elif opc == "4":

                            gestor_producto.mostrar_producto()

                            index = input("Ingresa el indice del producto que desea eliminar: ")
                            gestor_producto.eliminar_producto(index)
                            gestor_producto.sincronizar_binario(bin_file)

                        elif opc == "5":
                            break
                        else:
                            print("ERROR : Dene seleccionar una de las opciones disponibles")

        #Clientes
        elif opc == "2":
            bin_file = "clientes.bin"
            gestor_cliente = crud_cliente.gestorCliente()
            gestor_cliente.cargar_binario(bin_file)

            while True:
                opcion = mn.menu_cliente()
                if opcion == "1":
                    while True:
                        dni = input("Ingrese el DNI: ")
                        if gestor_cliente.validar_dni(dni):
                            break

                        
                    while True:
                        print("Ingresa los siguientes datos identificativos basicos: ")
                        nombre = input("Nombre: ")
                        apellido = input("Apellido: ")

                        if gestor_cliente.validar_cliente(nombre, apellido):
                            break

                                   
                    print("Ingrese la fecha de nacimiento (DD/MM/AAAA)")
                    print()

                    while True:
                        dia = input("Ingrese el dia: ")
                        if gestor_cliente.validar_dia(dia):
                            break


                    while True:
                        mes = input(f"Ingrese el mes ({dia}/MM/AAAA): ")
                        if gestor_cliente.valiar_mes(mes):
                            break


                    while True:
                        anio = input(f"Ingrese el año ({dia}/{mes}/AAAA): ")
                        if gestor_cliente.validar_anio(anio):
                            cliente = f"{nombre} {apellido}"
                            gestor_cliente.crear_cliente(dni, cliente, f"{dia}/{mes}/{anio}")
                            gestor_cliente.sincronizar_binario(bin_file)                        
                            break
                             
                elif opcion == "2":
                    gestor_cliente.mostrar_clientes()
                elif opcion == "3":
                    gestor_cliente.mostrar_clientes()

                    while True:
                        index = input("Ingrese el usuario que desea modificar: ")
                        if gestor_cliente.validar_indice(index):
                            break

                    index = int(index)

                    gestor_cliente.lista_clientes[index].dni = ""
                    gestor_cliente.lista_clientes[index].cliente = ""
                    gestor_cliente.lista_clientes[index].fecha_nacimiento = ""

                    while True:
                        dni_nuevo = input("Ingrese el nuevo DNI: ")
                        if gestor_cliente.validar_dni(dni_nuevo):
                            break

                    while True:
                        nombre_nuevo = input("Ingrese el nuevo nombre: ")
                        apellido_nuevo = input("Ingrese el nuevo apellido: ")
                        if gestor_cliente.validar_cliente(nombre_nuevo, apellido_nuevo):
                            break
                    
                    print("Ingrese la nueva fecha de nacimiento")

                    while True:
                        dia_nuevo = input("Dia: ")
                        if gestor_cliente.validar_dia(dia_nuevo):
                            break

                    while True:
                        mes_nuevo = input("Mes: ")
                        if gestor_cliente.valiar_mes(mes_nuevo):
                            break

                    while True:
                        anio_nuevo = input("Año: ")
                        if gestor_cliente.validar_anio(anio_nuevo):
                            fecha_nacimiento_nueva = f"{dia_nuevo}/{mes_nuevo}/{anio_nuevo}"
                            cliente_nuevo = f"{nombre_nuevo} {apellido_nuevo}"
                            gestor_cliente.modificar_cliente(index,dni_nuevo, cliente_nuevo, fecha_nacimiento_nueva)
                            gestor_cliente.sincronizar_binario(bin_file)
                            break

                elif opcion == "4":
                    gestor_cliente.mostrar_clientes()

                    while True:
                        index = input("Ingrese el usuario que desea modificar: ")
                        if gestor_cliente.validar_indice(index):
                            break

                    index = int(index)

                    confirmacion = input("¿Estas seguro de continuar con la eliminacion? (S/N): " ) 
                    while confirmacion.lower() not in ["s", "n"]:
                        confirmacion = input("Elige entre S/N : ")

                    if confirmacion=="s":
                        gestor_cliente.eliminar_cliente(index) 
                        gestor_cliente.sincronizar_binario(bin_file)
                    else:
                        print("Eliminacion cancelada")

                elif opcion == "5":
                    break
                else:
                    print("ERROR : Seleccione una de las opciones disponibles")

        #Pedidos
        elif opc == "3":
            gestor_pedido = crud_pedidos.gestorPedido()
            opc = mn.menu_pedido()

            if opc == "1":

                gestor_cliente.mostrar_clientes()

                opc_cliente = input("Ingrese el ID del cliente que realizo el pedido: ")
 
                gestor_pedido.crear_pedido()


        elif opc == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Debes seleccionar una de las opciones disponibles")

if __name__ == "__main__":
    main()