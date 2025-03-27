#include<iostream>
using namespace std;
int main(){
	float area,num1,num2,perimetro;
	cout<<"\n Ingrese la base de su rectangulo \n";
	cin>>num1;
	cout<<"\n Ingrese la altura de su rectangulo \n";
	cin>>num2;
	area=(num1*num2);
	cout<<"EL area de su rectangulo es: "<<area<<"cm2"<<endl;
	perimetro=2*(num1+num2);
	
	cout<<"El perimetro de su rectangulo es: "<<perimetro<<endl;
	
	
	
	
	
	
	return 0;
}