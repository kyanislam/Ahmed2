[app]
title = Colors Game
package.name = colorsgame
package.domain = org.test
source.dir = .
source.include_exts = py, mp3, png, jpg,
version = 1.0
requirements = python3, kivy==2.3.0, pillow
orientation = portrait

# 👇 هذا السطر يلغي واجهة Kivy الافتراضية ويستبدلها بملفك
presplash.filename = presplash.png
# أو يمكنك جعلها فقط لون بدون صورة 👇
presplash_color = #FFFFFF

# 👇 هذا السطر يحدد الأيقونة
icon.filename = icon.png
