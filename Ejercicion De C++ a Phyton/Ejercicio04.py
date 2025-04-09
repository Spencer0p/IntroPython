import os
os.system('cls' if os.name == 'nt' else 'clear')

# Ejercicio: Escribe la siguiente expresión como expresión: (a/b) + 1

print("El Programa Realizara esto: (a/b)+1")
a=float(input("Ingrese el valor de a: "))
b=float(input("Ingrese el valor de b: "))

resultado=(a/b)+1
print("El resultado de la expresión es:", resultado)