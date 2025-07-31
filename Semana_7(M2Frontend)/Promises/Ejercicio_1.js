const ids = [1, 4, 7]; 

const fetchPokemon = (id) =>
  fetch(`https://pokeapi.co/api/v2/pokemon/${id}`)
    .then(res => res.json());

Promise.all(ids.map(fetchPokemon))
  .then(pokemons => {
    pokemons.forEach(poke => {
      console.log(`Pokémon: ${poke.name}`);
    });
  })
  .catch(error => {
    console.error("Something went wrong:", error);
  });
