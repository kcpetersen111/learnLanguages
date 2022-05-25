console.log("Hello World");

// can make a variable and assign it a value
const name = "John";
let age = 30;

// const is a constant and let is a variable can use var but should be avoided

// can do all standard math operations

let ageInWeeks = age * 52;

// javascript has numbers, strings, booleans, null, undefined, and objects

let person = { name: "John", age: 30 };

//can have functions
function personSays(person, message) {
    console.log(person.name + " says " + message);
}

personSays(person, "Hello");

// can use recursion to solve problems
function fibNum(num){
    if(num <= 1){
        return num;
    }
    return fibNum(num - 1) + fibNum(num - 2);
}

console.log(fibNum(10));

// can add event listeners to html elements
// document.getElementById("button").addEventListener("click", function(){
//     console.log("button clicked");
// });

//can use maps
let map = new Map();
map.set("name", "John");
map.set("age", 30);
console.log(map);

// can use arrays
let names = ["John", "Jane", "Mary"];
console.log(names[0]);
names[0] = "Bob";
console.log(names[0]);

// get the length of an array
console.log(names.length);

//can also pop and push to arrays
names.push("Bob");
console.log(names);
names.pop();
console.log(names);

//can shift and unshift to arrays to use the first element

names.shift();
console.log(names);
names.unshift("Bob");
console.log(names);


//can delete or set specific elements in an array but this will leave a hole of undefined values in your array

delete names[1];
console.log(names);
names[1] = "Jane";
console.log(names);

names[4] = "Bob";
console.log(names);
delete names[4];
console.log(names);

//above will leave undefined values in the array

// there are all the normal comparison operators
// there is also equal type and value ===
// there is also not equal type or value !==

//can use if else statements

if (age > 30) {
    console.log("You are old");
} else if (age < 30) {
    console.log("You are young");
} else {
    console.log("You are aged");
}


//switch statements

switch(names[1]){
    case "John":
        console.log("John");
        break;
    case "Jane":
        console.log("Jane");
        break;
    case "Mary":
        console.log("Mary");
        break;
    default:
        console.log("Unknown");
}
names.pop();
names.pop();
//have c style loops
for(let i = 0; i < names.length; i++){
    console.log(names[i], " ", i);
}

//ranging loops

for (let name in names){
    console.log(names[name]);
}

//while loops

while(names.length > 0){
    names.pop();
    console.log(names);
}

// can also do a do while loop

//can use break and continue to break out of loops
let i = 0;
while(true){
    if (i > 10){
        break;
    } else{
        i++;
    }
}

//sets are just arrays that do not have duplicates

const letters = new Set();
letters.add("a");
letters.add("b");
letters.add("c");
letters.add("a");
letters.add("b");
letters.add("c");
console.log(letters);