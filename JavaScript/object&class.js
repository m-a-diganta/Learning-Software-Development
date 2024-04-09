const student ={ // Object
    fullName: "Arabi Hossain",
    marks: 90,
    printMarks: function (){ //methods
        console.log(this.fullName," : ",this.marks); //this => student
    }
}

console.log(student.fullName);
console.log(student.marks);
student.printMarks();
console.log(student);

// Each object has a special property called protoype that has its own predefined objects and methods

const employee ={
    calcTax(){
        console.log("Tax rate = 10%");
    },
};

const ahil ={
    salary:5000,
};

ahil.__proto__ = employee;  //including employee in the object list of ahil's prototype

ahil.calcTax();


// Classes in JS 
class toyotaCar{
    constructor(brandName){
        console.log("Creating a new object");
        this.brandName = brandName;
    }
    start(){
        console.log(`${this.brandName} started`);
    } // no need to use comma like we do in objects
    stop(){
        console.log(`Car stopped`);
    }
    setColor(color){
        this.color = color;
    }
}

let fortuner = new toyotaCar("Fortuner");
let lexus = new toyotaCar("Lexus");
console.log(fortuner);
console.log(lexus);

fortuner.start();
lexus.stop();
fortuner.setColor("Red");
console.log(fortuner.color);

fortuner.brandName = "Fortuner 2.0";
fortuner.start();


// Inheritance in JS
class Parent{
    hello(){
        console.log("Hello"); 
    }
}
class Child extends Parent{
    work(){
        console.log("Working");
    }
}

let newObj = new Child();
newObj.work();
newObj.hello(); // Inheriting from Parent

//method overrriding


// super constructor
class Person{
    constructor(name){
        this.name = name;
        this.species = "Homo Sapiens";
    }
    eat(){
        console.log("Eating");
    }
}
class Engineer extends Person{
    constructor(branch){
        super(); // to invoke parent class constructor
        this.branch = branch;
    }
}
class Doctor extends Person{
    constructor(branch,name){
        super(name); 
        this.branch = branch;
    }
    work(){
        console.log("Currently");
        super.eat(); // to invoke parent class method
    }
}

let engObj = new Engineer("Chemical");
console.log(engObj.branch,"Engineer");
console.log(engObj);

let docObj = new Doctor("Medicine","Ahil");
console.log(docObj.branch,"Doctor");
console.log(docObj.name);
console.log(docObj);
docObj.work();


// In case of doubt about a portion of code
let a= 10;
let b=2;
try{
    console.log("a+b=",a+c);
}
catch(err){
    console.log("Error"); // the program still executes
    // console.log(err);
}