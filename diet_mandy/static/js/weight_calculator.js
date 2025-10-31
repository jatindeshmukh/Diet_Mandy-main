const idealWeights = {
    male: {
        "5.0": [52, 65],
        "5.3": [58, 72],
        "5.6": [63, 80],
        "5.9": [69, 88],
    },
    female: {
        "5.0": [46, 58],
        "5.3": [50, 64],
        "5.6": [55, 70],
        "5.9": [61, 77],
    },
};

document.getElementById("checkBtn").addEventListener("click", () => {
    const gender = document.getElementById("gender").value;
    const height = document.getElementById("height").value;
    const weight = parseFloat(document.getElementById("weight").value);

    if (!weight) {
        document.getElementById("result").innerText = "⚠️ Enter your weight!";
        return;
    }

    const [min, max] = idealWeights[gender][height];

    let message = `Ideal Weight Range: <b>${min}kg - ${max}kg</b><br>`;

    if (weight < min) {
        message += `📉 You are underweight. Try to gain healthy weight.`;
    } else if (weight > max) {
        message += `📈 You are overweight. Consider weight loss.`;
    } else {
        message += `✅ Perfect! You are in healthy weight range.`;
    }

    document.getElementById("result").innerHTML = message;
});