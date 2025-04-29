edad=int(input("ingrese su edad:"))

if edad <18:
    print("Usted es menor de edad")
elif edad >=18 and edad <=30:
    print("Usted es un adulto joven")
elif edad >=31 and edad<=65:
    print("Usted es un adulto maduro")
else:
    print("Usted es un adulto mayor")
