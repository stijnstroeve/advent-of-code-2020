#!/usr/bin/env ts-node

import {getDayBasePath, getYearBasePath, isDaySelected} from './helpers';
import {loadedConfig} from './config';

const commander = require('commander');
const program = new commander.Command();
const fs = require('fs');
const {spawn} = require('child_process');

const loadTemplate = (template: string) => {
    return fs.readFileSync(`templates/${template}.ts`, 'utf8')
}

program
    .command('generate <year> <day> [template]')
    .description('generates the template for a new day and year')
    .action((year: string, day: string, template: string) => {
        template = template || 'default';

        const loadedTemplate = loadTemplate(template);

        const yearBasePath = getYearBasePath(year);
        const dayBasePath = getDayBasePath(year, day);
        if(!fs.existsSync(yearBasePath)) {
            fs.mkdirSync(yearBasePath);
        }

        fs.mkdirSync(dayBasePath);
        fs.writeFileSync(dayBasePath + '/index.ts', loadedTemplate, 'utf8')
        fs.writeFileSync(dayBasePath + '/input.txt', '', 'utf8')

        console.log(`Generated template for day ${day} and year ${year}.`);
    });

program
    .command('select <year> <day>')
    .description('selects a program to run')
    .action((year: string, day: string) => {
        loadedConfig.config.year = year;
        loadedConfig.config.day = day;

        loadedConfig.save();

        console.log(`Selected day ${day} for year ${year}.`);
    });

program
    .command('run')
    .description('runs the currently selected program')
    .action(() => {

        if(!isDaySelected()) {
            console.log('No day selected.');
            return;
        }

        const dayBasePath = getDayBasePath();

        const cmd = `ts-node ${dayBasePath}/index.ts`;

        const writeStream = fs.createWriteStream(`${dayBasePath}/output.txt`)

        const child = spawn(cmd, [], { shell: true });

        child.stdout.on( 'data', data => {
            console.log( `${data}` );
        } );

        child.on( 'close', code => {
            console.log( `child process exited with code ${code}` );
        } );

        child.stdout.pipe(writeStream);
        child.stderr.pipe(writeStream);
    });


program.parse(process.argv);