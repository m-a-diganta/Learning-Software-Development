// Window Oboject - by default global object by browser
// console / alert / prompt are pasrts of window object
// Window => Document (object) => holds all html codes
// JS used for dynamic manipulation that HTML,CSS cant do
// firstChild, lastChild, cheldren of node & nodes => text,comment,element

console.log(window.document);  
console.dir(window.document);  // to print object properties

console.log(document.body);  
console.dir(document.body);

console.dir(document.body.childNodes[1]);

// DOM Maninpulation

// Selecting with id
let firstDiv = document.getElementById("test");
console.log(firstDiv);

// Selecting with class
let parClass = document.getElementsByClassName("par");
console.dir(parClass);
console.log(parClass);

// Selecting with Tags
let buttonTag = document.getElementsByTagName("button");
console.dir(buttonTag);
console.log(buttonTag);

// Selecting with QuerySelector
let firstElementP = document.querySelector("p");
console.dir(firstElementP);
console.log(firstElementP);

let circle = document.querySelector("#circle");
console.dir(circle);
console.log(circle);

let elementsP = document.querySelectorAll("p");
console.dir(elementsP);
console.log(elementsP);

console.log(circle.tagName); // returns the tag name
console.log(document.body.children); 
console.log(firstDiv.innerText);  // get 
console.log(firstDiv.innerHTML); 

firstDiv.innerText = "abcd"; // set - works similar for innerHTML
console.log(firstDiv.innerText); 


// Task1
let heading2 = document.getElementsByTagName("h2");
console.log(heading2[1]);
heading2[2].innerText += " - This is Task 2";


// Accessing Attributes
let attCircle =  circle.getAttribute("align");
console.log(attCircle);

circle.setAttribute("align","left");
console.log(attCircle);
console.log(circle.getAttribute("align"));

console.log(circle.style); // shows only inline style not from css file
circle.style.backgroundColor = "green";
// circle.style.visibility = "hidden";


// Insert Elements with JS
let newButton = document.createElement("button"); // create
newButton.innerText = "Click the Button!";
console.log(newButton);

let buttons =  document.querySelector(".buttons");
buttons.append(newButton); // adds at the end of the node
buttons.prepend(newButton);  // adds at the start of the node
buttons.before(newButton); // adds before the node
buttons.after(newButton); // adds after the node
// buttons.remove(); //removes the node
// newButton.remove(); //removes the element
// appendChild / removeChild



