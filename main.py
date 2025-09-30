import arabic_reshaper
from bidi.algorithm import get_display

from random import choice
from kivy.app import App
from kivy.uix.button import Button, Label
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import get_color_from_hex


Window.clearcolor = (1, 0, 0, 1)

class main(App):
    def build(self):
        self.h = 0  # تعريف h كمتغير خاص بالكائن
        
        layout = BoxLayout(orientation="horizontal")
        tex2 = arabic_reshaper.reshape("التالي")
        tex3 = get_display(tex2)
        
        self.b1 = Button(
            text=tex3,
            font_name="arial-1.ttf",
            size_hint=(None, None),
            size=(200, 70),
            on_press=self.ching,
            pos_hint={'x': 0.4, 'y': 0.01},
            font_size=40,
            halign="center",
            valign="center"
            
        )
        
        self.List_of_dhikr = [
            "             سبحان الله",
            "              الحمد لله",
            "                لا إله إلا الله",
            "               الله أكبر",
            "                 لا حول ولا قوة إلا بالله"
        ]
        
        tex = arabic_reshaper.reshape(self.List_of_dhikr[self.h])
        tex2 = get_display(tex)
        
        self.L1 = Label(
            text=tex2,
            font_name="arial-1.ttf",
            font_size=42,
            pos_hint={'x':0.5, 'y': 0.05},
            halign="center",
            valign="center"
            
            
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
        self.h = (self.h + 1) % len(self.List_of_dhikr)  # التنقل بين الأذكار
        tex = arabic_reshaper.reshape(self.List_of_dhikr[self.h])
        tex2 = get_display(tex)
        self.L1.text = tex2


if __name__ == "__main__":
    main().run()
