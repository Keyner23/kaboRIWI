dia=input("ingrese el dia (S/N): ")
if dia =="S":
    hora=int(input("ingrese la hora en la que se encuentra: "))
    if hora >=7 and hora <=9 or hora >=17 and hora <=19:
        print("Usted esta en hora PICO")
    else:
        print("Usted esta en hora NORMAL")
elif dia=="N":
    print("FIN DE SEMANA")
else:
    print("Ingrese un dia valido")
