const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = [line];
}).on('close',function(){
    str = input[0];
    res = ''
    for (letter of str) {
        if (letter.toUpperCase() == letter) {
            res += letter.toLowerCase()
        } else {
            res += letter.toUpperCase() 
        }
    }
    
    console.log(res)
});