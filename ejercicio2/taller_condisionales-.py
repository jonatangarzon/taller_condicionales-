# programa calcular costo de una llamada 

# input 
print("---------------------------------")
print("---------- costo de llamada --------")
print("---------------------------------")
x = int(input("dijite la duracion de la llamad en minutos: "))

# processing
if (min <= 3):
    costo_llamada = 500
else:
    costo_llamada = 500 +(min - 3)*100

# output
print("------------------------------------")
print("----------- resultado ----------------")
print("------------------------------------")
print("Duración de la llamada: " + str(min))
print("costo de la llamada: " + str(costo_llamada))