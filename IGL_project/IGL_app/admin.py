from django.contrib import admin
from .models import IGL_account



class IGL_admin(admin.ModelAdmin):
    list_display = ['IGL_username']


admin.site.register(IGL_account,IGL_admin)
