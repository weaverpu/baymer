import kivy
from tkinter import Widget
from tracker import Tracker
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.app import App
import os
import time


a = Tracker()

class Mylayout(GridLayout):
    def __init__(self, **kwargs):
        super(Mylayout, self).__init__()
        self.cols = 2

        self.add_widget(Label(text="Age"))
        self.age = TextInput(multiline = False)
        self.add_widget(self.age)

        self.add_widget(Label(text="sex"))
        self.sex = TextInput(multiline = False)
        self.add_widget(self.sex)


        self.add_widget(Label(text="weight"))
        self.weight = TextInput(multiline = False)
        self.add_widget(self.weight)
        
        self.add_widget(Label(text="height"))
        self.height1 = TextInput(multiline = False)
        self.add_widget(self.height1)

        self.add_widget(Label(text="Enter a fitness goal- choose from gain, main, or loose"))
        self.fitness = TextInput(multiline = False)
        self.add_widget(self.fitness)

        self.submit = Button(text="Submit", font_size = 32)
        self.submit.bind(on_press=self.submission)
        self.add_widget(self.submit)

    def submission(self, instance):
        age = self.age.text
        sex = self.sex.text
        weight = self.weight.text
        height = self.height1.text
        a.getsex(sex)
        a.getage(age)
        a.getheight(height)
        a.getweight(weight)
        a.getcalorieintake(self.fitness.text)
        calories = a.ReturnCalories()

        userinfofile = "touch userinfo.txt"
        os.system(userinfofile)
        f = open('userinfo.txt', 'w')
        f.write(age + "\n")
        f.write(sex + "\n")
        f.write(weight + "\n")
        f.write(height + "\n")
        f.write(str(calories))
        f.close 


class baymer(App):
    def build(self):
        return Mylayout()


if __name__ == '__main__':
    baymer().run()

