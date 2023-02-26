
import kivy
from tkinter import Widget
from tracker import Tracker
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.app import App



f = open('userinfo.txt', 'r')
lines = f.readlines()
print(lines)
for i in range(len(lines)):
    data = lines[i]
    temp = str(data)
    temp = temp.replace("\n", "")
    lines[i] = temp
height = lines[3]
height = height.replace("\\", '')
weight = lines[2]
age = lines[0]
sex = lines[1]
calories = lines[4]

class Mylayout(GridLayout):
    def __init__(self, **kwargs):
        super(Mylayout, self).__init__()
        self.cols = 2

        self.add_widget(Label(text="Your Calories left to eat"))
        self.calsleft = TextInput(multiline = False)
        self.add_widget(self.calsleft)

        self.add_widget(Label(text="Enter Calories youve had in a meal"))
        self.intake = TextInput(multiline = False)
        self.add_widget(self.intake)

        self.enter = Button(text="Enter", font_size=40)
        self.enter.bind(on_press=self.pressed)
        self.add_widget(self.enter)

    def pressed(self, instance):
        calintake = self.intake.text
        calint = int(calories)
        calremainder = calint - int(calintake)

        self.calsleft.text = str(calremainder)



class baymer(App):
    def build(self):
        return Mylayout()

if __name__ == '__main__':
    baymer().run()











    

