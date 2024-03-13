/* let ouch = "ouch";
console.log(typeof ouch.toUpperCase);
console.log(ouch.toUpperCase());

let secuencia = [1,2,3];
secuencia.push(4);
secuencia.push(5);
console.log(secuencia);

console.log(secuencia.pop());
console.log(secuencia); */


/* let dia1 = {
    ardilla: false,
    eventos: [
        "trabajo",
        "toque un arbol",
        "pizza",
        "salir a correr"
    ]
};

dia1.lobo = false
console.log(dia1.lobo); */


/* let unObjeto = { izquierda: 1, derecha: 2 };
delete unObjeto.izquierda;
console.log("derecha" in unObjeto); */

/* console.log(Object.keys({x: 0, y: 0, z:2})); */

/* let objetoA = { a: 1, b: 2};
Object.assign(objetoA, {b: 3, c: 4});
console.log(objetoA); */

/* let diario = [
    {eventos: ["trabajo", "toque un arbol","pizza","sali a correr", "television"],
    ardilla: false},
    {eventos: ["trabajo", "helado", "coliflor","lasaña","toque un arbol", "me cepille"],
    ardilla: false},
    {eventos: ["fin de semana", "monte bici", "descanso", "nueces", "cerveza"],
    ardilla: true}
];
console.log(diario);
 */

/* puntuacion = {visitante:0, locales: 0};
puntuacion.visitante = 1
console.log(puntuacion)  */

/* let  diario = [];

function añadirEntrada(eventos,ardilla) {
    diario.push({eventos,ardilla});
}

añadirEntrada(["trabajo", "toque un arbol", "pizza", "television"],false);
añadirEntrada(["trabajo", "helado", "coliflor", "lasaña"],false);
añadirEntrada(["fin de semna", "monte bici", "descanso","nueces"],true);

console.log(diario); */


/* function remover(array, indice){
    return array.slice(0,indice)// 0 a 2 , no agarra el 2 solo es 0 y 1
        .concat(array.slice(indice + 1));// indice(2 + 1) agarra el 3 y 4 
}//En el caso que no se pong aun final , te trae todo a partir de ese digito
console.log(remover(["a","b","c","d","e"],2));
 */

/* console.log("   okey 123".trim()) */
/* console.log(String(6).padStart(3,"0")); */

/* let oracion = "Los pajaros secretarios se especializan en pisotear";
let palabras = oracion.split(" "); */
/* console.log(palabras); */
/* console.log(palabras.join(" ")); */

/* let string = "abc";
console.log(string[1]); */

/* function maximo(...numeros){
    let resultado = -Infinity;
    for (let numero of numeros){ 
        if (numero > resultado) resultado = numero;
    }
    return resultado;
}
console.log(maximo(4,1,9,-2));
 */

/* let palabras = [ "nunca", "entenderas" ];
let unir = ["tu", ...palabras , "completamente"];
console.log(unir.join(" ")); */

console.log(Math.floor(Math.random()*10));






