#Ejercicio: Escribe un programa que lea de la entrada estándar el precio 
#de un producto y muestre en la salida estándar el precio del producto al
#aplicarle el IVA.
# 12% IVA En honduras= 0.12
import os
os.system('cls' if os.name == 'nt' else 'clear')

Iva=0.12
    
pre=float(input("Ingrese Precio: "))
tt=pre*Iva
tt=pre+tt
print("El precio del producto al aplicarle el IVA es: L.", "{:.2f}".format(tt))