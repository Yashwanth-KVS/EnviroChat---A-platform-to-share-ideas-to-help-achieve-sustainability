# Generated by Django 5.0.6 on 2024-07-19 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_video'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='caption',
            new_name='Title',
        ),
    ]
