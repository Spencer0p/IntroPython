import os
os.system('cls' if os.name == 'nt' else 'clear')

# Arreglos con Paises
# Me base en el tema que expuse de arreglos, y logre realizar esto.
print("Ejercicio de arreglos con paises")
num=["504", "55", "33", "502"]
print("Seleccione un pais")
print("1. Honduras")
print("2. Brasil")
print("3. Francia")
print("4. Guatemala")
print("5. Salir")

opc= int(input("Ingrese una opcion: "))
if opc == 1:
    print("El codigo de Honduras es: ", num[0])
elif opc == 2:
    print("El codigo de Brasil es: ", num[1])
elif opc == 3:
    print("El codigo de Francia es: ", num[2])
elif opc == 4:
    print("El codigo de Guatemala es: ", num[3])
elif opc == 5:
    print("Saliendo del programa")
else:
    print("Opcion no valida")