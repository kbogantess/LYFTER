const numbers = [1, 2, 3, 4, 5];

const numDouble = numbers.map(double);
//const mult = numbers.map(multiply);

function double(value) {
    return value * 2;
}

//function multiply(value){
    //return value * index;
//}

console.log(numDouble);
//console.log(mult);