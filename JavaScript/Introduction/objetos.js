//Estructura de un objeto en js
let spaceship = {
    'Fuel Type' : 'diesel',
    color : 'silver'
};

// 'spaceship' es el nombre del objeto
// Dentro de 'spaceship' estan sus propiedades del objeto
// 'Fuel Type' y color son las llaves
// 'diesel' y 'silver' son los valores

let fasterShip = {
    'Fuel Type' : 'Turbo Fuel',
    color : 'silver'
};

//Acceder a las propiedades de un objeto
let spaceship1 = {
    homePlanet: 'Earth',
    color: 'silver',
    'Fuel Type': 'Turbo Fuel',
    numCrew: 5,
    flightPath: ['Venus', 'Mars', 'Saturn']
};

spaceship1.color; //Seleccionar
console.log(spaceship1.homePlanet); //Mostrar en consola
//Si intentamos acceder a una propiedad que no existe devolvera 'indefinido'

const crewCount = spaceship1.numCrew;
const planetArray = spaceship1.flightPath;
console.log(`My spaceship has ${crewCount} passengers and we are touring the planets ${planetArray.join(' ')} `);

//Notacion en corchetes ... manera de acceder a una propiedad de un objeto mediante []

let spaceship2 = {
    'Fuel Type' : 'Turbo Fuel',
    'Active Mission' : true,
    homePlanet : 'Earth', 
    numCrew: 5
};
let propName =  'Active Mission';

let isActive = spaceship2['Active Mission'];
/* console.log(isActive); */
console.log(spaceship2[propName]);

//Asignacion de propiedad 
// Los  objetos son mutables, lo que significa que podemos actualizarlos despues de crearlos

let spaceship3 = {
    'Fuel Type' : 'Turbo Fuel',
    homePlanet : 'Earth',
    color: 'silver',
    'Secret Mission' : 'Discover life outside of Earth.'
};

spaceship3['Fuel Type'] = 'vegetable oil';
spaceship3.color = 'gold';
//Si la propiedad ya existe en el objeto, cualquier valor que tuviera antes se reemplazara con el declarado
//Si no habia ninguna propiedad con ese nombre, se agregara una nueva propiedad al objeto
//IMPORTANTE -> No se puede reasignar un objeto declarado con 'const'
//Se puede elminar una propiedad con la plabra delete -> delete space.mission;

spaceship3.color = 'glorious gold';
spaceship3.numEngines = 3;
delete spaceship3['Secret Mission'];
console.log(spaceship3);

//METODOS 
//Cuando los datos almacenados dentro de un objeto son una funcion, lo llamamos metodo
//Una propiedad es lo que tiene un objeto, mientras que un metodo es lo que hace un objeto

const alienShip = {
    invade: function () {
        console.log('Hello, we have come to dominate your planet');//Agregamos una funcion dentro del objeto, convirtiendolo en un metodo para que haga algo el objeto
    }
}
alienShip.invade();

const alienShip1 = {
    invade1 () {
        console.log('Hello, we have come to dominate your planet');//manera simplificada de crear un metodo dentro de un objeto
    }
}


