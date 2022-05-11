from django.contrib.auth.models import Permission
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import Account

admin.site.register(Account, UserAdmin)
admin.site.register(Permission)
