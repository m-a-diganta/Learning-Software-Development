// API => Application Programming Interface

const url = "https://cat-fact.herokuapp.com/facts";
const factP = document.querySelector(".fact");
const button1= document.querySelector(".button1");

const getFacts = async ()=>{
    console.log("Getting data....")
    let response = await fetch(url);
    console.log(response);  // JSON format
    let data = await response.json();
    console.log(data);
    console.log(data[0].text);
    factP.innerText = data[0].text;
}
button1.addEventListener("click",getFacts);


// same with promises
const factP2 = document.querySelector(".fact2");
const button2= document.querySelector(".button2");
function getFacts2(){
    fetch(url)
    .then((response)=>{
        return response.json();
    })
    .then((data2)=>{
        console.log(data2);
        console.log(data2[1].text);
        factP2.innerText= data2[1].text;
    })
}
button2.addEventListener("click",getFacts2);

