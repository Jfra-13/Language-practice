//Clases
class Producto {
    constructor(nombre, precio) {
        this.nombre = nombre
        this.precio = precio
    }

    formatearProducto() {
        return `El producto ${this.nombre} tiene un precio de: $${this.precio}`
    }
}

const producto = new Producto('Monitor curvo de 27"',800);
const producto2 = new Producto('Laptop 24"',1000);

console.log(producto.formatearProducto());
console.log(producto2.formatearProducto());

class Precio {
    constructor(precio,descuento){
        this.precio = precio;
        this.descuento = descuento;
    }
    formatearPrecio (){
        return `Por compras mayores de $${this.precio} tienes un descuento de: $${this.descuento}`
    }
}

const disponible = new Precio(1450,200);


console.log(disponible.formatearPrecio())