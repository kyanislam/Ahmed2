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
        opacity: 0

    Button:
        text: "🎙️ Start Recording"
        font_size: '20sp'
        on_press: app.request_permission_and_record()

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
        self.recorder = None
        self.progress_event = None
        return Builder.load_string(KV)

    def request_permission_and_record(self):
        """طلب إذن أولاً ثم البدء بعد ثانيتين لتفادي الكراش"""
        if platform == 'android':
            from android.permissions import request_permissions, Permission
            request_permissions([
                Permission.RECORD_AUDIO,
                Permission.WRITE_EXTERNAL_STORAGE,
                Permission.READ_EXTERNAL_STORAGE
            ])
            self.root.ids.status.text = "⏳ Waiting for permission..."
            Clock.schedule_once(lambda dt: self.start_recording(), 2)
        else:
            self.root.ids.status.text = "⚠️ Works only on Android"

    def start_recording(self):
        try:
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
        except Exception as e:
            self.root.ids.status.text = f"⚠️ Error starting: {e}"

    def stop_recording(self):
        try:
            if self.recorder:
                self.recorder.stop()
                self.recorder.release()
                self.root.ids.status.text = f"✅ Saved: {self.output_file}"
            else:
                self.root.ids.status.text = "⚠️ No active recorder."
        except Exception as e:
            self.root.ids.status.text = f"⚠️ Error stopping: {e}"

    def play_recording(self):
        try:
            sound = SoundLoader.load(self.output_file)
            if sound:
                sound.play()
                self.root.ids.status.text = "🎧 Playing recording..."
                self.start_progress_bar(sound.length)
            else:
                self.root.ids.status.text = "⚠️ No recording found."
        except Exception as e:
            self.root.ids.status.text = f"⚠️ Error playing: {e}"

    def start_progress_bar(self, duration):
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
