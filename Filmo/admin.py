from django.contrib import admin
from .models import Films, Users


@admin.register(Films)
class FilmsAdmin(admin.ModelAdmin):
    list_display = ('name', 'length', 'genre')
@admin.register(Users)
class UsersDisplay(admin.ModelAdmin):
    list_display = ('name', 'email','password')