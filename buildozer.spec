[app]
# اسم التطبيق الذي سيظهر للمستخدم
title = Voice Recorder
# اسم حزمة التطبيق (يجب أن يكون فريدًا)
package.name = voicerecorder
package.domain = org.kivy
# مجلد الكود الرئيسي
source.dir = .
# تضمين الملفات المطلوبة
source.include_exts = py, wav, png, jpg, kv
# نسخة التطبيق
version = 1.0

# التطبيق الرئيسي
entrypoint = main.py

# المكتبات المطلوبة
requirements = python3,kivy,plyer

# الأذونات المطلوبة
android.permissions = RECORD_AUDIO, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# أيقونة التطبيق (اختياري)
icon.filename = icon.png

# دعم التخزين الخارجي (مطلوب لحفظ الصوت في /sdcard)
android.allow_backup = True
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.ndk_api = 21
android.archs = arm64-v8a, armeabi-v7a

# لغة الواجهة (UTF-8)
android.add_default_permissions = 1

# اسم الملف النهائي
package.version = 1.0
package.format = apk

# استخدام واجهة SDL2 الافتراضية
orientation = portrait

# تعطيل دعم أكواد الصوت القديمة
android.accept_sdk_license = True
android.debug = False

# اسم الحزمة النهائي للتطبيق
# سيصبح مثلاً org.kivy.voicerecorder
