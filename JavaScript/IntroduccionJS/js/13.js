//Array methods

const meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'];

const carrito = [
    { nombre: 'monitor 20 pulgadas', precio: 500},
    { nombre: 'Television 50 pulgadas', precio: 700},
    { nombre: 'Tablet', precio: 300},
    { nombre: 'Audifonos', precio: 200},
    { nombre: 'Teclado', precio: 50},
    { nombre: 'Celular', precio: 500},
    { nombre: 'Bocinas', precio: 300},
    { nombre: 'Laptop', precio: 800},
];

//forEach
meses.forEach(function(mes){
    if(mes == 'Marzo') {
        console.log('Marzo si existe');
    }
});

// Incluides
const resultado = meses.includes('Diciembre'); 

//Some ideal para arreglo de objetos
resultado = carrito.some(function(producto){
    return producto.nombre == 'Celular'
})
 //Reduce 
resultado = carrito.reduce(function(total, producto){
    return total + producto.precio
},0);

//Filter
resultado = carrito.filter(function(producto){
    return producto.precio > 400
})
console.log(resultado);