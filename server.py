from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route("/api/new_patient", methods=["POST"])
def new_patient():
    """
      Returns the patient's id, email, and age
    """
    r = request.get_json()
    patient_id = r["patient_id"]
    email = r["attending_email"]
    age = r["user_age"]
    return patient_id, email, age


@app.route("/api/heart_rate", methods=["POST"])
def heart_rate():
    r = request.get_json()
    answer = {
        "patient_id": "1",
        "heart_rate": 100,
    }
    return jsonify(answer)


@app.route("/", methods=["GET"])
def hello():
    """
    Returns the string "Hello, world" to the caller
    """
    return "Hello, world"


@app.route("/api/status/<patient_id>", methods=["GET"])
def hello(patient_id):

    return "Hello, world"


@app.route("/data", methods=["GET"])
def getData():
    """
    Returns the data dictionary below to the caller as JSON
    """
    data = {
        "name": "Suyash",
        "team": "instructor"
    }
    return jsonify(data)


@app.route("/api/heart_rate/average/<user_email>",methods=["GET"])
def average(user_email):
    """
	return average for all measurements
	"""
    user = models.User.objects.raw({"_id": user_email}).first()
    aver = sum(user.heart_rate)/len(user.heart_rate)
    tah = ta(user.age, aver)
    if tah > 1:
		stm = "this person may have Tachycardia"
	else:
		stm = "this person's heart rate is normal"
	average = {
		"average": aver,
		"health condition": stm
	}
	return jsonify(average),200