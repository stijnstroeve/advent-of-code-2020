const fs = require('fs');

export const getCurrentDay = () => {
    return process.env.CURRENT_DAY;
}

export const readInput = () => {
    return fs.readFileSync('days/' + getCurrentDay() + '/input.txt', 'utf8')
}