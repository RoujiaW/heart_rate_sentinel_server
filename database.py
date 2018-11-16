from pymodm import connect
from pymodm import MongoModel, fields


connect("mongodb://roujiw:wrj1995@ds163683.mlab.com:63683/bme590")


class User(MongoModel):
    user_id = fields.CharField(primary_key=True)
    email = fields.EmailField()
    age = fields.IntegerField()
    heart_rate = fields.ListField(field=fields.IntegerField())
    times = fields.ListField(field=fields.DateTimeField())
    health = fields.CharField()
