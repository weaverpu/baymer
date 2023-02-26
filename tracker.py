class Tracker:

    #defining all of my variables
    def __init__(self):
        self.username = ''
        self.age = 0
        self.height = 0
        self.weight = 0
        self.budget = 0
        self.bmi = 0
        self.sex = ''
        self.calorieintake = 0
        self.currentcalories = 0

    #getting the username of the user
    def getusername(self, username) -> None:
        self.username = username

    #getting the age of the user
    def getage(self, age) -> None:
        self.age = age

    #get the sex of the user
    def getsex(self, sex) -> None:
        self.sex = sex

    #getting height of the user and converting it into inches
    def getheight(self, height) -> None:
        feet, inches = height.split("'")
        inches = inches.replace('"',"")
        feet = feet.replace('"',"")
        inches = int(inches)
        feet = int(feet) * 12
        self.height = feet + inches

    #getting the weight of the user
    def getweight(self, weight) -> None:
        self.weight = int(weight)

    #get the budget that the user would like to use weekly or monthly
    def getbudget(self, budget) -> None:
            self.budget = budget

    #get the BMI of the user using height and weight
    def getbmi(self) -> None:
        self.getheight()
        self.getweight()
        self.height *= .0254
        self.weight *= .454
        self.bmi = float('%.1f' % (self.weight / (self.height ** 2)))

    #get the goal caloric intake of the user
    def getcalorieintake(self, goal) -> None:
        goal = goal.strip()
        goal = goal.lower()
        if goal == "gain":
            self.calorieintake = self.weight * 18
            self.calorieintake = int(self.calorieintake)
        elif goal == "maintain":
            self.calorieintake = self.weight * 15
            self.calorieintake = int(self.calorieintake)
        elif goal == "lose":
            self.calorieintake = self.weight * 13
            self.calorieintake = int(self.calorieintake)
        self.currentcalories = self.calorieintake

    #subtract consumed calories from starting calories
    def consumecalories(self, intake: int):
        self.currentcalories = self.currentcalories - intake
    
    def resetcalories(self):
        self.currentcalories = self.calorieintake

    def ReturnCalories(self):
        return self.currentcalories
a = Tracker()
a.consumecalories(10)
print(a.currentcalories)
    



