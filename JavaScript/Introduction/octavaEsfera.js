let userName = 'Joaquin';
let defaultName;
(userName) ? defaultName = userName : defaultName = '' ;
console.log(`Hello ${defaultName}`);

let  userQuestion = 'tendra un carro nuevo este año.';
console.log(`El usuario ${defaultName} quiere saber si ${userQuestion}`);

let eightBall = ('La octava magica bola contesta que!!...')
let randomNumber = Math.floor(Math.random()*8);
switch (randomNumber) {
    case 0:
    console.log(eightBall + 'I know bro');
    break;
    case 1:
    console.log(eightBall + 'It is certain');
    break;
    case 2:
    console.log(eightBall + 'It is decidedly so');
    break;
    case 3:
    console.log(eightBall + 'Reply hazy try again');
    break;
    case 4:
    console.log(eightBall + 'Cannot predict now');
    break;
    case 5:
    console.log(eightBall + 'Do not count on it');
    break;
    case 6:
    console.log(eightBall + 'My sources say no');
    break;
    case 7:
    console.log(eightBall + 'Outlook not so good');
    break;
    case 8:
    console.log(eightBall + 'Signs point to yes');
    break;
}