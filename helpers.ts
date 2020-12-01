import {loadedConfig} from './config';
const fs = require('fs');

export function isDaySelected(): boolean {
    return loadedConfig.config?.day != null && loadedConfig.config?.year != null;
}

/**
 * Gets the current selected day.
 */
export function getCurrentDay(): string {
    return loadedConfig.config.day;
}

/**
 * Gets the current selected year.
 */
export function getCurrentYear(): string {
    return loadedConfig.config.year;
}

export function getYearBasePath(year = getCurrentYear()): string {
    return 'years/' + year;
}

export function getDayBasePath(year = getCurrentYear(), day = getCurrentDay()): string {
    return getYearBasePath(year) + '/' + day;
}

/**
 * Reads the input from the input file.
 */
export function readInput(): string {
    return fs.readFileSync(getDayBasePath() + '/input.txt', 'utf8')
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