from flask import Flask, jsonify, request
from disease import disease
from database import User
import datetime
app = Flask(__name__)


def add_heart_rate(patient_id, heart_rate, time):
    user = User.objects.raw({"patient_id": patient_id}).first() # Get the first user where _id=email
    user.heart_rate.append(heart_rate) # Append the heart_rate to the user's list of heart rates
    user.heart_rate_times.append(time) # append the current time to the user's list of heart rate times
    user.save() # save the user to the database


@app.route("/api/new_patient", methods=["POST"])
def new_patient():
    """
    Post patient's id, email, and age
    """
    r = request.get_json()
    user = User(r["patient_id"], r["attending_email"], r["user_age"])
    user.save()
    # return jsonify(answer), 200


@app.route("/api/heart_rate",methods=["POST"])
def heart_rate():
    """
	post the new information about the heart rate measurement
	and time
	"""
    r = request.get_json()
    user = User.objects.raw({"user_id": r["patient_id"]}).first()
    user.heart_rate.append(r["heart_rate"])
    user.times.append(datetime.datetime.now())
    # return jsonify(answer), 200


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


@app.route("/api/heart_rate/average/<patient_id>",methods=["GET"])
def average(patient_id):
    """
	return average for all measurements
	"""
# somehow grab the user and take the information from database
    average_heart_rate = sum(user.heart_rate)/len(user.heart_rate)
    result = disease(user.age, average_heart_rate)
    if result:
		message = "Warning: the patient has Tachycardia"
	else:
		message = "Normal health condition"
	answer = {
		"average": average_heart_rate,
		"health condition": message
	}
	return jsonify(answer),200

