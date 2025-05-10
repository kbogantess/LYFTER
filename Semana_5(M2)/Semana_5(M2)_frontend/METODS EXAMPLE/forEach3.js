const letters = ['a', 'b', 'a', 'e', 'e'];

let count = {};

letters.forEach(i => {

    if (count[i]) {
        count[i] ++;

    }else {
        count[i] = 1;
    }
});

console.log(count);