[app]
title = AzkarApp
package.name = mykivyapp
package.domain = org.test
source.dir = .
source.include_exts = py,ttf
version = 1.0
requirements = python3,kivy==2.3.0,arabic_reshaper,python-bidi,six
orientation = portrait
fullscreen = 0

# لو عندك خط مخصص (مثلاً arial-1.ttf)
# لازم تحطه في مجلد المشروع وتضيفه هنا
android.add_assets = arial-1.ttf

[buildozer]
log_level = 2
warn_on_root = 1
