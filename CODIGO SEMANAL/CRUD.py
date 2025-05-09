inventario={}
def agregar_producto(nombre,precio,cantidad):       #funcion para agreagar el producto con clave valor al inventario
        inventario[nombre] = (float(precio), int(cantidad))       #clave es el nombre y la tupla son el precio y su cantidad
        print("----------------------------------------------------")
        print(f"PRODUCTO {nombre.upper()} SE AÑADIDO CORRECTAMENTE.")
    
def consultar_producto(inventario):          #funcion para consultar el producto en el inventario
    if not inventario: # verificamos si el inventario esta vacio o tiene elementos
        print("")
        print("EL INVENTARIO ESTA VACIO.")
        return
    nombre_producto=input("Ingrese el nombre del producto: ").strip()
    nombre=nombre_producto
    if nombre.isalpha()==False: #verificamos si el valor escrito es valido
        print("")
        print("SOLO SE ACEPTAN VALORES DE TEXTO.")
        print("")
    else:
        if nombre_producto in inventario:  #verificamos si el producto esta en el inventario
            nombre_producto=inventario[nombre] #convertimos el nombre del producto a buscar a que sea igual a la llave del diccionario
            print("")
            precio, cantidad = inventario[nombre] #desempaquetamos los valores que vienen con esa llave
            print(f"PRECIO $ {precio}")
            print(f"CANTIDAD: {cantidad}")
            print("")
        else:
            print("")
            print(f"EL PRODUCTO {nombre.upper()} NO SE ENCUENTRA EN EL INVENTARIO.") # si el prodcuto ingresado no se encuentra en el inventario
            print("")

def actualizar(inventario):    #funcion para actualizar los valores que se desean actualizar 
    if not inventario: #verificamos si el inventario  no esta vacio
        print("EL INVENTARIO ESTA VACIO.")
        print("")
        return
    nombre_actualizar=input("Producto que desea actualizar: ").strip()
    if nombre_actualizar.isalpha()==False:
        print("")
        print("SOLO SE ACEPTAN VALORES DE TEXTO.")
        print("")
    else:
        if nombre_actualizar in inventario:    #verificamos si el producto escrito existe en el inventario
            precio_actualizar=input("Ingrese el nuevo precio: ").strip()
            if precio_actualizar.isdigit() == False or int(precio_actualizar)<=0:  #verificamos si el valor escrito es valido y mayor que 0
                print("")
                print("SOLO SE ACEPTAN VALORES NUMERICOS Y MAYORES QUE 0.")
            else: 
                cantidad_actualizar=input("Ingrese la nueva cantidad: ")
                if cantidad_actualizar.isdigit() == False or int(precio_actualizar)<=0:
                    print("")
                    print("SOLO SE ACEPTAN VALORES NUMERICOS Y MAYORES QUE 0.")
                else:
                    nueva_tupla=(precio_actualizar,cantidad_actualizar)    #creamos una nueva tupla que va a reemplazar a la anterior ingresa originalmente
                    nombre=nombre_actualizar
                    inventario[nombre]=nueva_tupla     #asignamos que los valores de la nueva tupla sean los nuevos de esa clave escrita
                    #print(nueva_tupla)     #aqui hacia pruebas para ver si la tupla nueva obtenia los nuevos valores
                    print("")
                    print(f"EL PRODUCTO {nombre_actualizar.upper()} SE HA ACTUALIZADO CORRECTAMENTE, SU PRECIO A $ {precio_actualizar} Y SU CANTIDAD A {cantidad_actualizar}.")
                    print("")
        else:   #si el producto no se encuentra en el inventario
            print("")
            print("EL PRODUCTO INGRESADO NO ESTA EN EL INVENTARIO.")
            print("")

def eliminar_producto(inventario):   #funcion para elimar el producto
    if not inventario:
        print("")
        print("EL INVENTARIO ESTA VACIO.")
        return
    producto_eliminar=input("Ingrese el nombre del producto que desea eliminar: ").strip()
    if producto_eliminar.isalpha()==False:
        print("")
        print("SOLO SE ACEPTAN VALORES DE TEXTO.")
        print("") 
    if producto_eliminar in inventario:
        nombre=producto_eliminar
        del(inventario[nombre])     #aqui usamos el metodo (del) para eliminar todo lo que este con este conectado a ese nombre (tuplas)
        print("")
        print(f"SE HA ELIMINADO CORRECTAMENTE EL PRODUCTO {producto_eliminar.upper()} DEL INVENTARIO.")
        print("")
    else:
        print("")
        print("EL PRODUCTO ESCRITO NO SE ENCUENTRA EN EL INVENTARIO.")
        print("")
valor_total = lambda: sum(float(precio) * int(cantidad) for precio, cantidad in inventario.values())    #usamos la funcion lambda para recorrer la cantidad y precio de los productos en el inventario y asi hacer la operacion

print("BIENVENIDO...")
print("")

while True: 
        print("INVENTARIO DE TIENDA ...")
        print("---------------------------------------------")
        print("1"".Ingresar producto.")
        print("2"".Consultar producto.")
        print("3"".Actualizar precio y cantidad.")
        print("4"".Eliminar producto.")
        print("5"".Valor total de inventario.")
        print("6"".Salir del inventario.")
        print("---------------------------------------------")
        opcion=input("Escriba la opcion que quiera ejecutar: ")
        print("")

        if opcion=="1": 
            while True:
                nombre=input("Ingrese el nombre del producto: ").strip()
                if nombre.isalpha()==False:
                    print("")
                    print("SOLO SE ACEPTAN VALORES DE TEXTO.")
                    print("")
                    break
                else:
                    if nombre  in inventario: #verificamos si el producto ya se encuentra en el inventario
                        print("")
                        print(f"YA SE ENCUENTRA EL PRODUCTO {nombre.upper()} EN EL INVENTARIO")
                        print("")
                        break
                    else:
                        precio=input("Ingrese el precio del producto: ").strip()
                        if precio.isdigit() == False or int(precio)<=0:
                            print("")
                            print("SOLO SE ACEPTAN VALORES NUMERICOS Y MAYORES QUE 0.")
                            print("")
                            break
                        else:
                            cantidad=input("Ingrese la cantidad del producto: ").strip()
                            if cantidad.isdigit() == False or int(cantidad)<0:
                                print("")
                                print("SOLO SE ACEPTAN CANTIDADES POSITIVAS")
                                print("")
                                break
                            else:
                                agregar_producto(nombre,precio,cantidad) #llamamos la funcion de agregar producto
                                print("")
                                opcion2=input("Desea agregar un nuevo producto? (si/no): ").strip()
                                if opcion2=="si":
                                    print("")
                                elif opcion2=="no":
                                    print("")
                                    break


        elif opcion=="2":
            consultar_producto(inventario)    #llamamos la funcion de consultar el productos 

        elif opcion=="3":
            actualizar(inventario)       #llamamos la funcion de actualizar el producto
        

        elif opcion=="4":
            eliminar_producto(inventario)   #llamamos la funcion de eliminar producto

        elif opcion=="5":
            valor_total()
            print("VALOR TOTAL DEL INVENTARIO ES DE $ ",valor_total())   #llamomos la funcion lambda para imprimir el valor calculado
            print("")

        elif opcion=="6":
            print("HASTA PRONTO...")
            exit()

        elif opcion !="1" and opcion!="2" and opcion!="3" and opcion!="4" and opcion!="5" and opcion!="6":
            print("OPCION INVALIDA.")
            print("")