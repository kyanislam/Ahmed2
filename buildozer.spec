[app]
title = AzkarApp
package.name = azkarapp
package.domain = org.kyanislam
source.dir = .
source.include_exts = py,tff
version = 1.0
requirements = python3,kivy,kivy-garden,garden.arabictext
orientation = portrait
fullscreen = 1
android.permissions = INTERNET

# (اختياري) إضافة أي ملفات إضافية في مجلدات معينة:
# source.include_dirs = assets,images

[buildozer]
log_level = 2
warn_on_root = 1

[android]
# لتسريع البناء واختيار بنية محددة (arm64 فقط مثلاً)
# android.arch = arm64-v8a

# لتحديد الحد الأدنى لإصدار الأندرويد
# android.minapi = 21

# (اختياري) لتضمين أي مكتبات إضافية
# android.add_jars = libs/myjar.jar

# إذا كنت تستخدم garden widgets أو إضافات أخرى
# requirements = python3,kivy,kivy-garden,garden.arabictext

# إذا كان لديك ملفات kv أو صور في مجلدات معينة
# source.include_exts = py,png,jpg,kv,atlas
