[app]

# (اسم التطبيق الذي يظهر للمستخدم)
title = 😀الحروف😀

# (اسم الحزمة، اختَر اسمًا فريدًا على شكل reverse domain)
package.name = mykivyapp
package.domain = org.example

# الإصدار
version = 0.1

# ملف/مجلد المصدر (بشكل عام: كل الملفات في المجلد الحالي)
source.dir = .

# ملفات وسائط تُدرج في الحزمة
source.include_exts = py,kv,png,jpg,txt,ico,xml,mp3,ttf

# أيقونة التطبيق (ضع ملف icon.png في جذر المشروع)
icon.filename = icon.png

# صورة شاشة البداية / presplash (ضع presplash.png في جذر المشروع)
presplash.filename = presplash.png
presplash_scale = fit
# توجيه الشاشة
orientation = portrait

# متطلبات بايثون/مكتبات (أضف ما تحتاجه)
requirements = python3,kivy

# صلاحيات أندرويد (أزل أو أضف حسب حاجتك)
android.permissions = INTERNET

# إعدادات Android (لا تغير إن لم تكن متأكدًا)
android.api = 33
android.minapi = 21
android.arch = armeabi-v7a, arm64-v8a

# تحسينات الحزمة
fullscreen = 0
presplash_color = #000000

[buildozer]
# مسار لتثبيت SDK/NDK (اتركها فارغة لاستخدام الافتراضي)
# android.sdk_path = /path/to/android/sdk

# تنظيف بناء سابق عند الحاجة
clean_on_rebuild = 1
