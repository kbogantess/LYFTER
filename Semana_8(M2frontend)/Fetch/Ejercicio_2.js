async function createUser(name, email, password, address) {
    const body = {
      name,
      data: {
        email,
        password,
        address
      }
    };
  
    try {
      const res = await fetch("https://api.restful-api.dev/objects", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(body)
      });
  
      const result = await res.json();
      console.log("User created with ID:", result.id);
      console.log(result);
    } catch (error) {
      console.error("Error creating user:", error);
    }
  }
  
  createUser("John", "john@example.com", "1234", "New York");
  



  