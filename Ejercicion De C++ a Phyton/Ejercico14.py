import os
os.system('cls' if os.name == 'nt' else 'clear')

# Operaciones Aritmeticas

n1=int(input("Ingrese Primer Numero: "))
n2=int(input("Ingrese Segundo Numero: "))

suma=n1+n2
resta=n1-n2
multi=n1*n2
divi=n1/n2
print(n1,"+",n2,"=",suma)
print(n1,"-",n2,"=",resta)
print(n1,"x",n2,"=",multi)
print(n1,"/",n2,"=",divi)