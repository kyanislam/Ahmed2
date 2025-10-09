[app]
title = Colors Game
package.name = colorsgame
package.domain = org.test
source.dir = .
source.include_exts = py, mp3, png
version = 1.0

# المكتبات المطلوبة
requirements = python3, kivy==2.3.0, pillow

# اتجاه الشاشة
orientation = portrait
fullscreen = 0

# شاشة البدء (Splash Screen)


# أيقونة التطبيق
icon.filename = icon.png

# صلاحيات للتطبيق (تشغيل الصوت والوصول للملفات)
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# اسم الملف النهائي (اختياري)
android.arch = armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
