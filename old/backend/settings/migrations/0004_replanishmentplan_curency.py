# Generated by Django 2.2.4 on 2020-02-04 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_auto_20200109_2341'),
    ]

    operations = [
        migrations.AddField(
            model_name='replanishmentplan',
            name='curency',
            field=models.CharField(choices=[('US', 'US'), ('EUR', 'EUR')], default='US', max_length=5, verbose_name='Curency'),
        ),
    ]