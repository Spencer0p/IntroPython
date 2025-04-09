import os
os.system('cls' if os.name == 'nt' else 'clear')

#Escribe un programa que intercambie los valores de dos variables.

print("El Programa Intercambiara los valores de x e y")
x=int(input("Ingrese el valor de x: "))
y=int(input("Ingrese el valor de y: "))
# Intercambiando los valores de x e y
aux = x
x = y
y = aux
print("El valor de x es:", x)
print("El valor de y es:", y)