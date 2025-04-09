# Description: Ejemplos de condicionales en Python
# cono truncado
# Programa que calcula el area y volumen de un cono truncado
# Esfera
# Programa que calcula el area y volumen de una esfera
# Cilindro
# Programa que calcula el area y volumen de un cilindro

#Programa que calcula el Volumen y area de Esfera
import os
os.system('cls' if os.name == 'nt' else 'clear')

print("Programa que calcula el area y volumen de una esfera")
print("Formula de area A=4πr2")

PI= 3.1416
r=float(input("Ingrese el radio de la esfera: "))
A=4*PI*r**2
print("El area de la esfera es: ", A)

print("Formula de volumen V=4/3πr3")
V=(4/3)*PI*r**3
print("El volumen de la esfera es: ", V)

# Programa que calcula el area y volumen de un cono truncado

print("Programa que calcula el area y volumen de un cono truncado")
print("Formula de area A=π(r1+r2)*√((r1-r2)2+h2)")

PI=3.1416
r1=float(input("Ingrese el radio mayor: "))
r2=float(input("Ingrese el radio menor: "))
h=float(input("Ingrese la altura: "))

A=PI*(r1+r2)*((r1-r2)**2+h**2)**0.5
print("El area del cono truncado es: ", A)

print("Formula de volumen V=1/3*π*h*(r12+r1*r2+r22)")
V=(1/3)*PI*h*(r1**2+r1*r2+r2**2)
print("El volumen del cono truncado es: ", V)

# Programa que calcula el area y volumen de un cilindro

print("Programa que calcula el area y volumen de un cilindro")
print("Formula de area A=2πr(r+h)")
PI=3.1416
r=float(input("Ingrese el radio: "))
h=float(input("Ingrese la altura: "))
A=2*PI*r*(r+h)
print("El area del cilindro es: ", A)
print("Formula de volumen V=πr2*h")
V=PI*r**2*h
print("El volumen del cilindro es: ", V)