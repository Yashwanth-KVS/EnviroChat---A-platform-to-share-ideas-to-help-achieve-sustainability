# Generated by Django 5.0.6 on 2024-07-22 16:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_alter_favorites_options_alter_feeds_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pages',
            name='feed',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='pages_related', to='myapp.feeds'),
        ),
    ]
