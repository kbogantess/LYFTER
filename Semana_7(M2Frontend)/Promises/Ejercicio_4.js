const ids = [1, 2, 3];

const fetchPokemon = (id) =>
  fetch(`https://pokeapi.co/api/v2/pokemon/${id}`).then(res => res.json());

Promise.all(ids.map(fetchPokemon))
  .then(pokemons => {
    pokemons.forEach(poke => {
      console.log(`Pokémon: ${poke.name}`);
    });
  })
  .catch(error => {
    console.error("Error occurred:", error);
  })
  .finally(() => {
    console.log("Request completed.");
  });
