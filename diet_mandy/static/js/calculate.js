console.log("✅ calculate.js loaded successfully!");
document.getElementById("calculateBtn").addEventListener("click", () => {
    const age = parseInt(document.getElementById("age").value);
    const gender = document.getElementById("gender").value;
    const height = parseFloat(document.getElementById("height").value);
    const weight = parseFloat(document.getElementById("weight").value);
    const activity = parseFloat(document.getElementById("activity").value);
    const goal = document.getElementById("goal").value;

    if (!age || !height || !weight || !gender) {
        alert("Please fill all required fields!");
        return;
    }

    // BMI Calculation
    const bmi = (weight / ((height / 100) ** 2)).toFixed(1);
    let bmiStatus = "";
    if (bmi < 18.5) bmiStatus = "Underweight";
    else if (bmi < 24.9) bmiStatus = "Normal / Healthy";
    else if (bmi < 29.9) bmiStatus = "Overweight";
    else bmiStatus = "Obese";

    // BMR Calculation (Mifflin-St Jeor)
    let bmr;
    if (gender === "male") {
        bmr = 10 * weight + 6.25 * height - 5 * age + 5;
    } else {
        bmr = 10 * weight + 6.25 * height - 5 * age - 161;
    }

    // TDEE (Total Daily Energy Expenditure)
    let calories = bmr * activity;

    if (goal === "lose") calories -= 500;
    if (goal === "gain") calories += 500;

    // Macro Ratios (based on goal)
    let carbPercent, proteinPercent, fatPercent;

    if (goal === "lose") {
        carbPercent = 0.4;
        proteinPercent = 0.3;
        fatPercent = 0.3;
    } else if (goal === "gain") {
        carbPercent = 0.5;
        proteinPercent = 0.3;
        fatPercent = 0.2;
    } else {
        carbPercent = 0.45;
        proteinPercent = 0.25;
        fatPercent = 0.3;
    }

    const carbs = ((calories * carbPercent) / 4).toFixed(1);
    const protein = ((calories * proteinPercent) / 4).toFixed(1);
    const fats = ((calories * fatPercent) / 9).toFixed(1);

    // Display Results
    document.getElementById("bmi").textContent = bmi;
    document.getElementById("bmiStatus").textContent = bmiStatus;
    document.getElementById("bmr").textContent = Math.round(bmr);
    document.getElementById("calories").textContent = Math.round(calories);
    document.getElementById("carbs").textContent = carbs;
    document.getElementById("protein").textContent = protein;
    document.getElementById("fats").textContent = fats;

    document.getElementById("results").classList.remove("hidden");
});

// Generate Diet Plan Button
document.getElementById("generatePlanBtn").addEventListener("click", () => {
    const name = document.getElementById("name").value || "User";
    const goal = document.getElementById("goal").value;
    const pref = document.getElementById("foodPreference").value;

    let message = "";

    if (goal === "lose") {
        message = `🌱 ${name}, for weight loss, focus on high-protein meals with salads and avoid sugary foods.`;
    } else if (goal === "gain") {
        message = `🍚 ${name}, for weight gain, include calorie-dense foods like nuts, milk, rice, and paneer (or tofu for vegans).`;
    } else {
        message = `🥗 ${name}, for maintenance, balance your diet with whole grains, lean protein, and veggies.`;
    }

    if (pref === "jain") message += " Avoid root vegetables and ensure all meals are Jain-friendly.";
    if (pref === "vegan") message += " Include soy, lentils, and nuts for protein.";

    const msgBox = document.getElementById("dietPlanMessage");
    msgBox.textContent = message;
    msgBox.classList.remove("hidden");
});