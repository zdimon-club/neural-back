# Generated by Django 2.2.4 on 2020-02-24 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testwogs', '0003_logserver_test_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logserver',
            name='message',
            field=models.CharField(default='No message', max_length=1000),
        ),
    ]
