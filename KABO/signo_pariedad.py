numero=int(input("ingrese su numero:"))

if numero>0:
    print("su numero es positivo")
    if numero%2==0:
        print("su numero es positivo y es par")
    else:
        print("su numero es positivo y es impar")

elif numero==0:
    print("su numero es 0")

else:
    print("su numero es negativo")
    if numero%2==0:
        print("su numero es negativo y es par")
    else:
        print("su numero es negativo y es impar")