# Generated by Django 5.1.6 on 2025-02-22 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Filmo', '0004_alter_films_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='films',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/media/films'),
        ),
    ]
