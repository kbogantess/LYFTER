async function getUserNotFound() {
    try {
      const response = await fetch('https://reqres.in/api/users/23');
  
      if (!response.ok) {
        throw new Error("User not found");
      }
  
      const data = await response.json();
      console.log(data.data);
    } catch (error) {
      console.error("Error:", error.message);
    }
  }
  
  getUserNotFound();
  