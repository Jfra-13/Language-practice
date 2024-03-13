//Los bucles son herramientas que repiten un bloque de codigo hasta que se cumpla una condicion.
let spaceship = {
    crew: {
        captain: {
            name: 'Lily',
            degree: 'Computer Engineering',
            cheerTeam() { console.log('You got this!') }
        },
        'chief officer': {
            name: 'Dan',
            degree: 'Aerospace Engineering',
            agree() { console.log('I agree, captain!') }
        },
        medic: {
            name: 'Clementine',
            degree: 'Physics',
            announce() { console.log(`Jets on`) }
        },
        translator: {
            name: 'Shauna',
            degree: 'Conservation Science',
            powerFuel() { console.log('The tank is ful<<l') }
        }
    }
};


for (let crewMember in spaceship.crew) {
    console.log(`${crewMember}: ${spaceship.crew[crewMember].name}`);
}

for (let crewMember in spaceship.crew.name) {
    console.log(`${spaceship.crew[crewMember].name}:${spaceship.crew[crewMember].degree}`)
};

//Los objetos almacenan colecciones de pares clave_valor.
//Cada par clave-valor es una propiedad; cuando una propiedad es una funcion, se conoce como metodo
//Un objeto literal se compone de pares clave-valor separados por comas rodeados por llaves
//Puede acceder, agregar o editar una propiedad dentro de un objeto mediante la notacion de puntos o la notacion de corchetes
//Podemos agregar metodos a nuestros objetos literales usando la sintaxis de clave-valor con expresiones de funciones anonimas como valores o usando la nueva sintaxis de metodos ES6
//Podemos navegar por objetos aninados complejos encadenando operadores 
//Los objetos son mutables: pordemos cambiar sus propiedades incluso cuando se declaran con 'const'
//Los objetos se pasan por referencia: cuando hacemos cambios en un objeto que se pasa a una funcion, esos cambios son permanentes 
//Podemos iterar a traves de objetos usando la 'for in' sintaxis