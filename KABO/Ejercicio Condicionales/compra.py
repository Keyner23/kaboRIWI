#EJERCICIO 4
compra=int(input("ingrese un valor de compra: "))
vip=(input("ingrese su estado de vip (S/N):"))

if vip=="S":
    if compra>=500:
        descuento=compra*(20/100)
        print(f"usted es vip y ha obtenido un descuento del 20% y su descuento es de:{descuento:.0f}")
    elif compra <500:
        descuento1=compra*(10/100)
        print(f"usted es vip y ha obtenido un descuento del 10% y su descuento es de :{descuento1:.0f}")

elif vip=="N":
    if compra>=500:
        descuento2=compra*(5/100)
        print(f"usted no es vip y ha obtenido un descuento del 5% y su descuento es de:{descuento2:.0f}")
    else:
        print("usted no es vip y no tiene descuento")