# Generated by Django 5.0.7 on 2024-07-12 23:03

import datetime
import django.contrib.auth.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to=settings.AUTH_USER_MODEL)),
                ('user_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('email_id', models.EmailField(max_length=254, unique=True)),
                ('dob', models.DateField(default=datetime.date.today)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Followers',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('followee_id', models.ManyToManyField(related_name='following', to='myapp.member')),
                ('follower_id', models.ManyToManyField(related_name='followers', to='myapp.member')),
            ],
        ),
        migrations.CreateModel(
            name='feeds',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.member')),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('category', models.IntegerField(choices=[(1, 'Thread'), (2, 'Regular Post'), (3, 'Video Post')], default=2)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.member')),
            ],
        ),
        migrations.CreateModel(
            name='feeds_posts',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('feed_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.feeds')),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.posts')),
            ],
        ),
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.member')),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.posts')),
            ],
        ),
    ]
