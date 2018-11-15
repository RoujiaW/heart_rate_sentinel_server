from pymodm import connect
from pymodm import MongoModel, fields


connect("mongodb://vcm-7305.vm.duke.edu/heart_rate_server")


class User(MongoModel):
    user_id = fields.IntegerField(primary_key=True)
    email = fields.EmailField()
    age = fields.IntegerField()
    heart_rate = fields.ListField(field=fields.IntegerField())
    times = fields.ListField(field=fields.DateTimeField())
    health = fields.CharField()
