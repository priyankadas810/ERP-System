from django.contrib import admin
from .models import user_register, admin_register, user_attendance_monitor, user_notifications, membership

# Register your models here.
admin.site.register(user_register)

admin.site.register(admin_register)

admin.site.register(user_attendance_monitor)

admin.site.register(user_notifications)

admin.site.register(membership)