//.ForEach()
// Ejecuta el mismo codigo para cada elemento de una matriz.
//Llamamos al metodo de la manera "groceries.forEach()", toma un
//argumento de la funcion de devolucion, recordemos que una
//funcion de devolucion de llamada es una funcion que se pasa como
//argumento a otra funcion


const groceries = ['brown sugar','salt','cranberries','walnuts'];

groceries.forEach(groceryItem => console.log('-' + groceryItem)); //Manera resumida con funcion flecha

/* groceries.forEach(function(groceryItem){ 
    console.log('-' + groceryItem);        
}); 
 */

const fruits = ['mango', 'papaya', 'pineapple', 'apple'];

fruits.forEach(newText => console.log(`I  want to eat a ${newText}`));

//---------------------------------------------------------------------------------------------------------

//.map()
//Toma un argumento de una funcion de devolucion de llamada y devuelve una nueva matriz

const numberss = [1,2,3,4,5];

const minBigNumbers = numberss.map(number => { //'numbers.map' iterará a través de 
    return number*10;                      //cada elemento de la matriz "numbers"
})
console.log(minBigNumbers.join(' '));
//Map y forEach funcionan de manera similar , la principal diferencia es que devuelve una matriz nueva



const animals = ['Hen', 'elephant', 'llama', 'leopard', 'ostrich', 'Whale', 'octopus', 'rabbit', 'lion', 'dog'];
const secretMessage = animals.map( words => {
    return words[0];
})
console.log(secretMessage.join(''));


const bigNumbers = [100, 200, 300, 400, 500];
const divNumbers = bigNumbers.map(div => div / 100);

/* const smallNumbers = bigNumbers.map(function(division){
    return division / 100;
}) */

/* const smallNumbers = bigNumbers.map(division => {
    return division / 100;
  }) */

console.log(divNumbers.join(' '));


//---------------------------------------------------------------------------------------------------------

//.filter() 
// Realiza una condicion y de acuerdo a que salga true o false, se agrega a la nueva matriz si es true
const words = ['chair', 'music', 'pillow', 'brick', 'pen', 'door']; 
const shortWords = words.filter(word => {
    return word.length < 6;
});
console.log(shortWords);


const randomNumbers = [375, 200, 3.14, 7, 13, 852];

/* const smallNumbers = randomNumbers.filter(newNumber => newNumber < 250); */

/* const smallNumbers = randomNumbers.filter(function(newNumber){
    return newNumber < 250;
})*/

const smallNumbers = randomNumbers.filter(randomNumbers => {
    return randomNumbers < 250;
})


console.log(smallNumbers);


const favoriteWords = ['nostalgia', 'hyperbole', 'fervent', 'esoteric', 'serene'];

const longFavoriteWords = favoriteWords.filter( newwords => {
    return newwords.length > 7;
})

/* const longFavoriteWords = favoriteWords.filter(function(newwords){
    return newwords.length > 7;
})
 */
/* const longFavoriteWords = favoriteWords.filter(newwords => newwords.length > 7); */

console.log(longFavoriteWords);

//---------------------------------------------------------------------------------------------------------

//.findIndex()
//Sirve para encontrar la ubicacion de un elemento en una matriz

const jumbledNums = [123, 25, 78, 5, 9];
const lessThanTen = jumbledNums.findIndex(num => num < 10); //Devuelve el primer elemento true
console.log(lessThanTen);


const animalss = ['hippo', 'tiger', 'lion', 'seal', 'cheetah', 'monkey', 'salamander', 'elephant'];

const foundAnimal = animalss.findIndex(animal => animal === 'elephant')
console.log(foundAnimal);

const startsWithS = animalss.findIndex(firstLetter => firstLetter[0] === 's');
console.log(startsWithS);

//.reduce()
//Devuelve un unico valor despues de iterar por la matriz logrando su reduccio

const numeros = [1, 2, 4, 10];

const summedNums = numeros.reduce((accumulator, currentValue) => {
    return accumulator + currentValue;
})
console.log(summedNums);

//'accumulator' comienza como el primer valor de la matriz
//'currentValue' segundo elemento , se conviente en el valor  actual y el bucle se ejecuta hasta pasar por toda la matriz
//Dato, se puede agregar al final del codigo  '}, 100)' un valor inicial

const newNumbers = [1, 3, 5, 7];
const newSum = newNumbers.reduce((acumulador,valorActual) => {
    console.log(`El valor de acumulador es ${acumulador}`);
    console.log(`El valor de valor actual es ${valorActual}`);
    return acumulador + valorActual;
},10)
console.log(newSum);

/* .forEach se usa para ejecutar el mismo codigo en cada elemento de una matriz, no cambia la matriz y devuelve 'Undefined'
.map ejecuta el mismo codigo en cada elementode una matriz y devuelve una matriz nueva con elementos actualizados
.filter verifica cada elemento en una matriz para ver si cumple con ciertos criterios y devuelve una nueva matriz con los elementos verdaderos
.findIndex devuelve el indice del primer elemento de una matriz que compla con la condicion, si ninguno cumple devuelve un -1
.reduce itera a traves de una matriz y toma los valores de los elementos devolviendo un valor unico */

/* funcion de orden superior acepta funciones de parametros y devuelve funciones
 */

