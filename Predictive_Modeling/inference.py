import requests
import json

# Define the payload
payload = {
    "inputs": [
        {
            "tenure": 24,
            "MonthlyCharges": 65.5,
            "TotalCharges": 1500.0,
            "Contract_One year": 1,
            "Contract_Two year": 0,
            "InternetService_Fiber optic": 1,
            "InternetService_No": 0,
            "PaymentMethod_Credit card (automatic)": 0,
            "PaymentMethod_Electronic check": 1,
            "PaymentMethod_Mailed check": 0
        }
    ]
}

# Send the request
url = "http://127.0.0.1:1234/invocations"
headers = {"Content-Type": "application/json"}
response = requests.post(url, data=json.dumps(payload), headers=headers)

# Print the response
print(response.json())