#include <iostream>
using namespace std;
int main (){
	int num1,num2,suma;
	float numero1,numero2,multi,divicion;
	cout<<"\n Ingrese dos numeros entero: "<<endl;
	cin>>num1>>num2;
	suma=(num1+num2);
	cout<<"La su suma de dos numero esteros es: "<<suma<<endl;
	cout<<"\n Numero decimales a multiplicar\n "<<endl;
	cout<<"\n Ingrese dos numero decimales para multiplicar"<<endl;
	cin>>numero1>>numero2;
	multi=(numero1*numero2);
	cout<<"\n El resultado de la multiplicacion es: \n "<<multi<<endl;
	divicion =(num1/numero2);
	cout<<"\n El resultado del primero numero entero dividido con el segundo numero decimal es: "<<divicion<<endl;
	
	
	
	return 0;
}