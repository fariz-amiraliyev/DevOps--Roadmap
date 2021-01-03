const Cli = require('cli');

const cliArgs = Cli.parse({
    region: ['r', 'AWS region name', 'string', 'ap-south-1'],
    functionName: ['f', 'Function name', 'string'],
    input: ['i', 'Input to function', 'string']
})

if(!cliArgs.input) {
    Cli.getUsage();
}


process.env.AWS_REGION = cliArgs.region;

let event = JSON.parse(cliArgs.input);

require(`./${cliArgs.functionName}/index`).handler(event).then(console.log).catch(console.error);