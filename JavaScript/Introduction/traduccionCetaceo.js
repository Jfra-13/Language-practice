let input  = 'Perro pica una piedra pero viene Piero y lo pica antes que el perro';
const vowels = ['a','e','i','o','u'];
let resultArray = [];

for (let i = 0 ; i < input.length; i++) {
    /* console.log(i); */
    for(let j = 0 ; j < vowels.length; j++) {
        /* console.log(j); */
        if (input[i] === vowels[j]){
            resultArray.push(input[i]);
        }
    }
    if (input[i] === 'e'){
        resultArray.push(input[i]);
    }
    if (input[i] === 'u'){
        resultArray.push(input[i]);
    }

};
console.log(resultArray.join('').toUpperCase());




