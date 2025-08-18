document.getElementById("changeForm").addEventListener("submit", async (e) => {
    e.preventDefault();
  
    const userId = localStorage.getItem("userId");
    const oldPassword = document.getElementById("oldPassword").value.trim();
    const newPassword = document.getElementById("newPassword").value.trim();
    const confirmPassword = document.getElementById("confirmPassword").value.trim();
    const message = document.getElementById("message");
  
    try {
      const res = await axios.get(`https://api.restful-api.dev/objects/${userId}`);
      const user = res.data;
      const currentPassword = user.data?.password;
  
      if (currentPassword !== oldPassword) {
        message.textContent = "Current password is incorrect.";
        return;
      }
  
      if (newPassword !== confirmPassword) {
        message.textContent = "New password does not match confirmation.";
        return;
      }
  
      const updatedUser = {
        name: user.name,
        data: {
          ...user.data,
          password: newPassword
        }
      };
  
      await axios.put(`https://api.restful-api.dev/objects/${userId}`, updatedUser, {
        headers: {
          "Content-Type": "application/json"
        }
      });
  
      message.textContent = "Password updated successfully.";
    } catch (error) {
      message.textContent = "Error updating password: " + error.message;
    }
  });



  