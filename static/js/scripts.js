const loginBtn = document.getElementById("login-btn");
const usernameInput = document.getElementById("username");
const passwordInput = document.getElementById("password");
const errorMsg = document.getElementById("error-msg");

loginBtn.addEventListener("click", (e) => {
  e.preventDefault();
  const username = usernameInput.value;
  const password = passwordInput.value;

  if (username === "dummy" && password === "dummy") {
    window.location.href = "index.html";
    toastr.success("Successfully logged in!");
  } else {
    errorMsg.textContent = "Invalid username or password";
  }
});

// Navbar functionality
const menuIcon = document.querySelector("#menu-icon");
const navbar = document.querySelector(".navbar");
const navbg = document.querySelector(".nav-bg");
menuIcon.addEventListener("click", () => {
  menuIcon.classList.toggle("bx-x");
  navbar.classList.toggle("active");
  navbg.classList.toggle("active");
});
