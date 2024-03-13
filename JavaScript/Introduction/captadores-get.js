//Son metodos que obtienen y devulven las propiedades internas de un objeto

const person = {
    _firstName: 'John',
    _lastName: 'Doe',
    get fullName (){
        if (this._firstName && this._lastName){
            return `${this._firstName} ${this._lastName}`;
        } else {
            return 'Missing a first name or a last name.';
        }
    }
}
person.fullName; //John Doe

//La palabra clave 'get' enlaza la propiedad de un objeto con una funcion que sera llamada cuando la propiedad es buscada
//Pueden realizar una accion en los datos al obtener una propiedad
//Los captadores pueden devolver diferentes valores usando condicionales
//Podemos acceder a las propiedades del objeto que llama usando 'this'
//Al usar estos valores hacen mas facil de entender para otros desarrolladores

const robot = {
    _model: '1E78V2',
    _energyLevel: 100,
    get energyLevel () {
        if (typeof this._energyLevel === 'number') {
            return `My current energy level is ${this._energyLevel}`
        } else {
            return `System malfunction: cannot retrieve energy level`
        }
    }
}

console.log(robot.energyLevel);