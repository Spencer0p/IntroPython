#Ejercicio 3: Realice un programa que lea de la entrada estándar los siguientes datos de una persona:
#Edad: dato de tipo entero.
#Sexo: dato de tipo carácter.
#Altura en metros: dato de tipo real.
#Tras leer los datos, el programa debe mostrarlos en la salida estándar.
import os
os.system('cls' if os.name == 'nt' else 'clear')

Edad=int(input("Ingrese Su Edad: "))
Sexo=input("Ingrese Su Sexo: ")
Altura=float(input("Ingrese Su Altura: "))
print("Su Edad: ",Edad)
print("Su Sexo: ",Sexo)
print("Su Altura: ",Altura)