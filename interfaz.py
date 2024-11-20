import menus as mn
import crud_cliente as c





def main():

    gestor = c.gestorCliente()

    while True:
        opc = mn.menu_general()

        if opc == "2":
            while True:
                opcion = mn.menu_cliente()
                if opcion == "1":
                    while True:
                        dni = input("Ingrese el DNI: ")
                        if gestor.validar_dni(dni):
                            break

                        
                    while True:
                        print("Ingresa los siguientes datos identificativos basicos: ")
                        nombre = input("Nombre: ")
                        apellido = input("Apellido: ")

                        if gestor.validar_cliente(nombre, apellido):
                            break

                                   
                    print("Ingrese la fecha de nacimiento (DD/MM/AAAA)")
                    print()

                    while True:
                        dia = input("Ingrese el dia: ")
                        if gestor.validar_dia(dia):
                            break


                    while True:
                        mes = input(f"Ingrese el mes ({dia}/MM/AAAA): ")
                        if gestor.valiar_mes(mes):
                            break


                    while True:
                        anio = input(f"Ingrese el año ({dia}/{mes}/AAAA): ")
                        if gestor.validar_anio(anio):
                            cliente = f"{nombre} {apellido}"
                            gestor.crear_cliente(dni, cliente, f"{dia}/{mes}/{anio}")
                            break
                             

                elif opcion == "2":
                    gestor.mostrar_clientes()
                elif opcion == "3":
                    gestor.mostrar_clientes()

                    while True:
                        try:
                            index = int(input("Ingrese el usuario que desea modificar: "))
                            break
                        except ValueError:
                            print("ERROR : Debes ingresar un numero")

                    while True:
                        if index-1 > len(gestor.lista_clientes):
                            print("ERROR : Debes ingresar un indice de los clientes registrados")
                        else:
                            break

                    while True:
                        dni_nuevo = input("Ingrese el nuevo DNI: ")
                        if gestor.validar_dni(dni_nuevo):
                            break

                    while True:
                        nombre_nuevo = input("Ingrese el nuevo nombre: ")
                        apellido_nuevo = input("Ingrese el nuevo apellido: ")
                        if gestor.validar_cliente(nombre_nuevo, apellido_nuevo):
                            break
                    
                    print("Ingrese la nueva fecha de nacimiento")

                    while True:
                        dia_nuevo = input("Dia: ")
                        if gestor.validar_dia(dia_nuevo):
                            break

                    while True:
                        mes_nuevo = input("Mes: ")
                        if gestor.valiar_mes(mes_nuevo):
                            break

                    while True:
                        anio_nuevo = input("Año: ")
                        if gestor.validar_anio(anio_nuevo):
                            fecha_nacimiento_nueva = f"{dia_nuevo}/{mes_nuevo}/{anio_nuevo}"
                            cliente_nuevo = f"{nombre_nuevo} {apellido_nuevo}"
                            gestor.modificar_cliente(index-1,dni_nuevo, cliente_nuevo, fecha_nacimiento_nueva)
                            break

                elif opcion == "4":
                    gestor.mostrar_clientes()

                    while True:
                        try:
                            index = int(input("Ingrese el usuario que desea modificar: "))
                            break
                        except ValueError:
                            print("ERROR : Debes ingresar un numero")

                    while True:
                        if index-1 > len(gestor.lista_clientes):
                            print("ERROR : Debes ingresar un indice de los clientes registrados")
                        else:
                            break

                    confirmacion = input("¿Estas seguro de continuar con la eliminacion? (S/N): " ) 
                    while confirmacion.lower() not in ["s", "n"]:
                        confirmacion = input("Elige entre S/N : ")

                    if confirmacion=="s":
                        gestor.eliminar_cliente(index-1)
                    else:
                        print("Eliminacion cancelada")

                elif opcion == "5":
                    break
                else:
                    print("ERROR : Seleccione una de las opciones disponibles")
        elif opc == "2":
            mn.menu_cliente()
        elif opc == "3":
            mn.menu_pedido()
        else:
            print("Saliendo del programa")
            break

if __name__ == "__main__":
    main()