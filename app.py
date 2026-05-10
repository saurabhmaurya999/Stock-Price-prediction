from flask import Flask, render_template, request
import pickle
import numpy as np

# Flask app
app = Flask(__name__)

# Load model
model = pickle.load(open('model.pkl', 'rb'))

# Home page
@app.route('/')
def home():
    return render_template('index.html')


# Prediction route
@app.route('/predict', methods=['POST'])
def predict():

    # Get values from form
    feature1 = float(request.form['open_close'])
    feature2 = float(request.form['high_low'])
    feature3 = float(request.form['is_quarter_end'])

    # Convert into numpy array
    features = np.array([[feature1, feature2, feature3]])

    # Prediction
    prediction = model.predict(features)

    if prediction[0] == 1:
        result = "Stock will go up"
    else:
        result = "Stock will go down"

    # Send result to HTML
    return render_template(
        'index.html',
        prediction_text=result
    )


# Run app
if __name__ == "__main__":
    app.run(debug=True)