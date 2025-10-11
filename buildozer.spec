[app]
title = Voice Recorder
package.name = voicerecorder
package.domain = org.test
source.dir = .
source.include_exts = py, kv, wav
version = 1.0

# 📦 المتطلبات الأساسية
requirements = python3,kivy,plyer

# 🎙️ صلاحيات أندرويد المطلوبة
android.permissions = RECORD_AUDIO, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# مسار الأيقونة وشاشة البداية (اختياري)
icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/presplash.png

# توجيه الشاشة (عمودية)
orientation = portrait

# يدعم اللغة العربية والإنجليزية
android.allow_backup = True

# لمنع ظهور لوحة المفاتيح مع التشغيل
fullscreen = 0

# 🔊 لتحسين دعم الصوت (اختياري)
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.api = 33

# تقليل حجم التطبيق
log_level = 2
# إزالة المكتبات غير الضرورية
android.strip = True

# اسم حزمة Android النهائي
package.version_code = 1
