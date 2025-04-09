import os
os.system('cls' if os.name == 'nt' else 'clear')

#Escriba un programa que lea las notas  de
#los alumnos y calcule el promedio de las cuatro notas.

print("El Programa Calcula el Promedio de cuatro notas")

n1 = float(input("Ingrese la primer nota: "))
n2 = float(input("Ingrese la segunda nota: "))
n3 = float(input("Ingrese la tercer nota: "))
n4 = float(input("Ingrese la cuarta nota: "))

prom = (n1 + n2 + n3 + n4) / 4
print("El promedio es:", prom, "%")
print("El promedio es:", "{:.2f}".format(prom), "%")
