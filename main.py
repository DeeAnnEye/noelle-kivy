from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MainApp(BoxLayout):
    pass

class NoelleApp(App):
    def self():
        return MainApp()
