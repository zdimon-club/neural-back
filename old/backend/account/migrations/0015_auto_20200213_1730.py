# Generated by Django 2.2.4 on 2020-02-13 17:30

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_userprofile_is_blocked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='account',
            field=models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=20),
        ),
    ]
