from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
try:
    model = joblib.load('model.pkl')
except Exception as e:
    raise ValueError(f"Failed to load the model: {e}")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Retrieve input values from the form
            soil_moisture = float(request.form['soil_moisture'])
            ldr = float(request.form['ldr'])
            temperature = float(request.form['temperature'])
            humidity = float(request.form['humidity'])

            # Prepare input data for prediction
            input_data = np.array([[soil_moisture, ldr, temperature, humidity]])

            # Make a prediction
            predicted_label = model.predict(input_data)[0]

            return render_template('result.html', prediction=predicted_label)

        except Exception as e:
            return f"Error during prediction: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
