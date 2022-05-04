# Generated by Django 4.0.4 on 2022-05-04 19:59

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, db_index=True, max_length=255, verbose_name='image'),
        ),
    ]