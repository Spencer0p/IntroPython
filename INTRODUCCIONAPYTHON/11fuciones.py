#funciones en python
import os
os.system('cls' if os.name =='nt' else 'clear')

def suma(a,b):
    return a+b
def resta(a,b):
    return a-b

# funciones en phyton
import os
os.system('cls' if os.name == 'nt' else 'clear')

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def division(a,b):
    return a/b

def potencia(a,b):
    return a**b

# operaciones aritmeticads

print("operaciones artitmeticas")
x=int(input("a: "))
y=int(input("b: "))

# s=suma(x,y)
print(f"{x}+{y}={suma(x,y)}")
print(f"{x}-{y}={resta(x,y)}")
print(f"{x}*{y}={multiplicacion(x,y)}")
print(f"{x}/{y}={division(x,y)}")
print(f"{x}^{y}={potencia(x,y)}")

