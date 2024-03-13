#include <iostream>
#include <math.h>
#define PI 3.14

using namespace std;

int main()
{
    double radio;
    cout << "Ingrese el radio del circulo: ";
    cin >> radio;

    cout << "El diametro del circulo es: " << 2 * radio * PI << endl;
    cout << "El area es: " << PI * pow(radio, 2);
    
}
