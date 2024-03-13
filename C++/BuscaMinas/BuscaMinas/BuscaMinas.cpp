#include <iostream>
#include <time.h>

#define MAX 32

using namespace std;

void mensaje();
int elegirNivel();
int elegirFilas(int level);
int elegirColumnas(int level);
int elegirMinas(int level);
void inicializaTablero(int row, int col, char space[MAX][MAX]);
void colocarMinas(int row, int col, char space[MAX][MAX], int minas);
void colocaNumeros(int row, int col, char space[MAX][MAX]);
void imprimeTablero(int jugadaFil, int jugadaCol,char space[MAX][MAX], char space2[MAX][MAX], int row, int col);
int verificaGanador(int row, int col, char space[MAX][MAX], int minas);

int main(){

    int level, row, col, min;//filas columnas minas
    int jugadaFila, jugadaColumna;
    int situacion;
    char space[MAX][MAX], space2[MAX][MAX];

mensaje();
level = elegirNivel();
row = elegirFilas(level);
col = elegirColumnas(level);
min = elegirMinas(level);
inicializaTablero(row, col, space);
colocarMinas(row, col, space2, min);
colocaNumeros(row, col, space2);
    
while (1) {
    cout << "Ingrese la coordenada de la fila y columna que desea voltear: ";
    cin >> jugadaFila >> jugadaColumna;
    if (jugadaFila > 0 && jugadaFila < row + 1 && jugadaColumna < col + 1 && jugadaColumna > 0) {
        imprimeTablero(jugadaFila, jugadaColumna, space, space2, row, col);
        situacion = verificaGanador(row, col, space, min);
        if (situacion == 1) {
            cout << "Usted Gano el Juego !!! ";
            break;
        }
        else if (situacion == 2) {
            cout << "Usted Perdió el Juego";
            break;
        }
    }
    else cout << "Valores incorrectos"<<  endl;
}

return 0;

}

void mensaje()
{
    cout << "Bienvenido a Buscaminas" << endl;
    cout << "Los niveles son: " << endl;
    cout << "<1> Nivel principiante" << endl;
    cout << "<2> Nivel intermedio" << endl;
    cout << "<3> Nivel avanzado" << endl;
    cout << "<4> Nivel personalizado" << endl;
}

int elegirNivel()
{
    int l;
    while (1) {
        cout << "Ingrese el nivel: ";
        cin >> l;
        if (l == 1)break;
        else if (l == 2)break;
        else if (l == 3)break;
        else if (l == 4)break;
    }
    return l;
}

int elegirFilas(int level)
{
    int fila;
    if (level == 1) fila = 8;
    else if (level == 2) fila = 16;
    else if (level == 3) fila = 16;
    else if (level == 4) {
        while (1) {
            cout << "Ingrese el numero de filas: ";
            cin >> fila;
            if (fila <= 30) break;
        }
    }
    return fila;
}   

int elegirColumnas(int level)
{
    int columna;
    if (level == 1) columna = 8;
    else if (level == 2) columna = 16;
    else if (level == 3) columna = 30;
    else if (level == 4) {
        while (1) {
            cout << "Ingrese el numero de columnas: ";
            cin >> columna;
            if (columna <= 30) break;
        }
    }
    return columna;
}

int elegirMinas(int level)
{
    int mina;
    if (level == 1) mina = 10;
    else if (level == 2) mina = 40;
    else if (level == 3) mina = 99;
    else if (level == 4) {
        while (1) {
            cout << "Ingrese el numero de minas: ";
            cin >> mina;
            if (mina <= 200) break;
        }
    }
    return mina;
}

void inicializaTablero(int row, int col, char space[MAX][MAX])
{
    for (int i = 0; i < row + 2; i++) {
        for (int j = 0; j < col + 2; j++) {
            space[i][j] = '0';
        }
    }

    cout << endl << "El tablero ha sido creado, puede emprezar a jugar" << endl;
    cout << "El tablero actual es: "<< endl << endl;

    for (int i = 1; i < row + 1; i++  ) {
        for (int j = 1; j < col + 1; j++) {
            cout << space[i][j];
        }
        cout << endl;
    }
}

void colocarMinas(int row, int col, char space[MAX][MAX], int minas)
{
    int pcol, pfil;
    for (int i = 0; i < row + 2; i++) {
        for (int j = 0; j < col + 2; j++) {
            space[i][j] = '0';
        }
    }
    srand(time(NULL));
    while(1) {
        pfil = 1 + rand() % row;
        pcol = 1 + rand() % col;
        if (space[pfil][pcol] == '0') {
            space[pfil][pcol] = 'M';
            minas--;
        }
        if (minas == 0) break;
    }
}

void colocaNumeros(int row, int col, char space[MAX][MAX])
{
    int number;
    for (int i = 1; i < row + 1; i++) {
        for (int j = 1; j < col + 1; j++) {
            if (space[i][j] == '0') {
                number = 0;
                if (space[i - 1][j] == 'M') number++;
                if (space[i - 1][j - 1] == 'M') number++;
                if (space[i - 1][j + 1] == 'M') number++;
                if (space[i][j - 1] == 'M') number++;
                if (space[i][j + 1] == 'M') number++;
                if (space[i + 1][j] == 'M') number++;
                if (space[i + 1][j - 1] == 'M') number++;
                if (space[i + 1][j + 1] == 'M') number++;

                if (number == 0) space[i][j] = ' ';
                else space[i][j] = number + '0';
            }
        }
    }
}

void imprimeTablero(int jugadaFil, int jugadaCol, char space[MAX][MAX], char space2[MAX][MAX], int row, int col)
{
    space[jugadaFil][jugadaCol] = space2[jugadaFil][jugadaCol];
    for (int i = 1; i < row + 1; i++) {
        for (int j = 1; j < col + 1; j++) {
            cout << space[i][j];
        }
        cout << endl;

    }



}

int verificaGanador(int row, int col, char space[MAX][MAX], int minas)
{
    int situacion = 0;
    int casillasFaltantes=0, cantMinas = 0;
    for (int i = 1; i < row + 1; i++) {
        for (int j = 1; j < col + 1; j++) {
            if (space[i][j] == 'M') cantMinas++;
            else if (space[i][j] == '0')casillasFaltantes++;
        }
    }

    if (cantMinas != 0) situacion = 2;//Situacion vale 2 el jugador pierde
    else if (casillasFaltantes == minas) situacion = 1;

    return situacion;
}
