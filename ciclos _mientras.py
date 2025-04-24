#EJERCICIO 13
maximo=int(input("ingrese el numero: "))
contador=1
while contador<maximo:
    print(contador)
    contador+=1


##################################################

#EJERCICIO 14
suma = 0

while True:
    numero = int(input("Ingrese un número (ingrese 0 para finalizar): "))
    if numero == 0:
        break
    suma += numero

print("La suma total es:", suma)


##########################################################


#EJERCICIO 15
secreto=10
numero=int(input("ingrese el numero: "))

while numero != secreto:
    numero=int(input("ingrese el numero: "))


##################################################


#EJERCICIO 16 
contraseña=1044
clave=int(input("ingrese la contraseña en numeros : "))

while clave != contraseña:
    clave=int(input("ingrese la contraseña en numeros : "))