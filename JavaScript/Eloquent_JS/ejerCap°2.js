/* function EncuentraMin (a,b){
    console.log(Math.min(a,b))
    
}
EncuentraMin(9,7) */


/* function esEnteroPositivoPar (param){
    if(!Number.isInteger(param) && param <= 0){
        console.log(`Ingrese un numero entero positivo`)
    } else {
        esEnteroPositivoPar (param = true)
    }
}

esEnteroPositivoPar(4); */


/* function esPar (num){
    if (num === 0){
        return true;
    } else if (num === 1){ 
        return false;
    } else {
        return esPar(Math.abs(num)- 2);//Llamara esPar y la restara hasta que el resultado sea 1 o 0
    }
}

console.log(esPar(2)); */


/* function contarFs(string){//
    return countCharacters(string, "F")//retornamos una nueva funcion con el parametro mas otro con lo que queremos que es las "F"
}

function countCharacters(string, character) {//nueva funcion con el primer parametro y character como "F"
    let count = 0;
    for(let i = 0; i < string.length; i++){//En el bucle la cuenta se repetira hasta que i pase por todo el string ingresado
        if(string[i] === character){// Se busca dentro del string hay alguna letra  "F" 
            count = count + 1;//Se guarda la cuenta hasta el final del recorrido  
        }
    }
    return count; //Retorna la cantidad de valores "F" que existan 
}


console.log(contarFs("Fermando Famacio de Fimera")); */
