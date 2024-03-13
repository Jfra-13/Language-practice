const producto = {
    nombreProducto : "Monitor 20 pulgadas",
    precio : 300,
    disponible : true    
}

Object.freeze(producto);

producto.imagen = 'imagen.jpg';

delete producto.precio

console.log(producto);