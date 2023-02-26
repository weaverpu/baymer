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
        self.currentwater = 0
        self.waterintake = 0

    #getting the username of the user
    def getusername(self) -> None:
        self.username = input("Enter Baymer username: ")

    #getting the age of the user
    def getage(self) -> None:
        self.age = input("Enter your age in years: ")

    #get the sex of the user
    def getsex(self) -> None:
        self.sex = input("What is your sex? ")

    #getting height of the user and converting it into inches
    def getheight(self) -> None:
        flag1 = True
        while flag1:
            try:
                feet, inches = input("Enter your height: ").split("'")
                if True:
                    inches = inches.replace('"',"")
                    feet = feet.replace('"',"")
                    inches = int(inches)
                    feet = int(feet)
                    if inches > 11.99:
                        print("Inches must be less than 12. Please try again: ")
                    else:
                        flag1 = False
            except ValueError:
                print("Please enter in _'_",'"'," format.")
        feet = int(feet) * 12
        self.height = feet + inches

    #getting the weight of the user
    def getweight(self) -> None:
        self.weight = input("Enter your weight in lbs: ")
        self.weight = int(self.weight)

    #get the budget that the user would like to use weekly or monthly
    def getbudget(self) -> None:
        Flag1 = True
        while Flag1:
            time = input("Would you like to budget weekly or monthly? ")
            time = time.strip()
            time = time.lower()
            if time == "weekly" or time == "monthly":
                Flag1 = False
            else:
                print("Please choose whether you would like to budget weekly or monthly.")
        if time == "weekly":
            self.budget = (float(input("Please enter how much you would like to spend weekly: $")))
            self.budget = int(self.budget)
        elif time == "monthly":
            self.budget = (float(input("Please enter how much you would like to spend monthly: $")))
            self.budget = int(self.budget)

    #get the BMI of the user using height and weight
    def getbmi(self) -> None:
        self.getheight()
        self.getweight()
        self.height *= .0254
        self.weight *= .454
        self.bmi = float('%.1f' % (self.weight / (self.height ** 2)))

    #get the goal caloric intake of the user
    def getcalorieintake(self) -> None:
        self.getweight()
        Flag1 = True
        while Flag1:
            getgoal = input("Are you trying to gain, maintain, or lose weight? ")
            getgoal = getgoal.strip()
            getgoal = getgoal.lower()
            if getgoal == "gain" or getgoal == "maintain" or getgoal == "lose":
                Flag1 = False
            else:
                print("Please only type in 'gain', 'maintain', or 'lose.")
        if getgoal == "gain":
            self.calorieintake = self.weight * 18
            self.calorieintake = int(self.calorieintake)
        elif getgoal == "maintain":
            self.calorieintake = self.weight * 15
            self.calorieintake = int(self.calorieintake)
        elif getgoal == "lose":
            self.calorieintake = self.weight * 13
            self.calorieintake = int(self.calorieintake)
        self.currentcalories = self.calorieintake

    #subtract consumed calories from starting calories
    def consumecalories(self, intake: int):
        self.getcalorieintake()
        self.currentcalories = self.currentcalories - intake
    
    #reseting calorie intake back to full daily amount
    def resetcalories(self):
        self.currentcalories = self.calorieintake

    #getting how much water the user should drink in a day
    def getwaterintake(self):
        self.getweight()
        self.waterintake = self.getweight() / 2
        self.currentwater = self.waterintake

    #getting water intake after water has been consumed
    def consumewater(self, intake: int):
        self.getwaterintake()
        self.currentwater -= intake

    #reseting water intake at the end of the day
    def resetwater(self):
        self.currentwater = self.waterintake
