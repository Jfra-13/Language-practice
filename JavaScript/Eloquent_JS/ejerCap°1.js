/* let cantDig = 7; //Declaramos la cant. de Digitos que queremos 
let figura = ""; // Declaracion vacia la cual nos servira mas adelante

for (let i = 0; i < cantDig ; i = i + 1){//i empezara en 0,i llegara hasta < 8,cerramos
    for (let j = 0; j < i + 1; j = j + 1){//i se suma 1,crea un nuevo valor con cada bucle,debe ser mayor que j
        figura+= "#";// actualizamos el valor de figura por el #
    }
    figura+= "\n";// creamos un salto de linea
}
console.log(figura);//Mostramos en consola

/*---------------------------------------------------------- */




/* for (let i = 1; i <= 100; i++){
    if (i % 15 === 0){
        console.log("FizzBuzz");

    } else if (i % 5 === 0){
        console.log("Buzz");

    } else if (i % 3 === 0){
        console.log("Fizz");

    } else{
        console.log(i);
        
    }
} */

/*---------------------------------------------------------- */



/* for (let i = 0; i < 8; i++){
    let row = '';
    for(let j = 0; j < 8; j++){
        if ((i + j) % 2 === 0){ // Si la suma de i y j es par , se agrega un #
            row = row + "#";
        } else {
            row += " ";// de lo contrario un espacio
        }
    }
    console.log(row);
} */

/*---------------------------------------------------------- */



