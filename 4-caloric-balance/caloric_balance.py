class CaloricBalance:
    def __init__(self, gender, age, height, weight):
        self.gender = gender
        self.age = age
        self.height = height
        self.weight = weight
        self.balance = 0 - self.getBMR(gender, age, height, weight)

    def getBMR(self, gender, age, height, weight):
        if gender == 'm':
            return 66 + (12.7 * height) + (6.23 * weight) - (6.8 * age)
        elif gender == 'f':
            return 655 + (4.7 * height) + (4.35 * weight) - (4.7 * age)
        else:
            return 0.0

    def getBalance(self):
        return self.balance

    def recordActivity(self, caloric_burn_per_pound_per_minute, minutes):
        self.balance -= ((caloric_burn_per_pound_per_minute * self.weight) * minutes)

    def eatFood(self, calories):
        self.balance += calories
