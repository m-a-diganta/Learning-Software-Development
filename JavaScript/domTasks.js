// DOM Qs1

let body = document.querySelector("body");
console.log(body);

let button1 = document.createElement("button");
button1.innerText = "Click Me";
console.log(button1);

body.prepend(button1);
button1.style.backgroundColor = "red";
button1.style.color = "white";

// DOM Qs2
let paragraph1 = document.querySelector(".paragraph1");
console.log(paragraph1);
// console.log(paragraph1.getAttribute("class"));
// paragraph1.setAttribute("class","newParagraph1");

console.dir(paragraph1.classList);
paragraph1.classList.add("newParagraph1");
console.dir(paragraph1.classList);
// paragraph1.classList.remove("newParagraph1");