//Toma un string y conviertelo en una lista de palabras, separandolas por espacios en blanco. No puedes usar la función split

let texto = "Hola mundo";

let palabra = "";

let palabras = [];

for (let i = 0; i < texto.length; i++) {
  let letra = texto[i];

  if (letra === " ") {
    palabras.push(palabra);
    palabra = "";
  } else {
    palabra += letra;
  }
}


if (palabra !== "") {
  palabras.push(palabra);
}

console.log(palabras); 
