import requests


r = requests.post("http://vcm-7305.vm.duke.edu:5000/api/new_patient",
                   json={"patient_id": "1",
                         "attending_email": "roujiw@uw.edu",
                         "user_age": "50"})
print(r.json())
r = requests.post("http://vcm-7305.vm.duke.edu:5000/api/heart_rate",
                  json={"patient_id": "1", "heart_rate": 100})
print(r.json())
r = requests.post("http://vcm-7305.vm.duke.edu:5000/api/heart_rate",
                  json={"patient_id": "1", "heart_rate": 130})
print(r.json())
r = requests.post("http://vcm-7305.vm.duke.edu:5000/api/heart_rate",
                  json={"patient_id": "1", "heart_rate": 80})
print(r.json())
r = requests.get("http://vcm-7305.vm.duke.edu:5000/api/status/1")
print(r.json())
r = requests.get("http://vcm-7305.vm.duke.edu:5000/api/heart_rate/1")
print(r.json())
r = requests.get("http://vcm-7305.vm.duke.edu:5000/api/heart_rate/average/1")
print(r.json())
r = requests.post("http://vcm-7305.vm.duke.edu:5000/api/heart_rate/interval_average",
                  json={"patient_id": "1",
                        "heart_rate_average_since":
                            "2018-12-09 11:00:36.372339"})
print(r.json())
