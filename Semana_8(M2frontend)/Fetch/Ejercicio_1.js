async function listarObjetos() {
    try {
      const res = await fetch("https://api.restful-api.dev/objects");
      const data = await res.json();
  

      const objetos = data.filter(obj => obj.data);
  
      objetos.forEach(obj => {
        const { name, data } = obj;
        const color = data.color || "N/A";
        const capacity = data.capacity || data["capacity GB"] || "N/A";
        console.log(`${name} (color: ${color}, capacity: ${capacity})`);
      });
    } catch (error) {
      console.error("Error al obtener los objetos:", error);
    }
  }
  
  listarObjetos();
  


  