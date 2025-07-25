<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <title>Search user</title>
  </head>
  <body>
    <h2>Search user by ID</h2>
    <input type="number" id="userIdInput" placeholder="Enter ID" />
    <button id="searchBtn">Buscar</button>
    <div id="result"></div>

    <script>
      const input = document.getElementById("userIdInput");
      const button = document.getElementById("searchBtn");
      const resultado = document.getElementById("resultado");

      button.addEventListener("click", async () => {
        const userId = input.value.trim();

        if (!userId) {
          resultado.textContent = "Use a valid ID";
          return;
        }

        try {
          const response = await fetch(`https://reqres.in/api/users/${userId}`);

          if (!response.ok) {
            throw new Error("User not found or invalid ID");
          }

          const data = await response.json();
          const user = data.data;

          resultado.innerHTML = `
          <p><strong>Nombre:</strong> ${user.first_name}</p>
          <p><strong>Apellido:</strong> ${user.last_name}</p>
          <p><strong>Email:</strong> ${user.email}</p>
        `;
        } catch (error) {
          resultado.innerHTML = `<p style="color:red;">${error.message}</p>`;
        }
      });
    </script>
  </body>
</html>
