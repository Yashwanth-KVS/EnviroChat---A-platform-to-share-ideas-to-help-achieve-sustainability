# Generated by Django 5.0.6 on 2024-07-23 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_mediacontent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='email_id',
        ),
    ]
