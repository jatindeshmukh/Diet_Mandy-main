document.getElementById('loginForm').addEventListener('submit', (e) => {
    e.preventDefault();
    alert("Login successful (demo). Redirecting to profile...");
    window.location.href = "profile.html";
});