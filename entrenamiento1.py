
#crear un programa que calcule el costo total de una compra en una tienda

nombre_producto=input("Nombre producto: ") #usuario debe ingresar el nombre del producto

precio_unitario=int(input("Precio del producto: ")) #usuario debe ingresar el precio del producto
if precio_unitario<=0: #validara si el precio es valido para que pueda continuar
    print("Usted ha ingresado un preciio no valido")
    exit() #saca al usuario del programa

cantidad_producto=int(input("Cantidad de productos: ")) #usuario debe ingresar la cantidad de productos comprados
if cantidad_producto<=0: #validara si la cantidad es valida para poder continuar
    print("Usted ha ingresado una cantidad no valida")
    exit() #saca al usuario del programa

descuento=10 #el % de descuento que se le aplicara
total=precio_unitario*cantidad_producto # formula para calcular el valor total a pagar
cantidad_minima=5 #cantidad minima para aplicar el descuento

print(             )
print(             )
print("          ....TIKET DE SU COMPRA...")
print()
# hacemos la validacion para ver si aplica al descuento siempre y cuando que la cantidad sea mayor a la minima
if cantidad_producto>cantidad_minima: #si la cantidad de producto es mayor a 5, se realizara lo siguiente 
    total_descuento=int(total * descuento / 100)
    total_pagar=total-total_descuento
    print(F"USTED HA OBTENIDO UN DESCUENTO DE  {total_descuento}")
    print()
    # luego se imprime los datos en sus respectivos espacios
    print("NOMBRE          PRECIO          DESCUENTO          VALOR TOTAL")
    print(f"{nombre_producto}          {precio_unitario:.0f}              {total_descuento:.0f}              {total_pagar:.0f}")
else: 
    # dado el caso que la cantidad sea menor a 5 se imprime tal cual sin descuento
    print("USTED NO HA OBTENIDO NINGUN DESCUENTO")
    print()
    print("NOMBRE          PRECIO          DESCUENTO          VALOR TOTAL")
    print(f"{nombre_producto}          {precio_unitario:.0f}                0                     {total:.0f}")
print(     )

print("          ....VUELVA PRONTO....")
