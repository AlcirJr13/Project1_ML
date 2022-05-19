"""
Creator: Ivanovitch Silva
Date: 26 April. 2022
Script that POSTS to the API using the requests 
module and returns both the result of 
model inference and the status code
"""
import requests
import json
# import pprint

person = {
        "customerID" : 0000AAAAAA,
        "gender"  : Male,
        "SeniorCitizen" :  0,
        "Partner" : Yes,
        "Dependents" : No,
        "tenure" : 10,
        "PhoneService" :  Yes,
        "MultipleLines" : No,
        "InternetService" : DSL,
        "OnlineSecurity" : No,
        "OnlineBackup" : No,
        "DeviceProtection" : No,
        "TechSupport" : No,
        "StreamingTV" : No,
        "StreamingMovies" : No,
        "Contract" : One year,
        "PaperlessBilling" : Yes,
        "PaymentMethod" :  Mailed check,
        "MonthlyCharges" : 29.30,
        "TotalCharges" : 29.30,
        "Churn" : No
    }

url = "http://127.0.0.1:8000"
#url = "https://teste-am.herokuapp.com"
response = requests.post(f"{url}/predict",
                         json=person)

print(f"Request: {url}/predict")
print(f"Person: \n age: {person['age']}\n workclass: {person['workclass']}\n"\
      f" fnlwgt: {person['age']}\n education: {person['education']}\n"\
      f" education_num: {person['education_num']}\n"\
      f" marital_status: {person['marital_status']}\n"\
      f" occupation: {person['occupation']}\n"\
      f" relationship: {person['relationship']}\n"\
      f" race: {person['race']}\n"\
      f" sex: {person['sex']}\n"\
      f" capital_gain: {person['capital_gain']}\n"\
      f" capital_loss: {person['capital_loss']}\n"\
      f" hours_per_week: {person['hours_per_week']}\n"\
      f" native_country: {person['native_country']}\n"
     )
print(f"Result of model inference: {response.json()}")
print(f"Status code: {response.status_code}")