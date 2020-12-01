import {readInputByLineParseNumber} from '../../helpers';

const target = 2020;
const input = readInputByLineParseNumber();

function calculatePart1(): number | null {
    for (let x = 0; x < input.length; x++) {
        let n1 = input[x];

        for (let y = 0; y < input.length; y++) {
            let n2 = input[y];

            const sum = n1 + n2;

            if(sum == target) {
                return n1 * n2;
            }
        }
    }
    return null;
}

function calculatePart2(): number | null {
    for (let x = 0; x < input.length; x++) {
        let n1 = input[x];

        for (let y = 0; y < input.length; y++) {
            let n2 = input[y];

            for (let z = 0; z < input.length; z++) {
                let n3 = input[z];

                const sum = n1 + n2 + n3;

                if(sum == 2020) {
                    return n1 * n2 * n3;
                }
            }

        }
    }
    return null;
}

console.log('Calculating answers...');

const p1 = calculatePart1();
console.log('Answer part 1:', p1);

const p2 = calculatePart2();
console.log('Answer part 2:', p2);