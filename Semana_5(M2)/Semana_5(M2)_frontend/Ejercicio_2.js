/* 2-Realiza un programa que recorra una lista de 
números y almacene todos los pares en otra lista
Para este ejercicio intenta hacer una solución
con un for y otra utilizando la función filter */



//FILTER



const myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

const evenNumbers = myList.filter((n) => n % 2 === 0);

console.log("Even: " , evenNumbers);



//FOR


const numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

const even = []; //Se crea un array vacio para almacenar los pares

for (let i = 0; i < numeros.length; i++) { //Empieza en i = 0 y se ejecuta mientras i sea menor a la longitud de la lista. luego se incrementa i en 1

  if (numeros[i] % 2 === 0) {

    even.push(numeros[i]); //Push va agregando a la derecha
  }
}

console.log("Even numbers:", even);