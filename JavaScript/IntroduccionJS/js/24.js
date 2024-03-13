//This
const reservacion = {
    nombre: 'Juan',
    apellido: 'Llamoja',
    total : 5000,
    pagado : false ,
    informacion: function(){
        console.log(`El cliente ${this.nombre} ${this.apellido} resrvo y su cantidad pagar es de: ${this.total}`)
    }
}

const reservacion2 = {
    nombre: 'Pedro',
    apellido: 'Gonzales',
    total : 5000,
    pagado : false, 
    informacion: function(){
        console.log(`El cliente ${this.nombre} ${this.apellido} resrvo y su cantidad pagar es de: ${this.total}`)
    }
}

reservacion.informacion();
reservacion2.informacion();

