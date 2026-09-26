import requests
#ID	No_Pation	Gender	AGE	Urea	Cr	HbA1c	Chol	TG	HDL	LDL	VLDL	BMI	CLASS
#0	502	17975	F	50.0	4.7	46.0	4.9	4.2	0.9	2.4	1.4	0.5	24.0	N

url = 'http://localhost:9690/predict'

client = {"Gender": "F",
         "AGE": 50.0,
         "Urea": 4.7,
         "Cr": 46.0,
         "HbA1c": 4.9,
         "Chol": 4.2,
         "TG": 0.9,
         "HDL": 2.4,
         "LDL": 1.4,
         "VLDL": 0.5,
         "BMI": 24.0
        }

response = requests.post(url, json=client).json()

predictions = {
    0: "Patient not diabetic",
    1: "Patient diabetic",
    2: "Patient probable diabetic"
}

pred = predictions.get(response["Predicted diabetic Status"], "Unknown")

print(f"Prediction: {pred}")