// Function - removes redundancy
// Whats HOF or Higher Order Functions

function prntFunc(){
    console.log("Let's work with functions");
}
prntFunc();

function sum(a,b){ // parameters are local variables of the function
    sum = a+b;
    return sum;
    console.log("After return");
}
console.log("The sum is ",sum(4,5));

// Arrow Function
let arrowSum = (a,b) => {  // function saved as a variable
    console.log(a+b);
};
arrowSum(3,4);
console.log("-----------------------------");


// "forEach" call-back function/ method
let arr= ["Dhaka", "Rajshahi", "Chittagong"]; 
arr.forEach((val, idx, arr)=>{  // cant be used for string
    console.log(val.toUpperCase(),"Insex = ",idx, arr);
});

// map method
let newArr = arr.map((val,idx)=>{
    return val+" - "+idx;
})
console.log(newArr); 

// Filter method
nums= [5,3,4,6,2,4,3,9,8];
let evenNums = nums.filter((val)=>{
    return val%2==0;
});
console.log(evenNums);

// Reduce method => gives a single output from an array
let sumArr = nums.reduce((res,current)=>{
    return res+current; // the summation gets stroed into res again
});
console.log(sumArr);

let maxNum = nums.reduce((res,current)=>{ 
    return res>current ? res:current; // finding max number
});
console.log(maxNum);