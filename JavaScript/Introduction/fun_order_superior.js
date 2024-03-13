/* const funcionDeAltoOrden = param => {
    param ();
    return `I just invoked ${param.name} as a callback function!`;
};
const otraFuncion = () => {
    return `I\'m being invoked by the higher-order function!`;
};
console.log(funcionDeAltoOrden(otraFuncion)); */

/*const addTwo = num => {
    return num + 2;
}

const checkConsistentOutput = (func, val) => {
    let checkA = val + 2;//Suma y alamcena el digito en checkA dando 6
    let checkB = func(val);// iguala checkB a la funcion addTwo con el valor de la suma 6
    if (checkA === checkB){ //si la respuesta A es igual a la B quiere decir que la funcion addtwo salio igual que la funcion checkConsistentOutput
        return checkB;//devolvemos checkB 
    } else {
        return 'inconsistent results'
    }
}
console.log(checkConsistentOutput(addTwo,4));
 */
const finalParticipants = ['Taylor', 'Donald', 'Don', 'Natasha', 'Bobby'];

// add string after each final participant
const announcements = finalParticipants.map(member => {
    return member + ' joined the contest.';
})

console.log(announcements);