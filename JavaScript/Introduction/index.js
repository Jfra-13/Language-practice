console.log('Hello!')//Mostrar en consola

console.log(Math.random())//Methods , devuelve numeros random entre 0 y 1

Math.random// es una libreria(Contienen metodos)

let mensaje = 'Good night';//String length -> devuelve el numero de caracteres
console.log(mensaje.length);
console.log('howdy'.length)

let JAIME = 19;//Booleans (Resultados de verdadero o falso)
    if (JAIME > 18){
        console.log(true)
    }

const semanasAño = Math.floor(365/7)
const diasExtra = (365 % 7) //Modulo operator -> sirve para dar a conocer el 'resto' de una divicion
console.log(`El año tiene ${semanasAño} semanas y ${diasExtra} dia.`)

let number = 50;
number = number + 10
number += 10; // Lo mismo que la linea 21 pero resumido, tmbn se puede usar "-=" "*=" "/="
console.log(number)

let años = 18;
console.log('Jaime tiene ' + años + ' de edad')
console.log(`Jaime tiene ${años} de edad`) // Interpolacion en cadenas, manera mas sencilla para leer codigo

const moneda = '$'; 
let transferencia = 4800
console.log(`Usted ingreso: ${moneda}${transferencia} al banco BCP`)

let nombre = "Maria";//let -> Definir variables mutables / Necesitamos especificar un valor / se exapande a nivel de estrucura contenedora
const encontrado = false;//const -> Define variables inmutables / No cambian a lo largo de nuestro trabajo
var edad = 18;//var -> Definir variables mutables / Su valor por defecto es Undefined / se expande a nivel de funcion 
console.log(nombre, encontrado, edad);

let count;
console.log(count);
count = 20;
console.log(count)

const numeroColumnas = 30; //No se puede reasignar valor , dara error en pantalla
/* numeroColumnas = 10;
console.log(numeroColumnas); */

let servicio = 'Tarjeta de credito';
let vencimiento = 'mayo 11';
let tramite = `Tu ${servicio} vencera en ${vencimiento} de este año.`;
console.log(tramite);


function dni(mayorEdad){//Comprueba los valores y devuelve un booleano , si uno o ambos valores son verdaderos devuelve true y si ambos son falsos, devuelve false
    if (mayorEdad >= 18 || mayorEdad < 17){
        console.log('Tienes la edad exacta para ingresar a nuestras instalaciones');
    } else {
        console.log('Solo ingresas acompañado');
    }
}
dni(17);

let precio = 10.5;
let dia = 'Lunes';
console.log((dia === 'Lunes') ? precio = precio + 1.5 : precio = precio - 1.5 );//Operador ternario, if y else pero resumido

const completo = false;
if (completo) {
    console.log('Completo')
} else { // El bloque else solo se cumple se la condicion es falsa o incorrecta
    console.log('Incompleto')
}

function iniciarSesion (correo, contraseña){
    if((correo === 'Juan@gmail.com') && (contraseña === 'JF23')){ // El operador && sirve para comprobar que dos o mas sentencias sean verdaderas para continuar
        console.log('Usuario y contraseña correcto');
    } else {
        console.log('Datos ingresados INCORRECTOS');
    }
}
iniciarSesion('Juan@gmail.com','JF23');

const food = 'Postres';
switch(food){ // Swich comprueba una expresion en varias clausulas , en el caso que coincida con una se ejecuta el codigo en su interior
    case 'Segundos':
        console.log('Tenemos una variedad de platos tipicos.');
        break;
    case 'Salad':
        console.log('Tenemos ensaladas frescas y cocidas.');
        break;
    case 'Postres':
        console.log('No contamos con postres en nuestro restaurante.');
        break;
    default:
        console.log('Esperamos cumplir con sus expectativas.')
}

const enviadoCorrectamente = true;
if (enviadoCorrectamente) { // Si la expresion es verdadera se ejecuta el codigo, siendo falsa no se ejecutara a menos que cuente con un else
    console.log ('El envio fue exitoso');
}

let tardeAlTrabajo = true;
let opositivo = !tardeAlTrabajo; // '= !' invierte un booleando e invierte la veracidad de los valores no booleanos
console.log(opositivo);

let estoyFueraDeCasa = true;
let enCasa = !estoyFueraDeCasa;
console.log(enCasa)

//Operadores de comparacion 
//=== Estricta igualdad
//!== Estricta desigualdad
//> Mas grande que
//< Menos que
//<= menor igual que 
//=> mayor igual que


