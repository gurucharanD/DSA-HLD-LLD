<!-- call apply bind -->
function saySomething(message,age){
  console.log(this.name + " is " + message+age)
}        
var person4 = {name:  "John"};
saySomething.apply(person4, ["awesome",209]);
saySomething.call(person4, "awesome",209);

function multiply(a,b){
  return a*b;
}
<!--  -->

<!-- function currying -->
function currying(fn){
  return function(a){
    return function(b){
      return fn(a,b);
    }
  }
}

var curriedMultiply = currying(multiply);

console.log(multiply(4, 3)); // Returns 12

console.log(curriedMultiply(4)(3)); // Also returns 12
<!--  -->

<!-- generator functions:  -->

special kind of functions whose execution can be paused
func* gen(){
    yield 3;
    yield 4;
}
the call to next() return an iterator which has a value and done properties

gen().next() 
returns  {value:3,done:false}

gen().next()
returns  {value:4,done:true}

<!--  -->

<!-- Destructuring -->
Destructuring is used to extract out values from collections such as 
arrays and objects

object destructuring:
const classDetails = {
  strength: 78,
  benches: 39,
  blackBoard:1
}
const {strength:classStrength, benches:classBenches,blackBoard:classBlackBoard} = classDetails;

array destructuring:
const arr = [1, 2, 3, 4];
const [first,second,third,fourth] = arr;
<!--  -->

let and const are hoisted but are placed
in a temporal deadzone until they are assigned a value
during which they cannot be accessed

function fruit(){
  console.log(name)
  console.log(color)
  var name = 'apple'
  let color = 'red'
}

fruit()

<!-- Async Vs Defer -->
  these are boolean attributes that are used in the script tag

  when browser comes across a script tag, then it stops parsing the HTML
downloads the script and executes it then goes back to parsing the HTML again

  Async: when async is used, the browser will asyncronously download the script
while rendering the HTML in parallel. Once the script is downloaded it will execute it
and then goes back to parsing the HTML

  Defer: when Defer is used, the browser will async download the script will parsing the HTML
but it will only execute the script once the parsing of HTML is finished

async attribute doesnt guarantee the order of scripts but differ does

<!--  -->

<!--  Slice vs Splice -->
slice() can be used to create a copy of an array or return a portion of an array. 
It is important to note that the slice() method does not alter the original array but instead creates a shallow copy.

splice() will change the contents of the original array.
it is used to add or remove elements of an existing array and the return value will be the removed items from the array.

const cities = ["Tokyo","Cairo","Los Angeles","Paris","Seattle"];

const newCityArr = cities.slice(2);

console.log(newCityArr)
// ["Los Angeles", "Paris", "Seattle"]

console.log(cities)
// ["Tokyo", "Cairo", "Los Angeles", "Paris", "Seattle"]

cities.splice(2,1)
console.log(cities)
// ["Tokyo", "Cairo", "Paris", "Seattle"]

cities.splice(2,1,'hyderabad')
console.log(cities)
// ["Tokyo", "Cairo", "hyderabad", "Seattle"]

<!--  -->

