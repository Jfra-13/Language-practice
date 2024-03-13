#include <iostream>
using namespace std;

int main()
{   
    /*int number;
    while (1) {
        cout << "instruccion" << endl;
        cout << "ingrese un numero: ";
        cin >> number;
        if (number > 100) break;

    }*/


    /*int i = 0;
    while (i < 5) {
        cout << "Estudiante " << i + 1 << endl;
        i++;
    }*/


    /*for (int i = 0; i < 10; i++) {
        cout << i + 1 << endl;
    }*/


   
	/*int nota, estudiantes;
	double total = 0;

	cout << "Ingrese la cantidad de estudiantes: ";
	cin >> estudiantes;

	for (int i = 0; i < estudiantes; i++) {
		cout << "Ingrese la nota del alumno " << i + 1 << ": ";
		cin >> nota;

		total = total + nota;
	}

	cout << "El promedio de los alumnos es: " << total / estudiantes;*/


    int n, num, digito, inverso = 0;
    cout << "Ingrese un numero entero positivo: ";
    cin >> n;

    num = n;
    while (num > 0) {
        digito = num % 10;
        inverso = inverso * 10 + digito;
        num = num / 10;
    }

    if (n == inverso) {
        cout << "El numero ingresado es capicua";
    }
    else {
        cout << "El numero ingresado no es capicua";
    }
    return 0;
}

