function checkNumber(number, evenCallback, oddCallback) {
  if (number % 2 === 0) {
      evenCallback();
  } else {
      oddCallback();
  }
}

checkNumber(9, 
  () => console.log("The number is even!"), 
  () => console.log("The number is odd!")
);
