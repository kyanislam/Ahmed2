from kivy.app import App
from kivy.lang import Builder
from kivy.utils import platform
from kivy.core.audio import SoundLoader
from jnius import autoclass
from kivy.clock import Clock

KV = '''
BoxLayout:
    orientation: 'vertical'
    padding: 20
    spacing: 10

    Label:
        id: status
        text: "Press Start to record"
        font_size: '18sp'
        size_hint_y: None
        height: self.texture_size[1] + 20

    ProgressBar:
        id: progress
        max: 100
        value: 0
        size_hint_y: None
        height: 20
        opacity: 0  # مخفي افتراضيًا

    Button:
        text: "🎙️ Start Recording"
        font_size: '20sp'
        on_press: app.start_recording()

    Button:
        text: "⏹️ Stop Recording"
        font_size: '20sp'
        on_press: app.stop_recording()

    Button:
        text: "▶️ Play Recording"
        font_size: '20sp'
        on_press: app.play_recording()
'''

class AndroidRecorderApp(App):
    def build(self):
        self.sound = None
        self.progress_event = None
        return Builder.load_string(KV)

    def start_recording(self):
        if platform == 'android':
            from android.permissions import request_permissions, Permission
            request_permissions([
                Permission.RECORD_AUDIO,
                Permission.WRITE_EXTERNAL_STORAGE,
                Permission.READ_EXTERNAL_STORAGE
            ])

            MediaRecorder = autoclass('android.media.MediaRecorder')
            AudioSource = autoclass('android.media.MediaRecorder$AudioSource')
            OutputFormat = autoclass('android.media.MediaRecorder$OutputFormat')
            AudioEncoder = autoclass('android.media.MediaRecorder$AudioEncoder')

            self.recorder = MediaRecorder()
            self.recorder.setAudioSource(AudioSource.MIC)
            self.recorder.setOutputFormat(OutputFormat.THREE_GPP)
            self.recorder.setAudioEncoder(AudioEncoder.AMR_NB)
            self.output_file = '/sdcard/recorded_audio.3gp'
            self.recorder.setOutputFile(self.output_file)
            self.recorder.prepare()
            self.recorder.start()

            self.root.ids.status.text = "🎤 Recording..."
        else:
            self.root.ids.status.text = "⚠️ Recording works only on Android"

    def stop_recording(self):
        try:
            self.recorder.stop()
            self.recorder.release()
            self.root.ids.status.text = f"✅ Saved: {self.output_file}"
        except Exception as e:
            self.root.ids.status.text = f"Error stopping: {e}"

    def play_recording(self):
        try:
            sound = SoundLoader.load(self.output_file)
            if sound:
                self.sound = sound
                sound.play()
                self.root.ids.status.text = "🎧 Playing recording..."
                self.start_progress_bar(sound.length)
            else:
                self.root.ids.status.text = "⚠️ No recording found."
        except Exception as e:
            self.root.ids.status.text = f"Error playing: {e}"

    def start_progress_bar(self, duration):
        """تشغيل شريط التقدم أثناء التشغيل"""
        bar = self.root.ids.progress
        bar.opacity = 1
        bar.value = 0
        self.progress_time = 0

        if self.progress_event:
            self.progress_event.cancel()

        self.progress_event = Clock.schedule_interval(lambda dt: self.update_progress(dt, duration), 0.1)

    def update_progress(self, dt, duration):
        bar = self.root.ids.progress
        self.progress_time += dt
        bar.value = (self.progress_time / duration) * 100

        if self.progress_time >= duration:
            bar.opacity = 0
            bar.value = 0
            self.root.ids.status.text = "✅ Playback finished"
            self.progress_event.cancel()
            return False
        return True

AndroidRecorderApp().run()
