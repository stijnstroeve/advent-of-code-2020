import {readInputByLine} from '../../../helpers';

const input = readInputByLine();

function calculatePart1(): number {
    let valid = 0;

    input.forEach((line) => {

        const password = line.split(' ')[2];
        const charToCheck = line.split(' ')[1].replace(':', '');
        const min = parseInt(line.split(' ')[0].split('-')[0])
        const max = parseInt(line.split(' ')[0].split('-')[1])

        const charCountMap = {};

        for (const char of password) {
            if(!charCountMap[char]) {
                charCountMap[char] = 1;
            } else {
                charCountMap[char] += 1;
            }
        }

        for(const [char, value] of Object.entries(charCountMap)) {
            if(char == charToCheck) {
                if(value >= min && value <= max) {
                    valid++;
                }
            }
        }

    })

    return valid;
}

function calculatePart2(): number {
    let valid = 0;

    input.forEach((line) => {

        const password = line.split(' ')[2];
        const charToCheck = line.split(' ')[1].replace(':', '');
        const c1 = parseInt(line.split(' ')[0].split('-')[0]) - 1
        const c2 = parseInt(line.split(' ')[0].split('-')[1]) - 1

        if(password[c1] == charToCheck && password[c2] != charToCheck) {
            valid++;
        }
        if(password[c2] == charToCheck && password[c1] != charToCheck) {
            valid++;
        }

    })

    return valid;
}




console.log('Part 1:', calculatePart1());
console.log('Part 2:', calculatePart2());
