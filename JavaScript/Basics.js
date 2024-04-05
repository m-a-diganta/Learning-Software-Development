/* Dynamically Typed 
MDN docs - to learn
Data Types - Primitive and Non-primitives*/

// Print in JS
console.log("Learning JavaScript");


// Variables in JS

/* var, const can be used instead of var
unlike var, let does not allow to redeclare a variable
value of const is fixed [pi, g, e ....]
var => global scope, let/const => block scope */

let name1="Arabi Hossain Ahil"; 
let age1= 15;
console.log(name1,age1);
console.log(typeof age1);;

console.log(name1 + age1); // string concates the following number

let job1= null; 
console.log(job1);
console.log(typeof job1);  // object type

let job2= undefined;  // null and undefined are different
console.log(job2);
let job3 ; // cant be done for const
console.log(job3);

let isStudent= true;  // Variable naming => Camel case
console.log(isStudent);
console.log(isStudent + 1);

let x= BigInt("123");
let y= Symbol("Hello");
console.log(x);
console.log(y);


// Non-primitive variable => Object(a collection of variables)
const student1={
    name1: "Shafin",
    age1: 20,
    class1: 9
}  // wroks like dictionary (key value pair)
console.log(student1); 
console.log(name1);
console.log(student1["name1"])
console.log(student1.age1)

student1["age1"]= student1["age1"] + 1  // cant change the value of a const variable, but can change the value of the keys of an object
console.log(student1["age1"])


// Use of operators in JS

let a = 5;
let b = 2;

console.log("a / b = ", a/b);
console.log("a % b = ", a%b);
console.log("a ** b = ", a**b);

// Unary operators => incr, decr
console.log("a = ", a++); // First assign then incr (Post incr)
console.log("a = ", a);
console.log("a = ", ++a); // First incr then assign (Pre incr)
console.log("a = ", a);

// Assignment operators
b += 2;
console.log("b = ", b);

// Comparison Operators
console.log(a != b);
console.log(a !== b); // compares value and type both
c = "4";
console.log(b == c );
console.log(b === c);

// Logical Operators ( &&, ||, !)
console.log( a>=b && b>3);
console.log( !(6<5));




// Conditional Statements - if Statement

let age = 21;
if(age >= 18){
    console.log("You can vote");
}

// if-else / else if Statement
let mode = "light";
let color;
if (mode === "dark"){
    color = "black";
}
else if (mode === "light"){
    color = "Grey";
}
else{
    color = "white";
}
console.log(color);

if (mode === "light") console.log("Blue"); // shortcut

// ternary operator
let ageCond = age >= 18 ? "Adult" : "Not adult";
console.log(ageCond);
age >= 25 ? console.log("Young") : console.log("Not young");




// Switch

const expr = 'Oranges';
switch (expr) {
  case 'Oranges':
    console.log('Oranges are $0.59 a pound.');
    break;
  case 'Papayas':
    console.log('Papayas are $2.79 a pound.');
    break;
  default:
    console.log(`Sorry, we are out of ${expr}.`); // Print variables using formatting
}



// Input-Output, Prompt, Alert

alert("Let's Start")
// let userName= prompt("Enter your name: ");
// console.log(`Your name is ${userName}.`);



// Loops - for loop

for (let i=1; i<=5; i++){
    console.log(`For Loop running ${i}`)
}
// console.log(i);

// while loop
let i = 1;
while (i <=5){
    console.log("while loop running");
    i++;
}
console.log(i);
// Do while loop runs at least once



// for-of loop (strings and arrays)
let str1 = "iterate";
for(let i of str1){
    console.log(i);
}

// for-in loop (Objects)
let car1={
    color: "Black",
    brand: "Audi",
    wheels: 4,
}
for(let i in car1){  // i = key
    console.log(`Key = ${i}, Value = ${car1[i]} `);
}




// String 

let str2= "here is a string";
console.log(str2.length);
console.log(str2[2]);

let str3= `Again ${str2}`; // Template literal - String interpolation
console.log(str3);
// escape characters => \n, \t [length of '\n' is always 1]

str4 = "  Example";
str5 = " Second ";
str4[5] = "y"; // Doesnt work as strings are immutable [rather use .replace]
console.log(str4.toUpperCase());
console.log(str4.toLowerCase());
console.log(str4.trim()) ; // removes whitespace from start and end
console.log(str4.slice(2,5));
console.log(str5.concat(str4));
console.log(str4.replace("xam","y"));
console.log(str4.charAt(3));




// Array - Mutable

let marks = [30,40,21,43,50,65];
for(let i=0; i< marks.length; i++){
    console.log(marks[i]);
}

let foodItems = ["Burger", "Piza", "Apple"];
foodItems.push("Chips", "Tomato");
console.log(foodItems);

let poppedItem = foodItems.pop();
console.log(foodItems);
console.log(poppedItem);

console.log(foodItems.toString());
foodItems.unshift("Veg");
console.log(foodItems);
foodItems.shift();
console.log(foodItems);

console.log(marks.slice(1,3)); //doesnt change the original array
// splice(start, delCount, new elements)
marks.splice(2, 2, 80,90);
console.log(marks);