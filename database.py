from pymodm import connect
from pymodm import MongoModel, fields


connect("mongodb://vcm-7305.vm.duke.edu/heart_rate_server")


class User(MongoModel):
    user_id = fields.CharField(primary_key=True)
    email = fields.EmailField()
    age = fields.IntegerField()
    heart_rate = fields.ListField(field=fields.IntegerField())
    times = fields.ListField(field=fields.DateTimeField())



"""
u = User('user1@email.com', last_name='Ross', first_name='Bob')
u2 = User('user2@email.com', last_name='Ross', first_name='Rob')

u.save()
u2.save()

for user in User.objects.raw({"first_name":"Rob"}):
    print(user)
	print(user.first_name)
	print(user.last_name)
"""