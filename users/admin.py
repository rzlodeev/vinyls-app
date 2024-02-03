from django.contrib import admin
from .models import User
from app.models import Disc


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')


admin.site.register(User, CustomUserAdmin)
admin.site.register(Disc)

# Register your models here.
