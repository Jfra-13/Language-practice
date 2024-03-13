//Arreglos o arrays
const numeros = [10,20,30,40,50];
console.table(numeros);



//Acceder valores de un arreglo
/* console.log(numeros[4])
console.log(numeros[2])
console.log(numeros[200])

//Conocer la extension
console.log(meses.length); */

/* numeros.forEach( function(numeros){
    console.log(numeros)
}) */

numeros.push(60,80,90); //final del arreglo
numeros.unshift(-10,-20,-30);//inicio del arreglo

console.table(numeros)

const meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'];

/* meses.pop()//elimina el ultimo elemento
meses.shift()//elimina el primer elemento

meses.splice(2,1)
console.table(meses); */

//Rest Operator p Spread Operator

const nuevoArreglo = [...meses, 'Junio'];
console.log(nuevoArreglo)

.filter