const promesas = [
  new Promise(resolve => setTimeout(() => resolve("very"), 300)),
  new Promise(resolve => setTimeout(() => resolve("dogs"), 100)),
  new Promise(resolve => setTimeout(() => resolve("cute"), 400)),
  new Promise(resolve => setTimeout(() => resolve("are"), 200))
];

Promise.all(promesas)
  .then(result => {
    const ordenCorrecto = ["dogs", "are", "very", "cute"];
    const frase = ordenCorrecto.map(palabra => result.find(p => p === palabra)).join(" ");
    console.log(frase); 
  });
