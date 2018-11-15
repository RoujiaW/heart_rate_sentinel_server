class user():
    """
    """

    def __init__(self, patient_id, email, age, heart_rate, time):
        self.patient_id = patient_id
        self.email = None
        self.age = None
        self.heart_rate = [None]
        self.time = [None]
        self.add_heart_rate()

    def as_dict(self):
        return {
             "patient_id": self.patient_id,
             "attending_email": self.email,
             "user_age": self.age,
             "heart_rate": self.heart_rate,
             "heart_rate_average_since": self.time
         }

    def add_heart_rate(self, heart_rate):
        if type(heart_rate) is int:
            self.heart_rate.append(heart_rate)

    def add_time(self, time):
        self.heart_rate.append(time)
