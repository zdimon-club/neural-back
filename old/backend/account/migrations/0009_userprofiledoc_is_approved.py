# Generated by Django 2.2.4 on 2019-12-25 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_userprofiledoc'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofiledoc',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
