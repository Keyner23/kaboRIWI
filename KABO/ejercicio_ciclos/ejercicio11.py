
#CICLO WHILE...
#maximo=0
#positivo=0
#print("EJERCICIO 11 CON WHILE")
#while maximo<5:
#    numero=int(input("ingrese su numero: "))
#    maximo+=1
#    if numero % 2==0:
#        positivo+=1
#print(f"hay {positivo} numeros pares")


#CICLO FOR...
maximo=0
positivo=0
print("EJERCICIO 11 CON FOR")
for i in range(0,5):
    numero1=int(input("ingrese su numero: "))
    maximo+=1
    if numero1 % 2==0:
        positivo+=1
print(positivo)
