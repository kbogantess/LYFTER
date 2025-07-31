const axios = require('axios');

async function createUser(name, email, password, address) {
  try {
    const res = await axios.post("https://api.restful-api.dev/objects", {
      name,
      data: {
        email,
        password,
        address
      }
    });

    console.log("User created with ID:", res.data.id);
    console.log(res.data);
  } catch (error) {
    console.error("Error creating user:", error.message);
  }
}

createUser("Jane", "jane@example.com", "5678", "California");


