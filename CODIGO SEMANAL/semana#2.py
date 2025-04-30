despliegue=""
while despliegue!="salir":
    despliegue=input("Quieres desplegar las opciones?(Si/No)")
    if despliegue=="si":
        print("____________________________________________________")
        print("1.""Determinar el estado de aprobacion.")
        print("2.""Calcular el promedio.")
        print("3.""Contar calificaciones mayores.")
        print("4.""Verificar y contar calificaciones especificas.")
        print("5.""Salir")
        print("____________________________________________________")
        
        opcion=input("Ingrese la opcion que desee: ")
        if opcion=="1":
            print("")
            print("DETERMINAR EL ESTADO DE APROBACION...")

            nota1=float(input("Ingrese una calificacion en el rango de (0-100): "))
            print("")
            if nota1>70:
                print("Usted ha aprobado la asignatura.")
            else:
                print("Usted ha reprobado la asignatura.")
            print("____________________________________________________")


        if opcion=="2":
            print("")
            print("CALCULAR PROMEDIO DE CALIFICACIONES...")

            lista_calificaciones=[]
            numero_notas=0
            contador=0
            cantidad_notas=int(input("Ingrese la cantidad de notas que desea escribir: "))

            while contador<cantidad_notas:
                calificacion=float(input("Ingrese su nota: "))
                lista_calificaciones.append(calificacion)
                contador+=1
            print("")
            print(lista_calificaciones)
            print("____________________________________________________")


        if opcion=="3":
            print("")
            print("CONTAR CALIFICACIONES MAYORES...")

            valor_especifico=int(input("Ingrese la nota que desee comparar: "))
            lista_notas=[]
            cantidad2=int(input("Ingrese la cantidad de notas que desea comparar: "))
            cont=0
            mayor=0

            while cont<cantidad2:
                nota=float(input("Ingrese la nota: "))
                lista_notas.append(nota)
                cont+=1
                if nota>valor_especifico:
                    mayor+=1
            print("")
            print(f"La lista de notas que ha ingresado es {lista_notas}")
            print("")
            print(f"Hay {mayor} numeros mayores a {valor_especifico}")
            print("____________________________________________________")


        if opcion=="4":
            print("opcion 4")



        if opcion=="5":
            exit()
    elif despliegue=="no":
        exit()