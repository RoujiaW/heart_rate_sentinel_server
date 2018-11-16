import requests


r = requests.post("http://127.0.0.1:5000/api/new_patient", json={"patient_id": "1",
                                                                 "attending_email": "roujiw@uw.eduu",
                                                                 "user_age": "50"})
print(r.json())
r = requests.post("http://127.0.0.1:5000/api/heart_rate", json={"patient_id": "1", "heart_rate": 100})
print(r.json())
r = requests.get("http://127.0.0.1:5000/api/status/1")
print(r.json())
r = requests.get("http://127.0.0.1:5000/api/heart_rate/1")
print(r.json())
r = requests.get("http://127.0.0.1:5000/api/heart_rate/average/1")
print(r.json())
r = requests.post("http://127.0.0.1:5000/api/heart_rate/interval_average",
                  json={"patient_id": "1",
                        "heart_rate_average_since": "2018-03-09 11:00:36.372339"})
print(r.json())

