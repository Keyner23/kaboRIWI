#EJERCICIO 17

numero=int(input("ingrese su numero: "))

for i in range(1,10):
    resultado=numero*i
    

    print(f"{numero} x {i} : {resultado}")


###################################################


#EJERCICIO 18
numero=int(input("ingrese el numero: "))
total=0

for i in range (1, numero+1):
    total+=i

print(f"la suma de los numero es {total} ")


###################################################


#EJERCICIO 19
numero=int(input("ingrese su numero: "))
numero_total=int(input("ingrese su numero de pares: "))

for numero in range(1,numero_total+1):
    total=numero*2
    print(total)
       

#####################################################


#EJERCICIO 20
numero = int(input("Ingrese un número entero: "))
factorial = 1


for i in range(1, numero + 1):
  factorial = factorial * i 

print(f"El factorial de {numero} es {factorial}")