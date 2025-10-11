from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from plyer import audio
from kivy.core.audio import SoundLoader

KV = '''
BoxLayout:
    orientation: 'vertical'
    padding: 20
    spacing: 15

    Label:
        id: status
        text: 'Press "Start Recording" to record your voice'
        font_size: '18sp'
        halign: 'center'

    Button:
        text: '🎙️ Start Recording'
        font_size: '20sp'
        on_press: app.start_recording()

    Button:
        text: '⏹️ Stop Recording'
        font_size: '20sp'
        on_press: app.stop_recording()

    Button:
        text: '▶️ Play Recording'
        font_size: '20sp'
        on_press: app.play_recording()
'''

class AudioApp(App):
    def build(self):
        return Builder.load_string(KV)

    def start_recording(self):
        self.output_file = '/sdcard/my_record.wav'  # file path (Android)
        self.root.ids.status.text = 'Recording... 🔴'
        try:
            audio.start(path=self.output_file)
        except Exception as e:
            self.root.ids.status.text = f'Error: {e}'

    def stop_recording(self):
        try:
            audio.stop()
            self.root.ids.status.text = f'Saved recording to {self.output_file}'
        except Exception as e:
            self.root.ids.status.text = f'Error: {e}'

    def play_recording(self):
        try:
            sound = SoundLoader.load(self.output_file)
            if sound:
                sound.play()
                self.root.ids.status.text = 'Playing recording ▶️'
            else:
                self.root.ids.status.text = 'File not found ❌'
        except Exception as e:
            self.root.ids.status.text = f'Error while playing: {e}'


if __name__ == '__main__':
    AudioApp().run()
