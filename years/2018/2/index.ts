import {readInputByLine} from '../../../helpers';

const input = readInputByLine().map(line => line.replace('\r', ''));

function calculatePart1(): number {

    let twoTimes = 0;
    let threeTimes = 0;

    input.forEach(x => {

        const chars = {};

        for (const char of x) {
            if(!chars[char]) {
                chars[char] = 1;
            } else {
                chars[char] += 1;
            }
        }

        let hasTwo = false;
        let hasThree = false;

        for (const [char, times] of Object.entries(chars)) {
            if(times == 2) {
                hasTwo = true;
            }

            if(times == 3) {
                hasThree = true;
            }
        }

        if(hasTwo) twoTimes++;
        if(hasThree) threeTimes++;

    })

    return twoTimes * threeTimes;
}

function calculatePart2(): string | null {
    let answer = null;

    input.forEach((x) => {
        input.forEach((y) => {
            let diff = 0;

            for (let i = 0; i < x.length; i++) {

                if (x[i] != y[i]) {
                    diff++;
                }
            }

            if (diff == 1) {

                let answerArr = [];

                for (let i = 0; i < x.length; i++) {

                    if (x[i] == y[i]) {
                        answerArr.push(x[i]);
                    }
                }

                answer = answerArr.join('');
            }
        })
    })

    return answer;
}

console.log('Part 1:', calculatePart1());
console.log('Part 2:', calculatePart2());
