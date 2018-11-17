# heart_rate_sentinel_server
This package includes a heart rate sentinel server that currently is running on the duke virtual machine. It contains a database that allow physicians to store user heart rate information. The server can receive POST requests from mock patient heart rate monitors. If a patient has a tachycardic heart rate, the user will be informed by the server. 
To access the server: 
1. First click on the link for Hello page: http://vcm-7305.vm.duke.edu:5000/hello to make sure the server is working 
2. An example client python code is included in the package. Simply type the following command in your terminal or command line
```
python main.py
```
3. To store a new user
```
r = requests.post("http://vcm-7305.vm.duke.edu:5000/api/new_patient", json={"patient_id": "1","attending_email": "test@example.com", "user_age": "50"})
print(r.json())
```
4. To update heart information using patient id, for example: 1
```
r = requests.post("http://vcm-7305.vm.duke.edu:5000/api/heart_rate",
                  json={"patient_id": "1", "heart_rate": 100})
print(r.json())
```
5. To find out patient's tachycardic condition based on the previously available heart rate and the timestamp of the most recent heart rate, for example: 1
```
r = requests.get("http://vcm-7305.vm.duke.edu:5000/api/status/1")
print(r.json())
```
6. To find out patient's all previous heart rates using patient id, for example: 1
```
r = requests.get("http://vcm-7305.vm.duke.edu:5000/api/heart_rate/1")
print(r.json())
```
7. To find out patient's overall average heart rate using patient id, for example: 1
```
r = requests.get("http://vcm-7305.vm.duke.edu:5000/api/heart_rate/average/1")
print(r.json())
```
8. To find out patient's user defined time interval average heart rate using patient id, for example: 1
```
r = requests.post(
    "http://vcm-7305.vm.duke.edu:5000/api/heart_rate/interval_average",
    json={"patient_id": "1", "heart_rate_average_since":
          "2018-12-09 11:00:36.372339"})
print(r.json())
```

Feature need improvements in the future is: if a new heart rate is received for a patient that is tachycardic, the email should be sent out at that time.
