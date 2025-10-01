[app]
title = AzkarApp
package.name = azkarapp
package.domain = org.test
source.dir = .
source.include_exts = py, ttf
version = 1.0

# المكتبات اللي محتاجها البرنامج
requirements = python3, kivy==2.3.0, pillow, setuptools, six, arabic_reshaper, python-bidi

orientation = portrait
fullscreen = 0

# حط أي صلاحيات هنا
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
