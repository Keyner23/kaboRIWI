#EJERCICIO 5
contraseña=input ("ingrese la contraseña a crear:")
caracter="@"
    
if len(contraseña) >= 8:
 if caracter in contraseña:
  print("Contraseña creada exitosamente")
 else:
  print("falta el caracter")
else:
 print("contraseña muy corta")