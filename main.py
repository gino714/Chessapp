from kivy.app import App
from kivy.uix.label import Label

class ChessApp(App):
    def build(self):
        return Label(text="Hello ChessApp!")

if __name__ == "__main__":
    ChessApp().run()
