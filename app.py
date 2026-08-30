import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import joblib

flask_app = Flask(__name__)
model = joblib.load('models/flight_delay_model.pkl')

@flask_app.route('/')
def home():
    return render_template('index.html')

@flask_app.route('/predict', methods=['POST'])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)
    return render_template('index.html', prediction_text='Delay of Flight is {:.2f} minutes'.format(prediction[0]))

if __name__ == "__main__":
    flask_app.run(debug=True)
