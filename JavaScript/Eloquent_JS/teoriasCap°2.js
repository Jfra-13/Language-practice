//Funciones

/* const  hacerSonido = function (){
    console.log("Pling!!");
}
hacerSonido(); */


//Codigo que calcule la potencia
/* const potencia = function(base,potencia){ // Declaramos la varaible y la funcion con sus parametros
    let resultado = 1;
    for(let cuenta = 0; cuenta < potencia; cuenta++){//La cuenta empieza en 0 y termina en 10
        resultado = resultado * base;// Se ira multiplicando 10 veces el resultado por si mismo hasta que sea 10
    }
    return resultado;
}
console.log(potencia(2,10)); */


/* let x = 10;
if(true){
    let y = 20;// Solo funciona en su entorno global
    var z = 30; //Puede salir de un cuerpo interno y ser escuchada por el exterior
    console.log(x + y + z);
}

console.log( x + z ); */


/* const dividirEnDos = function(numero) {
    return numero / 2;
}

let numero = 10;
console.log(dividirEnDos(100));
console.log(numero); */

/* const humus = function(factor) {
    
    const ingrediente = function(cantidad, unidad, nombre) {
    let cantidadIngrediente = cantidad * factor;
        if (cantidadIngrediente > 1) {
            unidad += "s";
        }
        console.log(`${cantidadIngrediente} ${unidad} ${nombre}`);
    };
    ingrediente(1, "lata", "garbanzos");
    ingrediente(0.25, "taza", "tahini");
    ingrediente(0.25, "taza", "jugo de limón");
    ingrediente(1, "clavo", "ajo");
    ingrediente(2, "cucharada", "aceite de oliva");
    ingrediente(0.5, "cucharadita", "comino");
}; */


/* function menos(a,b){
    if(b === undefined){
        return a
    } else {
        return a - b
    }
}    
console.log(menos(50,60)) */

/* function potencia(base, exponente = 2) {
    let resultado = 1;
    for (let cuenta = 0; cuenta < exponente; cuenta++){
        resultado = resultado * base
    }
    return resultado
}
console.log(potencia(2)); */

/* 
function envolverValor(n){
    let local = n;
    return () => local ;
}
let envolver1 = envolverValor(1);
let envolver2 = envolverValor(2);

console.log(envolver1());
console.log(envolver2()); */


/* function multiplicador (factor) {
    return numero => numero * factor
}

let duplicar = multiplicador(2);

console.log(duplicar(5)); */


/* function potencia(base, exponente){
    if (exponente == 0){
        return 1
    } else {
        return base * potencia(base, exponente -1);
    }
}
console.log(potencia(3,3)); */

/* function encontrarSolucion(objetivo){
    function encontrar(actual, historia){
        if (actual == objetivo) {
            return historia;
        } else if (actual > objetivo) {
            return null;
        } else {
            return encontrar(actual + 5, `(${historia} + 5)`) ||
                    encontrar(actual * 3, `(${historia} * 3)`);
        }
    }
    return encontrar(1,"1");
}
console.log(encontrarSolucion(9)); */


/* function imprimirInventarioGranja(vacas,pollos){
    let stringVaca = String(vacas);
    while(stringVaca.length < 3){
        stringVaca = "0" + stringVaca;
    }
    console.log(`${stringVaca} Vacas`);

    let stringPollos = String(pollos);
    while(stringPollos.length < 3){
        stringPollos = "0" + stringPollos
    }
    console.log(`${stringPollos} Pollos`);
}
imprimirInventarioGranja(7,99); */


/* function imprimirEtiquetaAlcochadaConCeros(numero,etiqueta){
    let stringNumero = String(numero);
    while(stringNumero.length < 3){
        stringNumero = "0" + stringNumero;
    }
    console.log(`${stringNumero} ${etiqueta}`);
}

function imprimirInventarioGranja(vacas,pollos,cerdos){
    imprimirEtiquetaAlcochadaConCeros(vacas,"Vacas");
    imprimirEtiquetaAlcochadaConCeros(pollos,"Pollos");
    imprimirEtiquetaAlcochadaConCeros(cerdos,"Cerdos");
}

imprimirInventarioGranja(3,6,9);
 */

/* function alcocharConCeros(numero, amplitud){
    let string = String(numero);
    while(string.length < amplitud){
        string = "0" + string;
    }
    return string;
}

function imprimirInventarioGranja(vacas,pollos,cerdos){
    console.log(`${alcocharConCeros(vacas, 3)} Vacas`);
    console.log(`${alcocharConCeros(pollos, 3)} Pollos`);
    console.log(`${alcocharConCeros(cerdos, 3)} Cerdos`);
}

imprimirInventarioGranja(1,16,23); */













































