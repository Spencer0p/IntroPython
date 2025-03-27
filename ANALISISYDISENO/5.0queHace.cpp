#include<iostream>//Esta línea incluye la biblioteca estándar <iostream>, que permite el uso de cout y cin para la entrada y salida de datos en la consola.

using namespace std;//Permite usar los elementos del espacio de nombres std sin necesidad de escribir std::cout, std::cin, etc.

int main(){//Define la función principal main(), que es el punto de inicio del programa.

	//DECLARACION DE VARIABLES
	
	int num1,num2,num3;//Declara tres variables enteras num1, num2, y num3, que almacenarán los números ingresados por el usuario.
	
	double prom;//Declara una variable de tipo double llamada prom, que almacenará el resultado del promedio.
	
	///DATOS DE ENTRADA
	cout<<"Ingrese Tres Numeros enteros: "<<endl;//Muestra en la consola el mensaje "Ingrese Tres Numeros enteros: ", pidiendo al usuario que ingrese tres números.
	
		cin>>num1>>num2>>num3;//Captura los tres números ingresados por el usuario y los almacena en num1, num2, y num3.
		
	//PRECESO MATEMATICO

	prom=(num1+num2+num3)/3;//En este cálculo, como num1, num2, y num3 son enteros, la división se realiza con enteros, lo que puede dar un resultado incorrecto si no se convierte a double. La solución sería escribir prom = (num1 + num2 + num3) / 3.0; para forzar una división con decimales.
	
	//DATOS DE SALIDA
	cout<<"El resultado es: "<<prom<<endl;//Muestra el resultado del promedio en la consola.
	
	
	
	
	return 0;//Indica que el programa terminó correctamente.


	
}