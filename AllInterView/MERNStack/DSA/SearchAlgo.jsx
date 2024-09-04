
let data = [10, 20, 30, 40, 50, 60, 80];
let op = 20;
for (let i = 0; i < data.length; i++) {
    if (data[i] > op) {
        console.log(data[i]);
    } else {
        console.log("Number is greater than ",op);
    }
}



////  ------------------>> Filter with a letter  ////////////  ------------->

function filter(str, letter) {
   let filteredStr = [];
   for (let i = 0; i < str.length; i++) {
       if (str[i][0].toLowerCase() !== letter.toLowerCase()) {  // !==  ====
           console.log(str[i]);
           filteredStr.push(str[i]);  // Add the element to filteredStr if it meets the condition
       } else {
           console.log("The first letter is not", letter);
       }
   }
   return filteredStr;
}
let str = ['jugal', 'aki', 'boy', 'cart', 'aus', 'arabic', 'body'];
let letter = "c";
let result = filter(str, letter);
console.log("Filtered array:", result);






// object serach with index number  ----> ----------------------
const objs = {
   0: {
       name: "Jugal",
       rollno: 45,
       identity: { hashPanCard: false, hashAdhaarCard: true },
   },
   1: {
       name: "Karan",
       rollno: 20,
       identity: { hashPanCard: false, hashAdhaarCard: true },
   }
};

console.log(objs)
let search = 1;
let post = undefined;

for (let i in objs) { // Looping through keys of the object
   if (i == search) { // Checking if the key matches `search`
       post = objs[i]; // Assigning the matching object to `post`
       break; // Exit loop once found
   }
}

console.log(post);








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
