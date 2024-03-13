//Los objetos a menudo estan anidados , un objeto puede tener otro objeto 
//como propiedad que a su vez podria tener una propiedad que es una matriz de
//incluso mas objetos

const spaceship = {
    passenger: null,
    telescope: {
        yearBuilt: 2018,
        model: '91031-XLT',
        focalLength: 2032
    },

    crew: {
        captain: {
            name: 'Sandra',
            degree: 'Computer Engineering',
            encourageTeam() { console.log('We got this!')},
            'favorite foods': ['cookies', 'cakes', 'candy', 'spinach'] 
        }
        
    },

    engine: {
        model: 'Nimbus2000'
    },

    nanoelectronics : {
        computer: {
            terabytes: 100,
            monitors: 'HD'
        },
        'back-up': {
            battery: 'Lithium',
            terabytes: 50
        }
    }
};
//Podemos encadenar operadores para acceder a propiedades anidadas,
//debes estar atento a que operador tiene sentido usar en cada capa.
//NOTA -> Puede ser util fingir que eres la computadora y evaluar 
//cada expresion de izquierda a derecha 

console.log(spaceship.nanoelectronics['back-up'].battery);

let capFave = spaceship.crew.captain['favorite foods'];
console.log(capFave);

spaceship.passenger = [{1: 'Jaime'},{2: 'Tom'}]; //Creacion de objeto dentro de un objeto

let firstPassenger = spaceship.passenger[0] // seleccion del primer objeto creado en spaceship 

console.log(firstPassenger);

