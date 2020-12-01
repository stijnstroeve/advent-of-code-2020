import {readInputByLineParseNumber} from '../../../helpers';

const input = readInputByLineParseNumber();

function calculatePart1(): number {
    let sum = 0;
    input.forEach((x) => {
        sum += x;
    })

    return sum;
}

function calculatePart2(): number {
    let done = [];
    let freq = 0;
    let isDone = false;

    while(isDone == false) {
        for (let i = 0; i < input.length; i++) {
            let x = input[i];

            freq += x;

            if(done.includes(freq)) {
                isDone = true;
                break;
            }

            done.push(freq);
        }
    }

    return freq;
}

console.log('Part 1: ', calculatePart1());
console.log('Part 2: ', calculatePart2());