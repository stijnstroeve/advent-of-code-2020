import {readInput, readInputByLine} from '../../../helpers';
const fs = require('fs');

const input = readInputByLine();
let valid = 0;


input.forEach((line) => {

    const password = line.split(' ')[2];
    const charToCheck = line.split(' ')[1].replace(':', '');
    const c1 = parseInt(line.split(' ')[0].split('-')[0]) - 1
    const c2 = parseInt(line.split(' ')[0].split('-')[1]) - 1

    let isValid = false;

    if(password[c1] == charToCheck && password[c2] != charToCheck) {
        isValid = true;
        valid++;
    }
    if(password[c2] == charToCheck && password[c1] != charToCheck) {
        isValid = true;
        valid++;
    }

    // const charCountMap = {};
    //
    // for (const char of password) {
    //     if(!charCountMap[char]) {
    //         charCountMap[char] = 1;
    //     } else {
    //         charCountMap[char] += 1;
    //     }
    // }
    //
    // for(const [char, value] of Object.entries(charCountMap)) {
    //     if(char == charToCheck) {
    //         if(value >= min && value <= max) {
    //             valid++;
    //         }
    //     }
    // }

})




console.log('Valid', valid);