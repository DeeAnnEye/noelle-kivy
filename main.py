from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation
from kivy.clock import Clock

class MainUI(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.start_pulse)

    def start_pulse(self, *args):
        mic_button = self.ids.mic_button
        self.animate_pulse(mic_button)

    def animate_pulse(self, widget):
        pulse_out = Animation(size=(90, 90), duration=0.4)
        pulse_in = Animation(size=(80, 80), duration=0.4)
        pulse_out += pulse_in
        pulse_out.repeat = True
        pulse_out.start(widget)

class NoelleApp(App):
    def build(self):
        return MainUI()

    def on_mic_pressed(self):
        print("Mic button pressed!")


NoelleApp().run()
