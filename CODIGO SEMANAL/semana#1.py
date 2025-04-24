
#crear un programa que calcule el costo total de una compra en una tienda

nombre_producto=str(input("Nombre producto: ")) #usuario debe ingresar el nombre del producto
if nombre_producto.isalpha()==False: #validamos que sea de tipo texto
    print("Solo se aceptan letras en este campo.")
    exit()

precio_unitario=(input("Precio del producto: ")) #usuario debe ingresar el precio del producto
if precio_unitario.isdigit() == False or int(precio_unitario)<=0: #validara si el precio es valido y tipo numerico para que pueda continuar
    print("Usted ha ingresado un preciio no valido")
    exit() #saca al usuario del programa
precio_unitario = int(precio_unitario)  # se convierte el valor a numerico despues que se haya validado

cantidad_producto=(input("Cantidad de productos: ")) #usuario debe ingresar la cantidad de productos comprados
if cantidad_producto.isdigit()==False or int(cantidad_producto)<=0: #validara si la cantidad es valida para poder continuar
    print("Usted ha ingresado una cantidad no valida")
    exit() 
cantidad_producto = int(cantidad_producto) # se convierte el valor a numerico despues que se haya validado

total=int(precio_unitario*cantidad_producto) # formula para calcular el valor total a pagar
print()
pregunta=input("Usted tiene descuento? (si/no)  ") #le preguntamos al usuario si tiene descuento
if pregunta=="si":
    descuento=int(input("Ingrese el valor del descuento entre (10 % - 50 %) : ")) #preguntamos de cuanto es su descuento y le damos un rango
    if descuento ==0  or int(descuento)<10 or int (descuento)>50 :
        print("Ha ingresado un valor no valido...")
        exit()
    else: 
        total_descuento=int(total * descuento / 100) #operacion de calculo de porcentaje
        total_pagar=total-total_descuento #formula para saber el valor a pagar con el descuento aplicado
        print()
        print("          ....TIKET DE SU COMPRA...")
        print(F"USTED HA OBTENIDO UN DESCUENTO DE  {total_descuento}")
        print()
        # luego se imprime los datos en sus respectivos espacios
        print("NOMBRE          CANTIDAD          PRECIO          DESCUENTO          VALOR TOTAL")
        print(f"{nombre_producto}               {cantidad_producto}               {precio_unitario:.0f}            {total_descuento:.0f}              {total_pagar:.0f}")
else: #si no se tiene descuento se prosigue 
    print()
    print("          ....TIKET DE SU COMPRA...")
    print("USTED NO HA OBTENIDO NINGUN DESCUENTO")
    print()
    print("NOMBRE          CANTIDAD          PRECIO          DESCUENTO          VALOR TOTAL")
    print(f"{nombre_producto}               {cantidad_producto}               {precio_unitario:.0f}             0              {total:.0f}")
print(             )
print("          ....VUELVA PRONTO....")