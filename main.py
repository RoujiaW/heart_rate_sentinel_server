class user():
    """
    """

    def __init__(self, patient_id, email, age, heart_rate, time):
        self.patient_id = patient_id
        self.email = None
        self.age = None
        self.heart_rate = None
        self.time = None

    def as_dict(self):
        return {
             "patient_id": self.patient_id,
             "attending_email": self.email,
             "user_age": self.age,
             "heart_rate": self.heart_rate,
             "heart_rate_average_since": self.time
         }
