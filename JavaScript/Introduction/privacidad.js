//Acceder a las propiedades es fundamental sin embargo hay casos en los que no queremos que otro codigo simplemente acceday actualice las propiedades de un objeto.
//
const catB = {
    _name: 'Snickers',
    get name(){
        return this._name
    },
    set name(newName) {
        (typeof newName === 'string' && newName.length > 0) ? this._name = newName : console.log('Error')
    }
}
console.log(catB);