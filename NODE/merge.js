var merge = require('lodash.merge');

var arr1 = [{
    "member": "guru",
    "bank": "guru",
    "country": "guru"
},
{
    "member": "charan",
    "bank": "charan",
    "country": "charan"
}];

var arr2 = [{
    "member": "ccccc",
    "name": 'xxxxxx',
    "age": 25
},
{
    "member": "ff",
    "name": 'yyyyyyyyyy',
    "age": 26
}];


var data = merge(arr1, arr2);
console.log(data)
