# Generated by Django 2.0 on 2018-09-25 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20180925_0337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transcript',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transcripts', to='users.Profile'),
        ),
    ]
