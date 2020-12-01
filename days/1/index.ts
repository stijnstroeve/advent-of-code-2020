import {readInput} from '../../helpers';
const fs = require('fs');

const input = readInput().split('\n');

console.log('Starting...');

// Part 1
for (let x = 0; x < input.length; x++) {
    let n1 = parseInt(input[x]);

    for (let y = 0; y < input.length; y++) {
        let n2 = parseInt(input[y]);

        const sum = n1 + n2;

        // console.log(sum);

        if(sum == 2020) {
            console.log('Part 1:', n1, n2, n1 * n2);
        }
    }
}

// Part 2
for (let x = 0; x < input.length; x++) {
    let n1 = parseInt(input[x]);

    for (let y = 0; y < input.length; y++) {
        let n2 = parseInt(input[y]);

        for (let z = 0; z < input.length; z++) {
            let n3 = parseInt(input[z]);

            const sum = n1 + n2 + n3;

            if(sum == 2020) {
                console.log('Part 3:', n1, n2, n3, n1 * n2 * n3);
            }
        }

    }
}