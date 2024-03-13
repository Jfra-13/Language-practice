/* 
condicion = true;
while (condicion === true ) {
    console.log('Soy verdadero');
    condicion++;
}; */

/* ♦♦
const palabraCorrecta = (palabra) => {
    while (palabra === 'Jfllamoja'){
        console.log('La contraseña es correcta.');
        palabra++;
    }
};

palabraCorrecta('Jfllamoja'); */

//CICLOS FOR
/* for (let i = 1; i <= 5; i++){
    console.log(`Iteracion ${i}.`);
}
console.log(`Fin del ciclo.`); */

/* const nomes = ['Maria', 'Joao'];
for (var i = 0; i < nomes.length; i++) {
    console.log(nomes[i]);
}; */

//ciclo for en reversa

/* for (let i = 4; i >= 1; i--){
    console.log(`Iteracion ${i}.`);
}
console.log(`Fin del ciclo.`);  */

// Ciclos anidados 
/* for (let i = 1; i <= 4; i++) {
    console.log(`Empieza iteracion ${i}`);
    for (let j = 0; j < 4; j++){
        console.log(j);
    }
};
console.log('Fin del ciclo'); */

//Ciclos While 
/* let x = 1;
while (x <= 4) {
    console.log(`Iteracion ${x}`);
    x++
}
console.log('Fin de while');
 */

//for se usa cuando uno sabe el numero de iteraciones y while cuando no se sabe. Apreder a usar su uso

//Do While
/* let y = 1;

do {
    console.log(`Iteracion ${y}`);
    y++;

} while(y <= 4);
 */

/* const bobsFollowers = ['Kamila','Joaquin','Roony','Lourdes'];
const tinasFollowers = ['Jaime','Roony','Lourdes'];
const mutualFollowers = [];

for (let i = 0; i < bobsFollowers.length; i++) {
    for (let j = 0; j < tinasFollowers.length; j++) {
        if (bobsFollowers[i] === tinasFollowers[j]){
            mutualFollowers.push(bobsFollowers[i]);
        }
    }
}
console.log(mutualFollowers.join(' y ')); */


/* const cards = ['diamond', 'spade', 'heart', 'club'];
let currentCard
while (currentCard !== 'spade'){
    currentCard = cards[Math.floor(Math.random() * 4)];
    console.log(currentCard);
}; */

/* for (let i = 0; i < 99; i++) {
    if (i > 2) {
        break;
    }
    console.log('Banana.');
}; */

/* const rapperArray = ["Lil' Kim", "Jay-Z", "Notorious B.I.G.", "Tupac"];

for (let i = 0; i < rapperArray.length; i++) {
    console.log(rapperArray[i]);
    if (rapperArray[i] === 'Notorious B.I.G.')
    break;
};
console.log("And if you don't know, now you know.");
 */























