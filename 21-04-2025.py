#EJERCICIO 1
#numero_entero = int (input("ingrese el numero: "))
#print(f"el numero digitado es {numero_entero}")


#EJERCICIO 2
#nombre=input("ingrese su nombre: ")
#edad=input("ingrese su edad: ")
#print(f"hola {nombre} tienes {edad} años")

#EJERCICIO 3
#numero1=int(input("ingrese el primer numero: "))
#numero2=int(input("ingrese el segundo numero: "))
#suma=numero1 + numero2

#print(f"la suma de los numeros es: {suma}")

#EJERCIO 4
#numero3=int(input("ingrese el primer numero: "))
#numero4=int(input("ingrese el segundo numero: "))
#resta=numero3 - numero4
#print(f"la resta de los numeros es: {resta}")

#EJERCICIO 5
#numero5=int(input("ingrese el primer numero: "))
#numero6=int(input("ingrese el segundo numero: "))
#multiplicacion=numero5 * numero6
#print(f"la multiplicacion de los numeros es: {multiplicacion}")

#EJERCICIO 6
#numero7=int(input("ingrese el primer numero: "))
#numero8=int(input("ingrese el segundo numero: "))
#division=int(numero7 / numero8)
#print(f"la division de los numeros es: {division}")

#EJERCICIO 7
#nota_1= float (input("ingrese la primera nota: "))
#nota_2= float (input("ingrese la segunda nota: "))
#nota_3= float (input("ingrese la tercera nota: "))
#promedio=(nota_1+nota_2+nota_3)/3
#print(f"el promedio de las notas es : {promedio}")


#EJERCICIO 10
#numero1=float(input("ingresa el primer numero: "))
#if numero1 > 0 :
#    print("el numero es positivo")
#if numero1<0:
#    print("su numero es negativo")
#if numero1==0:
#    print("su numero es 0")


#EJERCICIO 11
#numero=int(input("ingrese el numero: "))
#if numero % 2 == 0 :
#    print("tu numero es par ")
#else :
#    print("tu numero es impar")


#EJERCICIO 12
#edad=int(input("ingrese su edad: "))
#if edad==18:
#    print("es mayor de edad y su edad exacta es 18")
#if edad<18:
#    print("es menor de edad")
#if edad>18:
#    print(f"es mayor de edad y su edad es {edad}")

#EJERCICIO 13
#maximo=int(input("ingrese el numero: "))
#contador=1
#while contador<maximo:
#    print(contador)
#    contador+=1


#EJERCICIO 15
#secreto=10
#numero=int(input("ingrese el numero: "))

#while numero != secreto:
#    numero=int(input("ingrese el numero: "))


#EJERCICIO 16 
#contraseña=1044
#clave=int(input("ingrese la contraseña en numeros : "))

#while clave != contraseña:
#    clave=int(input("ingrese la contraseña en numeros : "))


#EJERCICIO 8
#numero1=int(input("ingrese el numero: "))
#numero2=int(input("ingresa el otro numero: "))

#if numero1>numero2:
#    print(f"el numero mayor es el primero :{numero1}")
#elif numero2>numero1:
#    print(f"el numero mayor es el segundo : {numero2}")
#else :
#    print("sus numero son iguales")


##############################################################################################################################################################################

#numero=int(input("ingrese su numero: "))

#for i in range(1,10):
#    resultado=numero*i
    

#    print(f"{numero} x {i} : {resultado}")


#numero=int(input("ingrese el numero: "))
#total=0

#for i in range (1, numero+1):
#    total+=i

#print(f"la suma de los numero es {total} ")




#numero=int(input("ingrese su numero: "))
#numero_total=int(input("ingrese su numero de pares: "))

#for numero in range(1,numero_total+1):
#    total=numero*2
#    print(total)
       





#numero = int(input("Ingrese un número entero: "))
#factorial = 1


#for i in range(1, numero + 1):
#  factorial = factorial * i

#print(f"El factorial de {numero} es {factorial}")

suma = 0

while True:
    numero = int(input("Ingrese un número (ingrese 0 para finalizar): "))
    if numero == 0:
        break
    suma += numero

print("La suma total es:", suma)




