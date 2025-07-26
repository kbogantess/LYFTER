const axios = require('axios');

async function listObjects() {
  try {
    const res = await axios.get("https://api.restful-api.dev/objects");

    const objects = res.data.filter(obj => obj.data);

    objects.forEach(obj => {
      const { name, data } = obj;
      const color = data.color || "N/A";
      const capacity = data.capacity || data["capacity GB"] || "N/A";
      console.log(`${name} (color: ${color}, capacity: ${capacity})`);
    });
  } catch (error) {
    console.error("Failed to fetch objects:", error.message);
  }
}

listObjects();
