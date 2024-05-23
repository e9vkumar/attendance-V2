from django.contrib import admin
from .models import statusclass,AttendanceRecord,userModel
# Register your models here.
admin.site.register(AttendanceRecord)
admin.site.register(userModel)
admin.site.register(statusclass)
