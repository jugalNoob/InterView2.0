
let data = [10, 20, 30, 40, 50, 60, 80];
let op = 20;
for (let i = 0; i < data.length; i++) {
    if (data[i] > op) {
        console.log(data[i]);
    } else {
        console.log("Number is greater than ",op);
    }
}






let obj = {
   name: "Jugal",
   hobbies:["walking" , "Reading"],
   age: 25,
   country: "India",
   identity:{hashPanCard:false , hashAdhaarCard:true},
   address: ["India", "USA"] // Changed {} to []
};


console.log(obj.hobbies[0])
console.log(obj.name)
console.log(obj.identity.hashPanCard)






const objArray = [
   {
       index: 0,
       details: {
           name: "jugal",
           rollno: 45,
           identity:{hashPanCard:false , hashAdhaarCard:true},
       }
   },
   {
       index: 1,
       details: {
           name: "karan",
           rollno: 20,
           identity:{hashPanCard:false , hashAdhaarCard:true},
       }
   }
];

console.log(objArray)

console.log(objArray[0])


const objs = {
    0: {
        name: "jugal",
        rollno: 45,
        identity:{hashPanCard:false , hashAdhaarCard:true},
    },
    1: {
        name: "karan",
        rollno: 20,
        identity:{hashPanCard:false , hashAdhaarCard:true},
    }
};





console.log(objs)
