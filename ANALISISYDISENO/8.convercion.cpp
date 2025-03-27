#include <iostream>
using namespace std;
int main (){
   float gradosfare,gradoscel;
   
   cout<<"\n Ingrese la temperatura en grados celcius \n";
   cin>>gradoscel;
   
   gradoscel = (gradoscel* 9/5)+32;
   
   cout<<"\n La convercion de su temperatura a fare es: \n "<<gradoscel<<"F"<<endl;	
	
	return 0;
}