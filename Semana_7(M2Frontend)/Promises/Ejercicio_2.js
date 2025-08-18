const ids = [1, 4, 7];

const fetchPokemon = (id) =>
  fetch(`https://pokeapi.co/api/v2/pokemon/${id}`)
    .then(res => res.json());

Promise.any(ids.map(fetchPokemon))
  .then(poke => {
    console.log(`First resolved Pokémon: ${poke.name}`);
  })
  .catch(error => {
    console.error("All promises failed:", error);
  });
q