# Generated by Django 2.2.4 on 2020-01-10 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0002_auto_20200109_2341'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bonussubscription2paymenttype',
            old_name='limit_measurement',
            new_name='limit_units',
        ),
        migrations.AlterField(
            model_name='bonussubscription2paymenttype',
            name='bonus_subscription',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='subscription.BonusSubscription'),
        ),
    ]
