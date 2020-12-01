const fs = require('fs');

/**
 * Gets the current running day out of the env variables.
 */
export function getCurrentDay(): string {
    return process.env.CURRENT_DAY;
}

/**
 * Reads the input from the input file.
 */
export function readInput(): string {
    return fs.readFileSync('days/' + getCurrentDay() + '/input.txt', 'utf8')
}

/**
 * Reads the input and splits them by line.
 */
export function readInputByLine(): string[] {
    return readInput().split('\n')
}

/**
 * Reads the input and splits them by line.
 * Also makes sure every line is a number
 */
export function readInputByLineParseNumber(): number[] {
    return readInput().split('\n').map(x => parseInt(x))
}