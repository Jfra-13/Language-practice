let secretMessage = ['Learning', 'is', 'not', 'about', 'what', 'you', 'get', 'easily', 'the', 'first', 'time,', 'it', 'is', 'about', 'what', 'you', 'can', 'figure', 'out.', '-2015,', 'Chris', 'Pine,', 'Learn', 'JavaScript'];
const eliminar = secretMessage.pop();
const agregar = secretMessage.push('to','Program');
const elimarPrimer = secretMessage.shift();
const agregarPrimer = secretMessage.unshift('Programing');

const ubicar = 6;
secretMessage[ubicar] = 'right';

const removerArrays = secretMessage.splice(6, 10, 'know');

console.log(secretMessage.join(' '));