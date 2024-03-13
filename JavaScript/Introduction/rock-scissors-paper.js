const getUserChoice = (userInput) => {
    userInput = userInput.toLowerCase();
    if ((userInput === 'rock') || (userInput === 'paper') || (userInput === 'scissors') ){
        return userInput;
    } else {{
        console.log('Error');
    }}
};

/* console.log(getUserChoice('')); */

const getcomputerChoice = () =>{
    randomNumber = Math.floor(Math.random()*3);
    switch (randomNumber) {
        case 0:
            return 'rock';
            break;
        case 1:
            return 'paper';
            break;
        case 2:
            return 'scissors';
            break;
    }
    return randomNumber;
};

/* console.log(getcomputerChoice()); */

const determineWinner = (getUserChoice,getcomputerChoice) => {
    if (getUserChoice === getcomputerChoice) {
        return 'Empate';
    }
    if (getUserChoice === 'rock'){
        if (getcomputerChoice === 'paper') {
            return 'La computadora gano';
        } else {
            return 'Usuario gano';
        }
    }
    if (getUserChoice === 'paper') {
        if (getcomputerChoice === 'scissors') {
            return 'La computadora gano';
        } else {
            return 'Usuario gano';
        }
    }
    if (getUserChoice === 'scissors') {
        if (getcomputerChoice === 'rock') {
            return 'La computadora gano';
        } else {
            return 'Usuario gano';
        }
    }
};

const playGame = () => {
    let userChoice = getUserChoice('paper');
    let computerChoice = getcomputerChoice();
    console.log(`Tu tiraste ${userChoice}`);
    console.log(`La maquina tiro ${computerChoice}`);
    console.log(determineWinner(userChoice,computerChoice))
};

playGame();
