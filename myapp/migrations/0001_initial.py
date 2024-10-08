# Generated by Django 5.0.6 on 2024-07-15 03:14

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
                ('user_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('email_id', models.EmailField(max_length=254, unique=True)),
                ('dob', models.DateField(default=datetime.date.today)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('profile_picture', models.ImageField(upload_to='profile_pictures')),
                ('cover_picture', models.ImageField(upload_to='cover_pictures')),
                ('interests', models.TextField(blank=True)),
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
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.IntegerField(choices=[(1, 'Request'), (2, 'Following')])),
                ('followee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to='myapp.member')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='myapp.member')),
            ],
        ),
        migrations.CreateModel(
            name='Feeds',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.member')),
            ],
        ),
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('page_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('content', models.TextField()),
                ('title_img', models.FileField(default='title_page.jpg', upload_to='title_imgs')),
                ('content_img', models.FileField(default='content_image.jpg', upload_to='content_imgs')),
                ('about_page', models.TextField(default='The page promotes discussion base for green energy')),
                ('about_img', models.FileField(default='content_page.jpg', upload_to='about_imgs')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.member')),
            ],
        ),
        migrations.CreateModel(
            name='Pages_comments',
            fields=[
                ('pages_comment_id', models.IntegerField(primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('upvote', models.IntegerField(choices=[(0, 'Yes'), (1, 'No')], default=0)),
                ('downvote', models.IntegerField(choices=[(0, 'Yes'), (1, 'No')], default=0)),
                ('page_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.pages')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.member')),
            ],
        ),
        migrations.CreateModel(
            name='Pages_followers',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('follower_id', models.ManyToManyField(related_name='followers_pages', to='myapp.member')),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.IntegerField(choices=[(1, 'Thread'), (2, 'Regular Post'), (3, 'Video Post')], default=2)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.member')),
            ],
        ),
        migrations.CreateModel(
            name='FeedsPosts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.feeds')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.posts')),
            ],
        ),
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.member')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.posts')),
            ],
        ),
    ]
