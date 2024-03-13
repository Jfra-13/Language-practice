//Pasar por referencia, esto significa que cuando pasamos una variable asiganada a un objeto a
//un objeto a una funcion como argumento, la computadora interpreta el nombre del parametro como
//apuntando al espacio en la memoria que contiene ese objeto

const spaceship = {
    homeplanet : 'Earth',
    color : 'silver'
} 
let paintIt = obj => { //Nuestra  funcion 'paintIt' cambio permanentemente el color de spaceship
    obj.color = 'glorious gold'
};

paintIt(spaceship);

console.log(spaceship.color);

//Como resultado tenemos que las funcines que cambian las propiedades del objeto en realidad mutan el objeto de forma permanente, incluso aunque este asignado a una varible 'const'

let spaceship2 = {
    homePlanet : 'Earth',
    color : 'red'
};
let tryReassignment = obj => {
    obj = {
        identified : false, 
        'transport type' : 'flying'
    }
    console.log(obj) // Prints {'identified': false, 'transport type': 'flying'}

};
  tryReassignment(spaceship2) // El intento de reasignación no funciona.
  spaceship2 // Still returns {homePlanet : 'Earth', color : 'red'};

spaceship2 = {
    identified : false, 
    'transport type': 'flying'
  }; // La reasignación regular sigue funcionando.




let spaceship3 = {
    'Fuel Type' : 'Turbo Fuel',
    homePlanet : 'Earth'
}; 

let greenEnergy = (obj1) => {
    obj1['Fuel Type'] = 'avocado oil';
};

let remotelDisplay = (obj1) => {
    obj1.disabled = true;
}

greenEnergy(spaceship3);
remotelDisplay(spaceship3);

console.log(spaceship3);
//En el codigo anterior se realizo un metodo para agregar elementos nuevos al objeto spaceship3. Tambien se puede eliminar