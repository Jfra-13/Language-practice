#include <iostream>
using namespace std;

//void llenarMatriz(int row, int col, int a[50][50]);
//void sumarMatriz(int a[50][50], int b[50][50], int c[50][50]);
//
//void mostrarMatriz(int row, int col, int a[50][50]);
//
//int main() {
//
//	int mat1[50][50], mat2[50][50], matRes[50][50];//Definimos la matrices a sumar y resultante
//	int row, col;// Varibales donde guardaremos las filas y columnas
//
//	cout << "Ingrese un numero de filas";
//	cin >> row;
//	cout << "Ingrese un numero de columnas";
//	cin >> col;
//
//	cout << "Ingrese los valores de la primera matriz: " << endl;
//	llenarMatriz(row, col, mat1);//LLenaremos la mat1
//	cout << "Ingrese los valores de la segunda matriz: " << endl;
//	llenarMatriz(row, col, mat2);//Llenaremos la mat2
//
//	sumarMatriz(mat1, mat2, matRes);//Realizamos el proceso de suma
//	cout << "La suma de las matrices es: " << endl;
//	mostrarMatriz(row, col, matRes);//Mostraremos el resultado en consola
//
//	return 0;
//
//}
//
//void llenarMatriz(int row, int col, int a[50][50])//Parametros de cada fila, columna y donde se agregara todo
//{
//	for (int i = 0; i < row; i++) {
//		for (int j = 0; j < col; j++) {
//			cout << "Ingrese un numero para la posicion [" << i << "]""[" << j << "]: ";
//			cin >> a[i][j];
//		}
//	}
//}
//
//void sumarMatriz(int a[50][50], int b[50][50], int c[50][50])//Parametros
//{
//	for (int i = 0; i < 50; i++) {
//		for (int j = 0; j < 50; j++) {
//			c[i][j] = a[i][j] + b[i][j];//suma de ambas matrices
//		}
//	}
//}
//
//void mostrarMatriz(int row, int col, int a[50][50])
//{
//	for (int i = 0; i < row; i++) {
//		for (int j = 0; j < col; j++) {
//			cout << a[i][j]<< " ";
//		}
//		cout << endl;
//	}
//}

int main() {
    int num, negativos = 0;

    for (int i = 1; i <= 5; i++) {
        cout << "Ingrese un número: ";
        cin >> num;
        if (num < 0) {
            negativos++;
        }
    }

    cout << "El número de valores negativos es: " << negativos << endl;
    return 0;
}
