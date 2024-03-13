/* function range (start,end){
    let arr = [];
    for(let i = start; i <= end; i++){
        arr.push(i);
    }
    return arr;
}

function suma (numeros){
    let sum = 0;
    for(let i = 0; i < numeros.length; i++){
        sum = sum + numeros[i];
    }
    return sum
}

console.log(suma(range(1,10))); */


/* function reverseArray (array) {
    let reversedArray = []; //Variable donde se guardara el nuevo array
    for (let i = array.length; i >= 0; i--){//Empieza en 5, termina en i 0, i va en retroceso
        reversedArray.push(array[i]);//Todo se agrega en reversedArray de acuedo a la condicion hacia array
    }
    return reversedArray;
}

let originalArray = [1,2,3,4,5];
let arrayreverso = originalArray;
console.log(reverseArray(arrayreverso));


function reversedArrayInPlace (array) {
    for (let i = 0; i < Math.floor(array.length / 2); i++) {//Cantidad en el array / 2, redondeado
        let oppositeIndex = array.length - 1 - i;// variable que equivale a cantidad del array - 1 - cantidad que del array que va
        let temp = array[i];
        array[i] = array[oppositeIndex];
        array[oppositeIndex] = temp
    }
    return array;
} 


let originalArrayInPlace = [1,2,3,4,5];
let reversoArrayInPlace = originalArrayInPlace;
console.log(reversedArrayInPlace(reversoArrayInPlace)); */


/* function arrayLista (array) {
    let lista = null;
    for (let i = array.length - 1; i >= 0; i--){
        lista = { value: array[i], rest: lista };
    }
    return lista;
} */

function listArray (lista) {
    let array = [];
    for (let node = lista; node; node = node.rest){
        array.push(node.value)
    }
    return listArray;
}

console.log(listArray([1,2,3,4]));
/* console.log(arrayLista([1,2,3])); */