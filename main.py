from random import choice
from kivy.app import App
from kivy.uix.button import Button, Label
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import get_color_from_hex


Window.clearcolor = (1, 0, 0, 1)

class Name(App):
    def build(self):
        self.h = 0
        
        layout = BoxLayout(orientation="horizontal")
        
        self.b1 = Button(
            text="التالي",
            size_hint=(None, None),
            size=(200, 70),
            on_press=self.ching,
            font_size=40
        )
        
        self.List_of_dhikr = [
            "سبحان الله",
            "الحمد لله",
            "لا إله إلا الله",
            "الله أكبر",
            "لا حول ولا قوة إلا بالله"
        ]
        
        self.L1 = Label(
            text=self.List_of_dhikr[self.h],
            font_size=42
        )
        self.L1.bind(size=self.L1.setter('text_size'))
        
        layout.add_widget(self.b1)
        layout.add_widget(self.L1)
        
        return layout

    def ching(self, yes):
        # تغيير الخلفية
        list_color = ["#eb0e0e","#ff6803","#c4ff03","#0b03ff","#d30fff","#b5b5b5","#66ff8cff","#ffdf7fff"]
        ching_color = choice(list_color)
        Window.clearcolor = get_color_from_hex(ching_color)
        
        # تحديث النص
        self.h = (self.h + 1) % len(self.List_of_dhikr)
        self.L1.text = self.List_of_dhikr[self.h]


if __name__ == "__main__":
    print("🚀 التطبيق بدأ يشتغل")
    Name().run()
