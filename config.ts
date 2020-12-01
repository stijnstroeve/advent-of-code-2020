const fs = require('fs');

const configFile = '.rc.json';

interface IConfiguration {
    year: string;
    day: string;
}

export class Configuration {

    load(): IConfiguration {
        if(this._config) return;

        if(!fs.existsSync(configFile)) {
            fs.writeFileSync(configFile, JSON.stringify({}), 'utf8');
        }

        const readConfig = fs.readFileSync(configFile);
        this._config = JSON.parse(readConfig);

        return this._config;
    }

    private _config: IConfiguration;

    get config(): IConfiguration {
        return this._config;
    }

    set config(config: IConfiguration) {
        this._config = config;
    }

    save(): void {
        if(!this._config) return;

        fs.writeFileSync(configFile, JSON.stringify(this._config), 'utf8');
    }

}

export const loadedConfig = new Configuration();
loadedConfig.load();