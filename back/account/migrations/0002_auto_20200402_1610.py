# Generated by Django 3.0.5 on 2020-04-02 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='about_me',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='goal',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='job',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='lookingfor',
        ),
    ]