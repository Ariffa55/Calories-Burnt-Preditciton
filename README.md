🔥 Calories Burnt Prediction using Machine Learning

This project focuses on predicting the number of calories burnt during exercise using various personal and activity-related features. The goal is to build a machine learning model that helps users understand how different factors affect their calorie expenditure, enabling more effective fitness planning.

📌 Project Overview
In this project, we used a regression model to predict the number of calories burned based on features such as:

💡 Features
🧠 Calories Burnt Prediction using ML model

⚖ BMI Calculator
🔥 BMR & TDEE Estimation
🔐 Login Page for user interaction
🧾 Clean UI with HTML/CSS
✅ Data handled via pandas, model stored via joblib/pickle

🗂 Project Structure:

Calories-Burnt-Prediction/
│
├── static/
│   ├── styles.css          # Styling for HTML pages
│   └── script.js           # Optional JS (if used)
│
├── templates/
│   ├── index.html          # Home page
│   ├── login.html          # Login form
│   ├── bmi.html            # BMI calculator
│   ├── bmr_tdee.html       # BMR & TDEE calculator
│   ├── calories.html       # Calories burnt prediction form
│   └── temp                # (Possibly unused or temp page)
│
├── calories.csv            # Raw data
├── exercise.csv            # Supporting dataset
├── caloriesburnt.ipynb     # ML model training notebook
├── app.py                  # Flask app file
├── README.md               # Project documentation

📊 Dataset
The dataset consists of individual records with personal attributes and activity stats. It includes:

Gender: Male / Female
Age: Age of the person
Height: in centimeters
Weight: in kilograms
Duration: Time of physical activity in minutes
Heart Rate: Average during activity
Body Temperature: In degrees Celsius
Calories: Target variable (actual calories burnt)

The dataset was cleaned and preprocessed for missing values and feature scaling before model training.

👩‍💻ML Models Used:
We experimented with several regression algorithms:

1.Linear Regression
2.Random Forest Regressor
3.XGBoost Regressor
4.Support Vector Regressor (SVR)

🧠 Machine Learning Workflow:

1.Data Preprocessing
   -Cleaned and encoded data
   -Scaled numerical features

2.Model Training
   -Models tested: Linear Regression, Random Forest, XGBoost
   -Best model selected based on accuracy and RMSE

3.Model Deployment
   -Trained model saved using joblib or pickle
   -Flask used to build a web interface for predictions
   
The best model was selected based on evaluation metrics such as R² Score, MAE, and RMSE.

📈 Visualizations:
We used Matplotlib and Seaborn to generate insights from the data including:

Correlation heatmap
Distribution of calories burned
Feature importance chart
Scatter plots of weight, duration vs calories


⚙ Technologies Used

Python
Pandas & NumPy
Scikit-learn
Matplotlib & Seaborn
Jupyter Notebook

🚀 How to Run
1.Clone the repository:
git clone https://github.com/Ariffa55/Calories-Burnt-Predictiton.git
cd Calories-Burnt-Predictiton

2.Install dependencies:
pip install -r requirements.txt

3.Run the Flask application:
python app.py

4.Open browser and go to:
http://127.0.0.1:5000

📈 Model Training:

-Done in caloriesburnt.ipynb
-Algorithms tested: Linear Regression, Random Forest, XGBoost
-Final model saved using joblib and loaded into Flask app.

🧪 Model Evaluation:

Model	              R² Score	  MAE	      RMSE
Linear Regression	   0.82	      18.3	      24.1
Random Forest	       0.94	      9.2	      12.6
XGBoost	               0.95	      8.5	      11.3
SVR	                   0.88	      14.1	      18.2

📌 XGBoost Regressor performed the best with the highest R² score and lowest error.

📍 Conclusion
This project demonstrates how machine learning can be effectively used in health and fitness domains. Predicting calories burned using user-specific data can lead to better personalized workout plans and motivate users toward healthier living.

💡 Future Improvements:

Add user registration system
Store previous records using SQLite
Host on Render / Railway / Heroku
Make mobile responsive UI
Integrate with wearable fitness trackers
Expand dataset with more diverse activity types.
