from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.progressbar import ProgressBar
from kivy.utils import platform
from kivy.clock import Clock
from kivy.core.audio import SoundLoader

# محاولة استيراد plyer للتسجيل الحقيقي
try:
    from plyer import audio
    PLYER_AVAILABLE = True
except Exception:
    PLYER_AVAILABLE = False

KV = '''
BoxLayout:
    orientation: 'vertical'
    padding: 20
    spacing: 15

    Label:
        id: status
        text: 'Press "Record" to start recording'
        font_size: '18sp'
        size_hint_y: None
        height: self.texture_size[1] + 20

    ProgressBar:
        id: progress
        max: 100
        value: 0
        size_hint: (1, None)
        height: 20
        opacity: 0  # مخفي افتراضيًا

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

class HybridRecorderApp(App):
    def build(self):
        return Builder.load_string(KV)

    def start_recording(self):
        progress = self.root.ids.progress
        progress.opacity = 1  # إظهار الشريط
        progress.value = 0

        if platform == "android" and PLYER_AVAILABLE:
            try:
                self.output_file = '/sdcard/my_record.wav'
                audio.start(path=self.output_file)
                self.root.ids.status.text = '🎤 Recording started...'
                self.start_progress(duration=5)
            except Exception as e:
                self.root.ids.status.text = f'Error: {e}'
        else:
            # وضع المحاكاة (Pydroid أو الحاسوب)
            self.root.ids.status.text = '🎙️ Simulating recording...'
            self.start_progress(duration=5)

    def start_progress(self, duration=5):
        """تحريك شريط التقدّم لمدة معينة"""
        self.progress_duration = duration
        self.progress_step = 100 / duration
        self.elapsed = 0
        Clock.schedule_interval(self.update_progress, 1)

    def update_progress(self, dt):
        self.elapsed += 1
        progress = self.root.ids.progress
        progress.value = min(100, self.elapsed * self.progress_step)

        if self.elapsed >= self.progress_duration:
            Clock.unschedule(self.update_progress)
            progress.opacity = 0  # إخفاء الشريط
            self.root.ids.status.text = '✅ Recording complete'

    def stop_recording(self):
        progress = self.root.ids.progress
        progress.opacity = 0  # إخفاء الشريط عند الإيقاف يدويًا
        if platform == "android" and PLYER_AVAILABLE:
            try:
                audio.stop()
                self.root.ids.status.text = f'✅ Recording saved to /sdcard/my_record.wav'
            except Exception as e:
                self.root.ids.status.text = f'Error: {e}'
        else:
            self.root.ids.status.text = '🟡 Simulation only (no real recording)'

    def play_recording(self):
        if platform == "android" and PLYER_AVAILABLE:
            try:
                sound = SoundLoader.load('/sdcard/my_record.wav')
                if sound:
                    sound.play()
                    self.root.ids.status.text = '▶️ Playing recorded audio...'
                else:
                    self.root.ids.status.text = '❌ No recorded file found'
            except Exception as e:
                self.root.ids.status.text = f'Error: {e}'
        else:
            self.root.ids.status.text = '🔊 Simulation: pretending to play audio'

if __name__ == '__main__':
    HybridRecorderApp().run()
