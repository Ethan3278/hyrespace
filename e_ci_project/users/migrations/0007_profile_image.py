# Generated by Django 2.0 on 2018-09-25 00:57

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_skill_skill_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=users.models.scramble_uploaded_filename, verbose_name='Avatar'),
        ),
    ]
