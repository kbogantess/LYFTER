const API = 'https://api.restful-api.dev/objects';

function show(sectionId) {
  document.querySelectorAll('.container').forEach(div => div.classList.add('hidden'));
  document.getElementById(sectionId).classList.remove('hidden');
}

if (localStorage.getItem('userId')) {
  show('profile');
  loadProfile();
} else {
  show('register');
}

// Register
document.getElementById('registerForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  const name = document.getElementById('name').value.trim();
  const email = document.getElementById('email').value.trim();
  const password = document.getElementById('password').value.trim();
  const address = document.getElementById('address').value.trim();

  const body = {
    name: name,
    data: {
      email,
      password,
      address
    }
  };

  try {
    const res = await fetch(API, {
      method: 'POST',
      body: JSON.stringify(body),
      headers: { 'Content-Type': 'application/json' }
    });

    const user = await res.json();
    localStorage.setItem('userId', user.id);
    alert(`User created successfully! Your ID is ${user.id}`);
    show('login');
  } catch (err) {
    document.getElementById('registerMessage').textContent = "Registration error: " + err.message;
  }
});

// Login
document.getElementById('loginForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  const id = document.getElementById('loginId').value.trim();
  const pass = document.getElementById('loginPass').value.trim();

  try {
    const res = await fetch(`${API}/${id}`);
    if (!res.ok) throw new Error("User not found");
    const user = await res.json();
    const correctPassword = user.data?.password;

    if (correctPassword === pass) {
      localStorage.setItem('userId', id);
      show('profile');
      loadProfile();
    } else {
      document.getElementById('loginMessage').textContent = "Incorrect password.";
    }
  } catch (err) {
    document.getElementById('loginMessage').textContent = "Error: " + err.message;
  }
});

// Load profile
async function loadProfile() {
  const id = localStorage.getItem('userId');
  if (!id) {
    show('login');
    return;
  }

  try {
    const res = await fetch(`${API}/${id}`);
    if (!res.ok) throw new Error("User not found");
    const user = await res.json();

    const { name, data } = user;
    const profileHTML = `
      <p><strong>Name:</strong> ${name}</p>
      <p><strong>Email:</strong> ${data.email}</p>
      <p><strong>Address:</strong> ${data.address}</p>
    `;
    document.getElementById('profileData').innerHTML = profileHTML;
  } catch (err) {
    document.getElementById('profileData').textContent = "Error loading profile.";
  }
}

// Logout
document.getElementById('logout').addEventListener('click', () => {
  localStorage.removeItem('userId');
  show('login');
});

// Change password
document.getElementById('changeForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  const id = localStorage.getItem('userId');
  const oldPassword = document.getElementById('oldPassword').value.trim();
  const newPassword = document.getElementById('newPassword').value.trim();
  const confirmPassword = document.getElementById('confirmPassword').value.trim();
  const msg = document.getElementById('changeMessage');

  try {
    const res = await fetch(`${API}/${id}`);
    if (!res.ok) throw new Error("User not found");
    const user = await res.json();

    if (user.data?.password !== oldPassword) {
      msg.textContent = "Current password is incorrect.";
      return;
    }

    if (newPassword !== confirmPassword) {
      msg.textContent = "New password does not match confirmation.";
      return;
    }

    user.data.password = newPassword;

    const updateRes = await fetch(`${API}/${id}`, {
      method: 'PUT',
      body: JSON.stringify({ name: user.name, data: user.data }),
      headers: { 'Content-Type': 'application/json' }
    });

    if (!updateRes.ok) throw new Error("Error updating password.");
    msg.textContent = "Password successfully updated.";
  } catch (err) {
    msg.textContent = "Error: " + err.message;
  }
});
