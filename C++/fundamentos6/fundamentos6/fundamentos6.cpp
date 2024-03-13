#include <iostream>
using namespace std;

int main()
{

	/*int numbers[5];
	for (int i = 0; i < 5; i++) {
		cout << "Ingrese el numero " << i + 1 << ": ";
		cin >> numbers[i];
	}

	cout << "Sus numeros guardados son: " << endl;

	for (int i = 0; i < 5; i++) {
		cout << numbers[i] << endl;
	}*/



	//int matrix[3][5];
	//for (int i = 0; i < 3; i++) {
	//	for (int j = 0; i < 5; j++) {
	//		//matrix[i][j] = 15;
	//		cout << "Ingrese un numero: ";
	//		cin >> matrix[i][j];
	//	}
	//}

	//for (int i = 0; i < 3; i++) {
	//	for (int j = 0; j < 5; j++) {
	//		cout << matrix[i][j] << " ";
	//	}
	//	cout << endl;
	//}

	/*int arreglo[5], guardar;

	cout << "Introduzca los numeros a ordenar... "<< endl;

	for(int i = 0; i < 5; i++) {
		cout << "Ingrese el numero " << i + 1 <<": ";
		cin >> arreglo[i];
	}

	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			if (arreglo[j] > arreglo[j+1]) {
				guardar = arreglo[j];
				arreglo[j] = arreglo[j + 1];
				arreglo[j + 1] = guardar;
			}
		}
	}

	for (int i = 0; i < 5; i++) {
		cout << arreglo[i] << endl;
	}*/


	int* var1;//Arreglo unidimencional 
	int estudiante, curso;
	var1 = new int[estudiante];

	int** var2;
	var2 = new int* [estudiante];

	for (int i = 0; i < estudiante; i++) {
		var2[i] = new int[curso];
	}





}
