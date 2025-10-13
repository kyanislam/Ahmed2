[buildozer]

[app]
title = Voice Recorder
package.name = voicerecorder
package.domain = org.kivy
source.dir = .
source.include_exts = py, wav, png, jpg, kv
entrypoint = main.py
version = 1.0
requirements = python3,kivy,plyer
android.permissions = RECORD_AUDIO, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25c
orientation = portrait
android.allow_backup = True
android.accept_sdk_license = True
package.format = apk
android.archs = arm64-v8a, armeabi-v7a
