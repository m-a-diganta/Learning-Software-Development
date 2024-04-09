console.log("before statement");

setTimeout(()=>{ //executes parallely
    console.log("3 seconds passed");
},3000); 

console.log("after statement"); 


// Callback Function
function sum(a,b){
    console.log(a+b);
}
function calc(a,b, sumCallback){
    sumCallback(a,b);
}
calc(1,4,sum); // passing function as an argument



// Callback Hell - nested callbacks
// need to get data one by one, each takes 2 seconds

function getData(dataID1,get_dataID2){
    setTimeout(()=>{
        console.log("Data", dataID1);
        if (get_dataID2){
            get_dataID2();
        }
    },2000);
}

getData(1,()=>{
    getData(2,()=>{
        getData(3,()=>{
            getData(4);
        });
    });
});



// Promises in JS - solution to Callback Hell
let promise = new Promise((resolve,reject)=>{
    console.log("This a promise");
    // resolve("Success");
    reject("Error Occurred");
})
console.log(promise);



// Async Wait