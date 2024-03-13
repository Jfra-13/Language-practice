function mensaje() {
    var saludo = 'Hola';
    var antisaludo = 'No me hables';
    var contento = true;

    if (contento === true) {
        console.log(saludo);

    } else {
        console.log(antisaludo);
    }
}

mensaje();
/* ----------------------------- */

function abrirPuerta () {
    var abrir = 'Identificacion confirmada'
    var cerrar = 'Desconocido'
    var confirmacion = true

    if (confirmacion === true){
        console.log(abrir);
    } else {
        console.log(cerrar);
    }
}

abrirPuerta();
/* ----------------------------- */

function passwordCorrect () {
    var correcta = 'confirmado' 
    var incorrecta = 'negado' 
    var verificador = true 

    if (verificador === true){
        console.log(correcta);
    } else {
        console.log(negado);
    }
}

passwordCorrect()
/* ----------------------------- */

var nombres = ['Juanito','Jaime','Javi'];

function mensaje(nombres){
    console.log(`Hola, ${nombres} buenos dias`);
}

nombres.forEach(function(valor){
    mensaje(valor);
})

var productos = ['Leche','huevos','Azucar'];
function enStock(productos){
    console.log(`El producto ${productos} se encuentra en Stock`);
}
productos.forEach(function(valor){
    enStock(valor)
})
/* ----------------------------- */
var coche  = {
    nombre: 'F-150',
    marca: 'Ford',
    motor: 'Gasolina',
    acelerar: function (){
        console.log(`Brrrrrrrrrrrrrrrrrr`);
    }

};
/* ----------------------------- */

var encabezado = document.querySelector("title");
encabezado.textContent = 'Esta es una prueba';

/* ----------------------------- */

function cambiacolor() {
    this.classList.toggle("cambia");
}
document.querySelector("body").addEventListener("click",cambiacolor)