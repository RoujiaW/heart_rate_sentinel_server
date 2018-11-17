from flask import Flask, jsonify, request
from pymodm import connect
from disease import disease
from database import User
from datetime import datetime
app = Flask(__name__)
connect("mongodb://roujiw:wrj1995@ds163683.mlab.com:63683/bme590")


@app.route("/hello")
def hello():
    """
    Welcome page
    """
    return "Hello, world"


@app.route("/api/new_patient", methods=["POST"])
def new_patient():
    """
    Post patient's id, email, and age
    :return jsonify file
    """
    r = request.get_json()
    user = User(r["patient_id"], r["attending_email"], r["user_age"])
    user.save()
    answer = {
        "Message": "User create successfully",
    }
    return jsonify(answer), 200


@app.route("/api/heart_rate", methods=["POST"])
def heart_rate():
    """
    post the new information about the heart rate measurement and time
    :return jsonify file
    """
    r = request.get_json()
    if isinstance(r["patient_id"], str) and isinstance(r["heart_rate"], int):
        user = User.objects.raw({"_id": r["patient_id"]}).first()
        user.heart_rate.append(r["heart_rate"])
        user.times.append(datetime.now())
        user.save()
    else:
        raise TypeError("Please enter patient_id and heart_rate as integers")
    # Test disease
    result = disease(user.age, r["heart_rate"])  # most recent heart rate
    if result:
        user.health = "Patient has Tachycardia"
    else:
        user.health = "Patient's heart rate is normal"
    answer = {
        "Message": "User heart rate update successfully",
    }
    user.save()
    print(answer)
    return jsonify(answer), 200


@app.route("/api/status/<patient_id>", methods=["GET"])
def status(patient_id):
    """
    Get patient health condition
    :return: jsonify file
    """
    user = User.objects.raw({"_id": patient_id}).first()
    answer = {
        "health condition": user.health,
        "Time": user.times[len(user.times) - 1],
    }
    return jsonify(answer), 200


@app.route("/api/heart_rate/<patient_id>", methods=["GET"])
def heart_rate2(patient_id):
    """
    :return: jsonify list of heart rate
    """
    user = User.objects.raw({"_id": patient_id}).first()
    result = {
        "heart_rate_list": user.heart_rate
    }
    return jsonify(result), 200


@app.route("/api/heart_rate/average/<patient_id>", methods=["GET"])
def average(patient_id):
    """
    :return: jsonify average for all heart rate data
    """
    user = User.objects.raw({"_id": patient_id}).first()
    average_heart_rate = sum(user.heart_rate)/len(user.heart_rate)
    answer = {
        "average": average_heart_rate,
    }
    return jsonify(answer), 200


@app.route("/api/heart_rate/interval_average", methods=["POST"])
def interval_average():
    """
    :return: interval_average based on user input
    """
    r = request.get_json()
    heart_rate_interval = []
    if isinstance((r["patient_id"]), str):
        user = User.objects.raw({"_id": r["patient_id"]}).first()
        input_time = datetime.strptime(r["heart_rate_average_since"],
                                       '%Y-%m-%d %H:%M:%S.%f')
        for i in user.times:
            if input_time >= i:
                index = user.times.index(i)
                heart_rate_interval.append(user.heart_rate[index])
    else:
        raise TypeError("Please enter patient_id and heart_rate as integers")
    if len(heart_rate_interval) > 0:
        ave = sum(heart_rate_interval) / len(heart_rate_interval)
        answer = {"Interval average": str(ave)}
    else:
        answer = {"Warning": "Input time is not existing"}
    return jsonify(answer)


if __name__ == "__main__":
    app.run(host="//0.0.0.0")
