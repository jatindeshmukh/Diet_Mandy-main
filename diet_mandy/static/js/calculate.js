console.log("✅ calculate.js loaded successfully!");

// Safe number reading function
function getValue(id) {
    const v = document.getElementById(id).value;
    return v === "" || isNaN(v) ? null : parseFloat(v);
}

document.getElementById("calculateBtn").addEventListener("click", () => {
    const age = getValue("age");
    const weight = getValue("weight");
    const gender = document.getElementById("gender").value;
    const activity = parseFloat(document.getElementById("activity").value);
    const goal = document.getElementById("goal").value;

    // ✅ Height input in FEET → Convert to cm
    let heightFeet = document.getElementById("height").value;
    let height = heightFeet ? parseFloat(heightFeet) * 30.48 : null;

    if (!age || !height || !weight || !gender) {
        alert("⚠️ Please fill Age, Gender, Height (ft) & Weight!");
        return;
    }

    // ✅ BMI Calculation
    const bmi = (weight / Math.pow(height / 100, 2));
    let bmiStatus =
        bmi < 18.5 ? "Underweight" :
        bmi < 24.9 ? "Normal" :
        bmi < 29.9 ? "Overweight" : "Obese";

    // 🎯 Automatic suggestion based on BMI
    let autoGoalSuggestion =
        bmi < 18.5 ? "Recommended: Gain Weight 💪" :
        bmi < 24.9 ? "Recommended: Maintain Weight ✅" :
        "Recommended: Lose Weight 🏃‍♂️";

    // ✅ BMR (Mifflin-St Jeor)
    let bmr =
        gender === "male" ?
        10 * weight + 6.25 * height - 5 * age + 5 :
        10 * weight + 6.25 * height - 5 * age - 161;

    // ✅ TDEE
    let calories = bmr * activity;

    // ✅ Goal calories
    const calorieAdjustment = goal === "lose" ? -400 : goal === "gain" ? 350 : 0;
    calories += calorieAdjustment;

    // ✅ Macro ratios
    const macroRatios = {
        lose: { carbs: 0.40, protein: 0.35, fats: 0.25 },
        maintain: { carbs: 0.45, protein: 0.30, fats: 0.25 },
        gain: { carbs: 0.50, protein: 0.30, fats: 0.20 }
    };

    const ratios = macroRatios[goal];
    const carbs = (calories * ratios.carbs / 4).toFixed(1);
    const protein = (calories * ratios.protein / 4).toFixed(1);
    const fats = (calories * ratios.fats / 9).toFixed(1);

    // ✅ Display Results
    document.getElementById("bmi").textContent = bmi.toFixed(1);
    document.getElementById("bmiStatus").textContent = bmiStatus + " — " + autoGoalSuggestion;
    document.getElementById("bmr").textContent = Math.round(bmr);
    document.getElementById("calories").textContent = Math.round(calories);
    document.getElementById("carbs").textContent = carbs;
    document.getElementById("protein").textContent = protein;
    document.getElementById("fats").textContent = fats;

    document.getElementById("results").classList.remove("hidden");
});

// ✅ Diet Plan Message
document.getElementById("generatePlanBtn").addEventListener("click", () => {
    const name = document.getElementById("name").value || "User";
    const goal = document.getElementById("goal").value;
    const pref = document.getElementById("foodPreference").value;

    let message =
        goal === "lose" ? `🌱 ${name}, choose high-protein, low-carb foods & increase fiber.` :
        goal === "gain" ? `🍚 ${name}, increase calories with nuts, paneer, ghee & rice.` :
        `🥗 ${name}, keep a balanced diet with grains, veggies & protein.`;

    if (pref === "jain") message += " (Jain friendly – avoid root vegetables)";
    if (pref === "vegan") message += " (Use tofu, lentils, soy for protein)";

    const box = document.getElementById("dietPlanMessage");
    box.textContent = message;
    box.classList.remove("hidden");
});