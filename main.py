from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy_garden.arabictext import ArabicLabel
from kivy.uix.button import Button
from random import choice
from kivy.core.window import Window
from kivy.utils import get_color_from_hex


class AzkarApp(App):
    def build(self):
        self.h = 0
        self.azkar = [
            "سبحان الله",
            "الحمد لله",
            "لا إله إلا الله",
            "الله أكبر",
            "لا حول ولا قوة إلا بالله"
        ]

        layout = BoxLayout(orientation="vertical", padding=20, spacing=20)

        self.label = ArabicLabel(
            text=self.azkar[self.h],
            font_name="arial-1.ttf",
            font_size=48,
            halign="center",
            valign="middle"
        )

        btn = Button(
            text="التالي",
            font_name="arial-1.ttf",
            font_size=32,
            size_hint=(None, None),
            size=(200, 80),
            pos_hint={"center_x": .5}
        )
        btn.bind(on_press=self.next_zekr)

        layout.add_widget(self.label)
        layout.add_widget(btn)

        return layout

    def next_zekr(self, instance):
        # تغيير اللون العشوائي للخلفية
        colors = ["#eb0e0e","#ff6803","#c4ff03","#0b03ff","#d30fff","#b5b5b5","#66ff8c","#ffdf7f"]
        Window.clearcolor = get_color_from_hex(choice(colors))

        # تحديث النص
        self.h = (self.h + 1) % len(self.azkar)
        self.label.text = self.azkar[self.h]


if __name__ == "__main__":
    AzkarApp().run()
