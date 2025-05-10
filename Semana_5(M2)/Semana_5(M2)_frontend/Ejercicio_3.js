//Toma una lista de temperaturas en grados celsius y conviertala a farenheit utilizando la función map

const celsiusTemperatures = [0, 5, 10, 15, 20];

const transformToFarenheit = celsiusTemperatures.map((temperature) => {
    return ((( temperature * 9) / 5) + 32);
})

console.log(transformToFarenheit);
