suma=0

while True:
    numero=input("ingrese su numero: ")     

    if numero!="salir":
        numero=int(numero)
        suma+=numero

    else:
        print("HA SALIDO DEL PROGRAMA...")
        print(f"el acumulado de numero ingresados es de {suma}")
        break
    