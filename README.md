#  Smart Farming with Crop Recommendation using IoT and Machine Learning

This project is a web-based smart farming system that recommends suitable crops based on real-time environmental parameters using a **Random Forest Classifier**. The solution combines **IoT-based sensor inputs** and **Machine Learning** to provide intelligent crop suggestions, aiming to assist farmers in making data-driven agricultural decisions.

---

## 📌 Objective

To design and deploy a smart farming solution that:
- Uses real-time sensor data (soil moisture, light intensity, temperature, humidity)
- Predicts the most suitable crop using a trained ML model
- Provides recommendations through a simple and accessible web interface

---

## 🧠 Machine Learning Model

- **Model Used**: Random Forest Classifier
- **Framework**: scikit-learn
- **Saved as**: `model.pkl` using `joblib`
- **Input Features**:
  - Soil Moisture
  - Light Intensity (LDR)
  - Temperature
  - Humidity
- **Output**: Predicted crop label (e.g., Rice, Wheat, Cotton, etc.)

---

## 💡 How It Works

1. **User Input**: User enters sensor values into a form on the home page.
2. **Backend Processing**:
   - The input values are formatted into a NumPy array.
   - The trained `RandomForestClassifier` model predicts the best crop.
3. **Output**: The recommended crop is shown on a result page.

---

## 🛠️ Tech Stack

| Layer        | Technologies Used                   |
|--------------|-------------------------------------|
| Frontend     | HTML, CSS, Jinja (Flask templates)  |
| Backend      | Python, Flask                       |
| ML Model     | scikit-learn (Random Forest Classifier) |
| Data Handling| NumPy, Joblib                       |

---

## 📁 Project Structure

Smart-Farming-with-Crop-Recommendation-Using-IOT-and-ML/
│
├── app.py # Flask app handling routes and prediction logic
├── model.pkl # Trained RandomForestClassifier model
├── templates/
│ ├── index.html # Input form page
│ └── result.html # Prediction output page
├── static/ # (Optional) For CSS or JS files if added
└── README.md # Documentation


---

## 🖥️ How to Run Locally

1. **Clone the Repository**
```bash
git clone https://github.com/abhinandan976/Smart-Farming-with-Crop-Recommendation-Using-IOT-and-ML.git
cd Smart-Farming-with-Crop-Recommendation-Using-IOT-and-ML

## Install Dependencies
pip install flask numpy joblib scikit-learn

## Run the application
python app.py


