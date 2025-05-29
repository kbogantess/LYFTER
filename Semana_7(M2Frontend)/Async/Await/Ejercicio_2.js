fetch('https://reqres.in/api/users/23')
  .then(response => {
    if (!response.ok) {
      throw new Error('User not found (status code: ' + response.status + ')');
    }
    return response.json();
  })
  .then(data => {
    const user = data.data;
    console.log("User found:");
    console.log("ID:", user.id);
    console.log("Name:", user.first_name, user.last_name);
    console.log("Email:", user.email);
  })
  .catch(error => {
    console.error("Error:", error.message);
  });
