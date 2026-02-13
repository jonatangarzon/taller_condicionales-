# programa para verificar si un programa es numero positivo o negativo o cero

#librerias
import math

#-----
#input 
#-----

print("--------------------------------------------------------------")
print("------ verificar si u numero es positivo, negativo o cero-----")
print("--------------------------------------------------------------")

x=int(input("Dijite el valor de x: "))

#processing 

if(x>0):
    Rta= "positivo"

else:
    Rta= "negativo o cero"

#-------
#output
#-------

print("--------------------")
print("----- RESULTADOS----")
print("--------------------")
print("El valor de x es: " +str(Rta))
print("-----------------------------")