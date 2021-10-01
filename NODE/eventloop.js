const fs = require('fs');
const setTimeOutlogger = () => { console.log('setTimeout logger'); }
const setImmediateLogger = () => { console.log('setImmediate logger'); }
//For timeout 
setTimeout(setTimeOutlogger, 1000);
//File I/O operation
fs.readFile('test.txt', 'utf-8', (data) => { console.log('Reading data 1'); });
fs.readFile('test.txt', 'utf-8', (data) => { console.log('Reading data 2'); });
fs.readFile('test.txt', 'utf-8', (data) => { console.log('Reading data 3'); }); fs.readFile('test.txt', 'utf-8', (data) => { console.log('Reading data 4'); }); fs.readFile('test.txt', 'utf-8', (data) => { console.log('Reading data 5'); });
//For setImmediate
setImmediate(setImmediateLogger);
setImmediate(setImmediateLogger);
setImmediate(setImmediateLogger);

process.nextTick(function C() {
    console.log("1st process");
});

process.nextTick(function D() {
    console.log("2nd process");
});
// // setImmediate
// //  loggersetImmediate
//  loggersetImmediate
//   loggerReading data 1Reading data 2Reading data 3Reading data 4Reading data 5setTimeout logger
