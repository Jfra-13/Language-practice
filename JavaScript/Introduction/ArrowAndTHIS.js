//La palabra reservada 'this' se refiere al objeto de llamada de un metodo y se puede usar para acceder a las propiedades de ese mismo objeto.
const goat = {
    dietType: 'herbivore',
    makeSound() {
        console.log('baaa');
    },
    diet(){
        console.log(this.dietType);
    }
};

goat.diet();

/* diet(){
    console.log(this.dietType)
};

giveDetails: function() {
    console.log(`${this.giveDetails}`)
}; */

//ejemplos alternos 