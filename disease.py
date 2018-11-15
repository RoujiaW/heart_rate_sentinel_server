def disease(age, heart_rate):
    if type(age) is int and type(heart_rate) is int:
        if age >= 1 and age < 3 and heart_rate > 151:
            result = True
        elif age >= 3 and age < 5 and heart_rate > 137:
            result = True
        elif age >= 5 and age < 8 and heart_rate > 133:
            result = True
        elif age >= 8 and age < 12 and heart_rate > 130:
            result = True
        elif age >= 12 and age < 15 and heart_rate > 119:
            result = True
        elif age >= 15 and heart_rate > 100:
            result = True
        else:
            result = False
        return result
    else:
        raise TypeError("Wrong type of input")
