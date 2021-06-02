from django.contrib import admin

# Register your models here.
from login_register_app.models import *


@admin.register(User)
class User(admin.ModelAdmin):
    pass
