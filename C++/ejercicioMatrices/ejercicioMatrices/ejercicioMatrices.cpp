#include <iostream>
using namespace std;

void llenarMatriz(int row, int col, int a[50][50]);
void multiMatriz(int a[50][50],int b[50][50],int c[50][50]);
void mostrarMatriz(int row, int col, int a [50][50]);

int main() {

	int mat1[50][50], mat2[50][50], martRes[50][50];
	int row, col;

	cout << "Ingrese la cantidad de filas: ";
	cin >> row;
	cout << "Ingrese la cantidad de columnas: ";
	cin >> col;

	cout << "Ingrese los valores de la primera matriz: " << endl;
	llenarMatriz(row, col, mat1);
	cout << "Ingrese los valores de la segunda matriz: " << endl;
	llenarMatriz(row, col, mat2);

	multiMatriz(mat1, mat2, martRes);
	cout << "La multiplicacion de las matrices es: " << endl;
	mostrarMatriz(row, col, martRes);

	return 0;

}

void llenarMatriz(int row, int col, int a[50][50])
{
	for (int i = 0; i < row; i++) {
		for (int j = 0; j < col; j++) {
			cout << "Ingrese un numero para la posicion [" << i << "][" << j << "]: ";
			cin >> a[i][j];
		}
	}
}

void multiMatriz(int a[50][50],int b[50][50],int c[50][50])
{
	for (int i = 0; i < 50; i++) {
		for (int j = 0; j < 50; j++) {
			c[i][j] = a[i][j] * b[i][j];
		}
	}
}

void mostrarMatriz(int row, int col, int a[50][50])
{
	for (int i = 0; i < row; i++) {
		for (int j = 0; j < col; j++) {
			cout << a[i][j]<< " ";
		}
		cout << endl;
	}
}




