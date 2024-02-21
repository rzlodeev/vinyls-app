from django.contrib import admin
from .models import User
from app.models import Disc, UserProfile


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')


admin.site.register(User, CustomUserAdmin)
admin.site.register(Disc)
admin.site.register(UserProfile)

# Register your models here.
