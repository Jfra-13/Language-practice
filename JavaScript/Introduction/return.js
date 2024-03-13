//FUNCIONES ggs
const suma = (suma1,suma2) => {
    return suma1 + suma2;
}
console.log(suma (2,5));

const printHello = () => {
    console.log('hello');
}
printHello();

const checkWeight = access => {
    console.log(`El peso maximo es ${access} kilogramos.`)
}
checkWeight(25);

const multiply = (a,b) => a*b;
console.log(multiply(2,3));

function sumita (sum1, sum2){
    return sum1 + sum2;
}
sumita(4,4);

function martRocket (){
    return 'Boom';
}

function rectangleArea(width,heigh) {
    if ((width > 0) && (heigh > 0)){
        const area = width * heigh;
        return area;
    } else {
        return 'Los digitos deben ser positivos!';
    }
}
console.log(rectangleArea(-5,4));

/* function numMonitors (rows, colums){
    return rows * colums;
}
const numOfMonitors = numMonitors(5,4);
console.log(`El numero de monitores totales es: ${numOfMonitors}.`);
 */

function numberOfMonitor (rows, columns){
    const numberOfMonitor = rows * columns;
    return numberOfMonitor;
}

function costMonitors(rows,columns){
    const  costMonitors = numberOfMonitor(rows,columns) * 200;
    return costMonitors;
}
const totalCost = costMonitors(4,5);
console.log(totalCost);

const waterInPlant = day =>{
    if (day === 'Monday'){
        return true;
    } else {
        return false;
    }
};

console.log(waterInPlant('Monday'))

const logSkyColor = () =>{
    let color = 'blue';
    console.log(color);
};
logSkyColor();




const groceryList = ['orange juice', 'bananas', 'coffee beans', 'brown rice', 'pasta', 'coconut oil', 'plantains'];

groceryList.shift();

console.log(groceryList);

groceryList.unshift('popcorn');

console.log(groceryList);

console.log(groceryList.slice(1, 4));

console.log(groceryList);

const pastaIndex = groceryList.indexOf('pasta');

console.log(pastaIndex);