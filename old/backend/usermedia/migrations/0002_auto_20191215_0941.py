# Generated by Django 2.2.4 on 2019-12-15 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermedia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermedia',
            name='croppos_land',
            field=models.CharField(default='', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='usermedia',
            name='croppos_port',
            field=models.CharField(default='', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='usermedia',
            name='croppos_square',
            field=models.CharField(default='', max_length=250, null=True),
        ),
    ]
