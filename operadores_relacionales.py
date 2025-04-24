#EJERCICIO 8
numero1=int(input("ingrese el numero: "))
numero2=int(input("ingresa el otro numero: "))

if numero1>numero2:
    print(f"el numero mayor es el primero :{numero1}")
elif numero2>numero1:
    print(f"el numero mayor es el segundo : {numero2}")
else :
    print("sus numero son iguales")


########################################################################3


#EJERCICIO 9
numero1=int(input("ingrese el primer numero: "))
numero2=int(input("ingrese el segundo numero: "))
numero3=int(input("ingrese el tercer numero: "))

if numero1>=numero2 and numero1>=numero3:
    print(f"el numero mayor es el primero: {numero1}")
elif numero2>=numero1 and numero2>=numero3:
    print(f"el numero mayor es el segundo: {numero2}")
else:
    print(f"el numero mayor es el tercero: {numero3}")


############################################################################


#EJERCICIO 10
numero1=float(input("ingresa el primer numero: "))
if numero1 > 0 :
    print("el numero es positivo")
if numero1<0:
    print("su numero es negativo")
if numero1==0:
    print("su numero es 0")


###############################################################################


#EJERCICIO 11
numero=int(input("ingrese el numero: "))
if numero % 2 == 0 :
    print("tu numero es par ")
else :
    print("tu numero es impar")


##################################################################################


#EJERCICIO 12
edad=int(input("ingrese su edad: "))
if edad==18:
    print("es mayor de edad y su edad exacta es 18")
if edad<18:
    print("es menor de edad")
if edad>18:
    print(f"es mayor de edad y su edad es {edad}")