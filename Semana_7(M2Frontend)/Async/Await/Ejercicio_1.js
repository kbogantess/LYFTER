async function getUser() {
    try {
    const response = await fetch('https://reqres.in/api/users/2');
    const data = await response.json();
    console.log("User received:");
    console.log(data.data);
    } catch (error) {
    console.error("Error obtaining user", error);
    }
}

getUser(); 