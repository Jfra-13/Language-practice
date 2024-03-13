const getSleepHours = (day) => {
    day = day.toLowerCase();
    switch (day) {
        case 'monday' :
            return 8 ;
            break;
        case 'tuesday' :
            return 8 ;
            break;
        case 'wednesday' :
            return 8 ;
            break;
        case 'thursday' :
            return 8 ;
            break;
        case 'friday' :
            return 8 ;
            break;
        case 'saturday' :
            return 8 ;
            break;
        case 'sunday' :
            return 10 ;
            break;
        default:
            return 'Dia de la semana incorrecto.'
    }
}

/* console.log(getSleepHours('Sunday')); */

const getActualSleepHours = () => {
    return getSleepHours('monday') + 
    getSleepHours('tuesday') + 
    getSleepHours('wednesday') + 
    getSleepHours('thursday') + 
    getSleepHours('friday') + 
    getSleepHours('saturday') + 
    getSleepHours('sunday') 
};

/* console.log(getActualSleepHours()); */

const getIdealSleepHours = () => {
    let idealHours = 8 * 7;
    return idealHours;
};

/* console.log(getIdealSleepHours()); */

const calculateSleepDebt = () => {
    const actualSleepHours = getActualSleepHours();
    const idealSleepHours = getIdealSleepHours();
    if (actualSleepHours === idealSleepHours) {
        console.log(`Durmio ${idealSleepHours} horas, la cantidad perfecta.`)
    } else if (actualSleepHours > idealSleepHours){
        console.log(`Durmio ${actualSleepHours - idealSleepHours} horas mas, puede levantarse.`)
    } else if (actualSleepHours < idealSleepHours){
        console.log(`Durmio ${idealSleepHours - actualSleepHours} horas menos de lo normal, debe dormir mas.`)
    }
};

calculateSleepDebt();
