##funcion cuadratica
def cuadratica (a,b,c):
    ##x1
    x1=(-b+(b**2-4*a*c)**0.5)/(2*a)
    ##x2
    x2=-(b-(b**2-4*a*c)**0.5)/(2*a)
    ##imprimir resultados
import os
os.system('cls' if os.name == 'nt' else 'clear')

##Funcion cuadratica
def cuadratica(a,b,c):
    ## x1
    x1=(-b+(b**2-4*a*c)**0.5)/(2*a)
    ## x2
    x2=(-b-(b**2-4*a*c)**0.5)/(2*a)

    # imprimir las soluciones
    print(f"x1={x1}") 
    print(f"x2={x2}")

##programa

print("Ecuacion cuadratica aX^2+bX+c=0")
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
cuadratica(a,b,c)