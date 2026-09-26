import joblib
import numpy as np
import pandas as pd
import json

from flask import Flask
from flask import request
from flask import jsonify

model_file = "./model.bin"
dv_file = "./dv.bin"
scaler_file = "./scaler.bin"

dv = joblib.load(dv_file)
scaler = joblib.load(scaler_file)
model = joblib.load(model_file)
    
app = Flask('Diabetes_Prediction')

@app.route('/predict', methods = ['POST'])
def predict():
    client = request.get_json()

    client = pd.DataFrame([client])  
    
    # Columns to scale
    columns_to_scale = ['AGE', 'Urea', 'Cr', 'HbA1c', 'Chol', 'TG', 'HDL', 'LDL', 'VLDL', 'BMI']

    client[columns_to_scale] = scaler.transform(client[columns_to_scale])

    dict_client = client.to_dict(orient='records')
    
    X = dv.transform(dict_client)    
    
    y_pred = model.predict(X)

    print(y_pred)

    result = {
        'Predicted diabetic Status': int(y_pred[0])
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(
    host="0.0.0.0",
    port=9690,
    debug=True)