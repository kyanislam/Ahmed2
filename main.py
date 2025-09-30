from kivy.lang import Builder
from kivymd.app import MDApp

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        
        return Builder.load_file("test.kv")

    def log(self):
        self.root.ids.wl.text = f'Welcome {self.root.ids.usr.text}'

    def clean(self):
        self.root.ids.wl.text = "Welcome"
        self.root.ids.usr.text = " "
        self.root.ids.passwd.text = ""

     
 
MainApp().run()