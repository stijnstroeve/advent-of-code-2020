#!/usr/bin/env ts-node

const commander = require('commander');
const program = new commander.Command();
const fs = require('fs');
const { spawn } = require('child_process');

const loadTemplate = (template: string) => {
    return fs.readFileSync(`templates/${template}.ts`, 'utf8')
}

program
    .command('generate <day> [template]')
    .description('generates the template for a new day')
    .action((day: string, template: string) => {
        template = template || 'default';

        const loadedTemplate = loadTemplate(template);

        fs.mkdirSync('days/' + day);
        fs.writeFileSync('days/' + day + '/index.ts', loadedTemplate, 'utf8')
        fs.writeFileSync('days/' + day + '/input.txt', '', 'utf8')

        console.log('Generated template for day ' + day);
    });

program
    .command('run <day>')
    .description('runs a days program')
    .action((day: string) => {
        process.env.CURRENT_DAY = day;

        const cmd = 'ts-node days/' + day + '/index.ts';
        const writeStream = fs.createWriteStream('days/' + day + '/output.txt')

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