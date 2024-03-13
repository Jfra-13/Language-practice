#include <iostream>
using namespace std;
double suma(double a, double b);
void mostrar(double a);

int main() {
	double number1, number2, var;
	cout << "Ingrese dos numeros a sumar: ";
	cin >> number1 >> number2;

	var = suma(number1, number2);
	mostrar(var);
	return 0;
}

double suma(double a, double b) {
	double c;
	c = a + b;
	return c;
}

void mostrar(double a) {
	cout << "La suma es: " << a;
}
