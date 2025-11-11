from django.contrib import admin

# Register your models here.
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name','email', 'school', 'role', 'is_active','rates','qualification')
    list_display = ('first_name', 'last_name', 'school','role','email', 'is_active','rates', 'qualification')
admin.site.register(CustomUser,CustomUserAdmin)

