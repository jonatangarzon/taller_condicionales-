#programa para calcular el precio de venta de un producto
import math

#----------
#processing
#-----------

print("---------------------------------")
print("------ calcular el precio de venta de un producto")
print("-----------------------------------")

pc=int(input("Dijite el precio costo del producto: "))

#----------
#processing
#----------

if(pc<3000):
    pv=(pc*0.15)+pc

else: 
    if(pc>6000):
        pv=(pc*0.25)+pc

    else:
        pv=pc+500

#-----------
#output
#------------

print("-----------------------------")
print("----- Resulados-------")
print("---------------------------")
print("El precio de venta es: " +str(pv))
print("----------------------------------")