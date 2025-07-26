async function getUserById(id) {
    try {
      const res = await fetch(`https://api.restful-api.dev/objects/${id}`);
  
      if (!res.ok) {
        throw new Error("User not found (404)");
      }
  
      const user = await res.json();
      console.log("User found:", user);
    } catch (error) {
      console.error("Error:", error.message);
    }
  }
  
  getUserById("your-object-id-here");
  