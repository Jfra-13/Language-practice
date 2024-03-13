//POO+

/* Object Literal */
/* const producto = {
    nombre: 'tablet',
    precio: 500
} */


/* object constructor */







function Cliente(nombre,apellido){
    this.nombre = nombre;
    this.apellido = apellido;
}
function Producto(nombre,precio,disponible) {
    this.nombre = nombre;
    this.precio = precio;
    this.disponible = disponible
}
//crear funciones que solo se utilizan en un objeto en especifico
Cliente.prototype.formatearCliente = function() {
    return`El nombre del cliente es ${this.nombre} ${this.apellido}`;
}
Producto.prototype.formatearProducto = function() {
    return `El producto ${this.nombre} tiene un precio de: $ ${this.precio}`;
}

const producto2 = new Producto('Monitor curvo de 27"', 800,'True');
const producto3 = new Producto('Laptot', 300,'False');
const cliente1 = new Cliente('Juan','Llamoja')


console.log(producto2.formatearProducto());
console.log(producto3.formatearProducto());
console.log(cliente1.formatearCliente());


