async function updateAddress(id, newAddress) {
    try {
      const res = await fetch(`https://api.restful-api.dev/objects/${id}`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          name: "Updated User",
          data: {
            address: newAddress
          }
        })
      });
  
      const result = await res.json();
      console.log("Address updated:", result);
    } catch (error) {
      console.error("Error updating address:", error.message);
    }
  }
  
  updateAddress("your-object-id-here", "123 Elm Street");
  