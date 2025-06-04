from flask import Flask, redirect, url_for, session, flash, request, jsonify, render_template
import pandas as pd
import joblib

# Initialize Flask app
app = Flask(__name__)
app.secret_key = "a_your_secret_key"  # Required for session management

# Load the trained model for calories burnt prediction
model = joblib.load('calories_model.pkl')

# Default credentials
DEFAULT_USERNAME = "admin"
DEFAULT_PASSWORD = "123"  # Changed to match your specified password

# Home Page Route
@app.route("/")
def home():
    if 'user' not in session:
        flash("Please log in to access the app!", "info")
        return redirect(url_for('login'))
    return render_template("index.html")

# Route for Calories Burnt Prediction Page
@app.route('/calories')
def calories_page():
    if 'user' not in session:
        flash("Please log in to access the app!", "info")
        return redirect(url_for('login'))
    return render_template('calories.html')


# Route for BMI Calculator Page
@app.route('/bmi')
def bmi_page():
    if 'user' not in session:
        flash("Please log in to access the app!", "info")
        return redirect(url_for('login'))
    return render_template('bmi.html')

# Route for BMR & TDEE Calculator Page
@app.route('/bmr_tdee')
def bmr_tdee_page():
    if 'user' not in session:
        flash("Please log in to access the app!", "info")
        return redirect(url_for('login'))
    return render_template('bmr_tdee.html')

# API Endpoint for Calories Burnt Prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        df = pd.DataFrame([data])
        prediction = model.predict(df)
        return jsonify({'calories_burnt': float(prediction[0])})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

# API Endpoint for BMI Calculation
# ... [previous imports and setup remain same]

@app.route('/bmi_calc', methods=['POST'])
def bmi_calc():
    try:
        data = request.get_json()
        height = data['height'] / 100  # Convert cm to meters
        weight = data['weight']
        bmi = weight / (height ** 2)

        # BMI Category and Diet Plan
        if bmi < 18.5:
            category = "Underweight"
            diet_plan = """
                <h3>📉 Underweight Diet Plan</h3>
                <ul>
                    <li>🍳 Breakfast: 3 eggs + 2 toast + 1 banana</li>
                    <li>🥜 Snack: Mixed nuts & dried fruits</li>
                    <li>🍗 Lunch: Grilled chicken with rice & veggies</li>
                    <li>🥛 Snack: Protein shake with oats</li>
                    <li>🐟 Dinner: Salmon with sweet potato</li>
                    <li>💡 Tip: Add healthy calories with nut butters</li>
                </ul>
            """
        elif 18.5 <= bmi < 25:
            category = "Normal"
            diet_plan = """
                <h3>⚖️ Maintenance Diet Plan</h3>
                <ul>
                    <li>🍳 Breakfast: Oatmeal with berries</li>
                    <li>🥑 Snack: Greek yogurt with nuts</li>
                    <li>🍗 Lunch: Quinoa salad with grilled meat</li>
                    <li>🥬 Snack: Veggies with hummus</li>
                    <li>🐟 Dinner: Grilled fish with brown rice</li>
                    <li>💡 Tip: Maintain balanced macros</li>
                </ul>
            """
        else:
            category = "Overweight"
            diet_plan = """
                <h3>📈 Weight Loss Diet Plan</h3>
                <ul>
                    <li>🍳 Breakfast: Veg omelette + green tea</li>
                    <li>🥒 Snack: Cucumber & carrot sticks</li>
                    <li>🍗 Lunch: Grilled chicken salad</li>
                    <li>🌰 Snack: Small handful of almonds</li>
                    <li>🐟 Dinner: Steamed fish with veggies</li>
                    <li>💡 Tip: Focus on portion control</li>
                </ul>
            """

        return jsonify({
            'bmi': round(bmi, 2),
            'category': category,
            'diet_plan': diet_plan
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

# ... [rest of the routes remain same]

# API Endpoint for BMR and TDEE Calculation
@app.route('/bmr_tdee_calc', methods=['POST'])
def bmr_tdee_calc():
    try:
        data = request.get_json()
        age = data['age']
        gender = data['gender']  # 0 for Male, 1 for Female
        weight = data['weight']
        height = data['height']
        activity_level = data['activity_level']  # Sedentary, Light, Moderate, Active, Very Active

        # Calculate BMR using Harris-Benedict Equation
        if gender == 0:  # Male
            bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
        else:  # Female
            bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

        # Activity Multipliers for TDEE Calculation
        activity_multipliers = {
            'Sedentary': 1.2,
            'Light': 1.375,
            'Moderate': 1.55,
            'Active': 1.725,
            'Very Active': 1.9
        }
        tdee = bmr * activity_multipliers.get(activity_level, 1.2)

        return jsonify({'bmr': round(bmr, 2), 'tdee': round(tdee, 2)})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

# Login Route
@app.route("/login", methods=['GET', 'POST'])
def login():
    if 'user' in session:
        flash("You are already logged in!", "info")
        return redirect(url_for('home'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == DEFAULT_USERNAME and password == DEFAULT_PASSWORD:
            session['user'] = username
            flash("Login successful!", "success")
            return redirect(url_for('home'))
        else:
            flash("Invalid username or password!", "danger")  # Updated to match the flash message category
    return render_template("login.html")

# Logout Route
@app.route("/logout")
def logout():
    if 'user' in session:
        session.pop('user', None)  # Clear user session
        flash("You have been logged out.", "info")
    else:
        flash("You are not logged in!", "warning")
    return redirect(url_for('login'))

# Run the Flask App
if __name__ == '__main__':
    app.run(debug=True)