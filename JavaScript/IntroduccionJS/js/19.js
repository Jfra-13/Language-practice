//Arrow Functions
const sumar2 = (n1,n2) => console.log(n1 + n2);
sumar2(5,10);

const aprendiendo = Tecnonologia => console.log(`Aprendiendo ${Tecnonologia}`)
aprendiendo('JavaScript')


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
meses.forEach( mes => {
    if(mes == 'Marzo') {
        console.log('Marzo si existe');
    }
});


//Some ideal para arreglo de objetos
resultado = carrito.some(producto =>  producto.nombre == 'Celular');

 //Reduce 
resultado = carrito.reduce((total, producto) => total + producto.precio,0);


//Filter
resultado = carrito.filter(producto => producto.precio > 400)
console.log(resultado);