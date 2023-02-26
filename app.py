'''
TabbedPanel
============

Test of the widget TabbedPanel.
'''

from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder

Builder.load_file("./baymer.kv")


class Mylayout(TabbedPanel):
    def press():
        
    pass


class baymer(App):
    def build(self):
        return Mylayout()


if __name__ == '__main__':
    baymer().run()

