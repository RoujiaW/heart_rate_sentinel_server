from flask import Flask, jsonify, request
from main import user
import datetime
app = Flask(__name__)


@app.route("/api/new_patient", methods=["POST"])
def new_patient():
    """
    Post patient's id, email, and age
    """
    r = request.get_json()
    user.patient_id = r["patient_id"]
    user.email = r["attending_email"]
    user.age = r["user_age"]
    answer = {
        "patient_id": user.patient_id,
        "attending_email": user.email,
        "user_age": user.age,
    }
    return jsonify(answer), 200


@app.route("/api/heart_rate",methods=["POST"])
def heart_rate():
    """
	post the new information about the heart rate measurement
	and time
	"""
    r = request.get_json()
    if user.patient_id is r["patient_id"]:
        user.heart_rate = r["heart_rate"]
        user.time = datetime.datetime.now()
        answer = {
            "heart_rate_average_since": user.time,
            "patient_id": user.patient_id,
            "heart_rate": user.heart_rate,
		}
        return jsonify(answer), 200
    else:
        answer = {"Warning": "This user is not existing"}
        return jsonify(answer), 400

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