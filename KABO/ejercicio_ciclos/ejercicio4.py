secreto=5
intentos=0
numero=0

while numero!=secreto and intentos<5:
    numero=int(input("ingrese el numero: "))
    intentos+=1
else:
    print("no adivino el numero")
        
