document.addEventListener("DOMContentLoaded", function () {
    // Handle Calories Burnt Prediction
    const predictionForm = document.getElementById("predictionForm");
    if (predictionForm) {
        predictionForm.addEventListener("submit", function (event) {
            event.preventDefault();
            const formData = {
                Gender: parseInt(document.getElementById("gender").value),
                Age: parseInt(document.getElementById("age").value),
                Height: parseFloat(document.getElementById("height").value),
                Weight: parseFloat(document.getElementById("weight").value),
                Duration: parseFloat(document.getElementById("duration").value),
                Heart_Rate: parseFloat(document.getElementById("heart_rate").value),
                Body_Temp: parseFloat(document.getElementById("body_temp").value)
            };
            fetch("/predict", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(formData)
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById("result").innerText = `Your calories burnt ${data.calories_burnt} %`;
            })
            .catch(error => {
                console.error("Error:", error);
                document.getElementById("result").innerText = "Error predicting calories burnt.";
            });
        });
    }

    // Handle BMI Calculation with Diet Report
    const bmiForm = document.getElementById("bmiForm");
    if (bmiForm) {
        let currentDietPlan = "";

        bmiForm.addEventListener("submit", async function (event) {
            event.preventDefault();

            const height = parseFloat(document.getElementById("bmi_height").value);
            const weight = parseFloat(document.getElementById("bmi_weight").value);
            const bmiResult = document.getElementById("bmiResult");
            const dietPlan = document.getElementById("dietPlan");

            // Reset UI elements
            dietPlan.innerHTML = "";
            dietPlan.style.display = "none";

            if (!height || !weight || height <= 0 || weight <= 0) {
                bmiResult.innerHTML = "⚠️ Please enter valid height and weight!";
                return;
            }

            try {
                const response = await fetch("/bmi_calc", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ height, weight })
                });

                const data = await response.json();

                if (response.ok) {
                    bmiResult.innerHTML = `
                        <div class="bmi-result">
                            <span class="bmi-value">BMI: ${data.bmi}</span>
                            <span class="bmi-category">(${data.category})</span>
                            <button class="report-btn">📄 Show Diet Report</button>
                        </div>
                    `;
                    currentDietPlan = data.diet_plan;
                } else {
                    bmiResult.textContent = `Error: ${data.message}`;
                }
            } catch (error) {
                bmiResult.innerHTML = "⚠️ Error connecting to the server!";
                console.error("Fetch error:", error);
            }
        });

        // Toggle diet plan visibility
        document.addEventListener("click", function(e) {
            if(e.target.classList.contains("report-btn")) {
                const dietPlan = document.getElementById("dietPlan");
                const button = e.target;
                
                if(dietPlan.style.display === "none" || !dietPlan.style.display) {
                    dietPlan.innerHTML = currentDietPlan;
                    dietPlan.style.display = "block";
                    button.textContent = "📕 Hide Diet Report";
                    dietPlan.scrollIntoView({ behavior: "smooth" });
                } else {
                    dietPlan.style.display = "none";
                    button.textContent = "📄 Show Diet Report";
                }
            }
        });
    }

    // Handle BMR and TDEE Calculation
    const bmrTdeeForm = document.getElementById("bmrTdeeForm");
    if (bmrTdeeForm) {
        bmrTdeeForm.addEventListener("submit", function (event) {
            event.preventDefault();
            const formData = {
                age: parseInt(document.getElementById("bmr_age").value),
                gender: parseInt(document.getElementById("bmr_gender").value),
                weight: parseFloat(document.getElementById("bmr_weight").value),
                height: parseFloat(document.getElementById("bmr_height").value),
                activity_level: document.getElementById("activity_level").value
            };
            fetch("/bmr_tdee_calc", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(formData)
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById("bmrTdeeResult").innerText = `BMR is ${data.bmr}, TDEE is ${data.tdee}`;
            })
            .catch(error => {
                console.error("Error:", error);
                document.getElementById("bmrTdeeResult").innerText = "Error calculating BMR and TDEE.";
            });
        });
    }
});