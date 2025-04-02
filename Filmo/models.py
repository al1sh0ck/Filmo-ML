from textwrap import shorten

from django.contrib.auth.hashers import make_password
from django.db import models

# Create your models here.
class Films(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Filmo/static/media/images', null=True, blank=True)
    length = models.IntegerField()
    genre = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # Увеличил длину для хеша

    def save(self, *args, **kwargs):
        if not self.password.startswith("pbkdf2_sha256$"):  # Проверяем, хеширован ли пароль
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
