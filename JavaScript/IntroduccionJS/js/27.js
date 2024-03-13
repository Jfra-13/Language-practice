class Producto {
    constructor(nombre, precio) {
        this.nombre = nombre
        this.precio = precio
    }

    formatearProducto() {
        return `El producto ${this.nombre} tiene un precio de: $${this.precio}`
    }
}

class Libro extends Producto {
    constructor(nombre,precio,isbn) {
        super(nombre,precio);
        this.isbn = isbn;
    }

    formatearProducto() {
        return `${super.formatearProducto()} y su ISBN es ${this.isbn}.`
    }
}

class Soda extends Producto {
    constructor(nombre,precio,cantidad) {
        super(nombre,precio);
        this.cantidad = cantidad;
    }

    formatearProducto () {
        return `${super.formatearProducto()} y usted llevara ${this.cantidad}.`
    }
}

class Rosas extends Producto {
    constructor(nombre,precio,color) {
        super(nombre,precio);
        this.color = color;
    }

    formatearProducto () {
        return `${super.formatearProducto()} de color ${this.color}.`
    }
}

const libro = new Libro('JavaScript la Revolucion', 120,'213213214341');
const producto = new Producto('Monitor curvo de 27"',800);
const soda = new Soda('Coca Cola',1.5, '4');
const rosa = new Rosas('Tupipanes',20, 'Blanco y azul')

console.log(producto.formatearProducto());
console.log(libro.formatearProducto());
console.log(soda.formatearProducto());
console.log(rosa.formatearProducto());








