fetch('https://reqres.in/api/users/2')
  .then(response => {
    if (!response.ok) {
      throw new Error('Request failed with status: ' + response.status);
    }
    return response.json();
  })
  .then(data => {
    const user = data.data;
    console.log("User found:");
    console.log("ID:", user.id);
    console.log("Name:", user.first_name, user.last_name);
    console.log("Email:", user.email);
    console.log("Avatar:", user.avatar);
  })
  .catch(error => {
    console.error("There was a problem retrieving the user:", error);
  });
