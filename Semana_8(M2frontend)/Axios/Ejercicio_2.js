document.getElementById("loginForm").addEventListener("submit", async (e) => {
    e.preventDefault();
  
    const userId = document.getElementById("userId").value.trim();
    const passwordInput = document.getElementById("password").value.trim();
    const message = document.getElementById("message");
  
    try {
      const res = await axios.get(`https://api.restful-api.dev/objects/${userId}`);
      const user = res.data;
      const savedPassword = user.data?.password;
  
      if (savedPassword?.trim() === passwordInput) {
        localStorage.setItem("userId", userId);
        window.location.href = "profile.html";
      } else {
        message.textContent = "Incorrect password.";
      }
    } catch (error) {
      message.textContent = "Error: " + error.message;
    }
  });
  