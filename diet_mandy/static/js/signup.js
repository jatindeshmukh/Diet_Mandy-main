document.getElementById("signupForm").addEventListener("submit", function(e) {
    e.preventDefault();

    const password = document.getElementById("password").value.trim();
    const confirm = document.getElementById("confirmPassword").value.trim();

    if (password !== confirm) {
        alert("❌ Passwords do not match!");
        return;
    }

    alert("✅ Signup successful! Welcome to Diet Mandy 🌿");
    this.reset();
});