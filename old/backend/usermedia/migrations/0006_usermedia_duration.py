# Generated by Django 2.2.4 on 2020-01-02 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermedia', '0005_auto_20191224_0658'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermedia',
            name='duration',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]