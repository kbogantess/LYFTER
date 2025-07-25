import fetch from 'node-fetch';

function ejercicio2() {
    const ids = [1, 4, 7];
    const requests = ids.map(id =>
        fetch(`https://pokeapi.co/api/v2/pokemon/${id}`).then(res => res.json())
    );

    Promise.any(requests)
        .then(result => {
            console.log("Ejercicio 2 - Promises:");
            console.log("Primer Pokémon resuelto:", result.name);
        })
        .catch(err => console.error("Error en ejercicio 2:", err.message));
}

ejercicio2();
