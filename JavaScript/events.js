let button3 = document.querySelector(".button3");
button3.onclick = () =>{
    button3.style.backgroundColor = "green";
    console.log("button3 is clicked");
} // Event handling on JS has more priority than inline handling

// Event Object
button3.onclick = (e) =>{
    button3.style.backgroundColor = "green";
    console.log("button3 is clicked");
    console.log(e);
    console.log(e.type);
    console.log(e.target);
} 

// Event Listener

const firstHandler = () =>{
    console.log("1st eventListener for button3");
};

button3.addEventListener("click",firstHandler );

button3.addEventListener("click", (e) =>{
    console.log("2nd eventListener for button3");
    console.log(e);
});

// button3.removeEventListener("click",firstHandler );

// Qs

let modeButton = document.querySelector(".screenMode");
console.log(modeButton);
let currentMode = "light";

modeButton.addEventListener("click",() =>{
    if (currentMode === "light") {
        currentMode = "dark";
        document.querySelector("body").style.backgroundColor= "darkGray";
    }
    else{
        currentMode="light";
        document.querySelector("body").style.backgroundColor= "white";
    }
    console.log(currentMode);
});