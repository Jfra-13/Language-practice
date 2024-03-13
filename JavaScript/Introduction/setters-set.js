// Junto con getter , tambien podemos crear metodos setter que reasignan valores de propiedades existentes dentro de un objeto
const person = {
    _age: 37,
    set age (newAge) {
        if (typeof newAge === 'number'){    
            this._age = newAge;
        } else {
            console.log('You must assing a number to age')
        }
    }
};
// Podemos realizar una comprobacion de que valor se esta asignando a this._age
//Cuando usamos el metodo setter, solo los valores que son numeros se reasignaran this._age
//Hay diferentes salidas dependiendoo de que valores se usan para reasignar this._age

