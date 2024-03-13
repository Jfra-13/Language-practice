let raceNumber = Math.floor(Math.random() * 1000);
let registeredEarly = true;
const age = 17;

if ((age >= 18) && (registeredEarly === true)) {
    console.log(`Se registro temprano y su numero es: ${raceNumber+= 1000}`);
} else if ((age > 18) && (registeredEarly === false)){
    console.log(`#${raceNumber}, no se registro temprano, correra a las 11:00am`)
}

if ((age >= 18) && (registeredEarly === true)) {
    console.log(`Para los que se registraron temprano: #${raceNumber}, correras a las 9:30am.`)
}


if (age < 18) {
    console.log(`Su numero es: #${raceNumber} y correra a las 12:30pm.`)
    
}
console.log(`Mucha suerte corredor #${raceNumber}`)
