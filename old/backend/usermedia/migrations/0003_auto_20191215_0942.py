# Generated by Django 2.2.4 on 2019-12-15 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermedia', '0002_auto_20191215_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermedia',
            name='croppos_land',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='usermedia',
            name='croppos_port',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='usermedia',
            name='croppos_square',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
    ]