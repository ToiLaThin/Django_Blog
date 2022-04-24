# Generated by Django 4.0.4 on 2022-04-24 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='blog_url',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='fb_url',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='zalo_url',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]