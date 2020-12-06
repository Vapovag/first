from kivy.app import App

kv = Builder.load_file("my.kv")

class VappovagApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    VappovagApp().run()
