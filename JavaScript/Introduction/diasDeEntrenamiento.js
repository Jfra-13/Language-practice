// The scope of `random` is too loose 
const random = Math.floor(Math.random() * 3);
const name = 'Nala';

const getRandEvent = () => {
    if (random === 0) {
        return 'Marathon';
    } else if (random === 1) {
        return 'Triathlon';
    } else if (random === 2) {
        return 'Pentathlon';
    }
};

/* console.log(getRandEvent()); */

const getTrainingDays = (event) => {
    let days;
    if (event === 'Marathon') {
        days = 50;
    } else if (event === 'Triathlon') {
        days = 100;
    } else if (event === 'Pentathlon') {
        days = 200;
    }
    return days;
    
};

/* console.log(getTrainingDays()); */

const logEvent = (name, event) => {
    console.log(`${name}'s event is: ${event}`);
};
const logTime = (name, days) => {
    console.log(`${name}'s time to train is: ${days} days`);
};

const event = getRandEvent();
const days = getTrainingDays(event);


logEvent(name, event);
logTime(name,days);
