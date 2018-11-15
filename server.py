from flask import Flask, jsonify, request
from main import user
from datetime import datetime
app = Flask(__name__)


@app.route("/api/new_patient", methods=["POST"])
def new_patient():
    """
    Post patient's id, email, and age
    """
    r = request.get_json()
    user(r["patient_id"], r["attending_email"], r["user_age"])
    answer = {"Information": "User update successfully"}
    return jsonify(answer), 200


@app.route("/api/heart_rate",methods=["POST"])
def heart_rate():
    """
	post the new information about the heart rate measurement
	and time
	"""
    r = request.get_json()
    if user.patient_id is r["patient_id"]: # somehow check your user ID
        user.add_heart_rate(r["heart_rate"])
        temp = str(datetime.now())
        user.add_time(temp)
        answer = {"Information": "User update successfully"}
        return jsonify(answer), 200
    else:
        answer = {"Warning": "This user is not existing"}
        return jsonify(answer), 400


@app.route("/api/status/<patient_id>", methods=["GET"])
def status(patient_id):
	"""
	return average for all measurements
	"""
    # somehow check the user id
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