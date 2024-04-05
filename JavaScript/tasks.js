// Task 1

let productName = "Parkewr Jotter Standard CT Ball Pen(Black)";
let rating = 7002;
let isDeal = true;
let price = 270;
let discount = 5;

console.log(productName, rating, isDeal, price, discount);

// Task 1 OR

let product1 = {
    productName: "Parkewr Jotter Standard CT Ball Pen(Black)",
    rating: 7002,
    isDeal: true,
    price: 270,
    discount: 5
};
console.log(product1);
console.log(product1.isDeal);
console.log(product1["rating"])


// Conditional Qs1
let num = 25; // take input from user instead
if (num%5 === 0){
    console.log("Yes");
}
else{
    console.log("No");
}

// Conditional Qs2
let marks = 69;
if (marks >100 || marks<0){
    console.log("Invalid Makrs");
}
else if (marks>=80){
    console.log("Your Grade is A")
}
else if (marks>=70){
    console.log("Your Grade is B")
}
else if (marks>=60){
    console.log("Your Grade is C")
}
else if (marks>=50){
    console.log("Your Grade is D")
}
else{
    console.log("You Failed");
}


// Loop Qs1
let r1 = "";
for(let i=0; i<=100; i++){
    if(i%2 === 0){
        r1 += i + " ";
    }
}
console.log("The even numbers: ",r1)

// loop Qs2
/*
let cValue = 23;
let gNum = prompt("Guess the number: ");
gNum = parseInt(gNum);  // Convert string into integer
while(gNum !== cValue){
    gNum = prompt("Guess another number: ");
    gNum = parseInt(gNum);
}
console.log("You won the game"); */



// String Qs1
/*
let givenName = prompt("Enter you full name: ");
givenName = givenName.toLowerCase();
let username = "@";
for(let i of givenName){
    if( i != " "){
        username+=i;
    }
}
username+= (username.length - 1);
console.log(username); */


// Array Qs2
let arr= [250,645,300,900,50];
for (let i=0; i<arr.length; i++){
    arr[i]= arr[i] - (arr[i] * 0.1);
}
console.log(arr);


// Function Qs1
function printVowels(s){
    rs=""
    for(i of s){
        if (i==="a" || i==="e" || i==="i" || i==="o" || i==="u" || i==="A" || i==="E" || i==="I" || i==="O" || i==="U"){
            rs+=i;
        }
    }
    return rs;
}
console.log(printVowels("JAVAscript"));

let arrowVowels = (s) => {
    rs=""
    for(i of s){
        if (i==="a" || i==="e" || i==="i" || i==="o" || i==="u" || i==="A" || i==="E" || i==="I" || i==="O" || i==="U"){
            rs+=i;
        }
    }
    return rs;
} 
console.log(arrowVowels("New String"));

