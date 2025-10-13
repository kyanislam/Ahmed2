[buildozer]

[app]
title = AndroidRecorder
package.name = androidrecorder
package.domain = org.test
source.dir = .
source.include_exts = py, kv, 3gp
version = 1.0

requirements = python3,kivy,android
android.permissions = RECORD_AUDIO, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
orientation = portrait
