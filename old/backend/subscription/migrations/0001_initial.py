# Generated by Django 2.2.4 on 2020-01-09 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('payment', '0004_auto_20191227_0847'),
    ]

    operations = [
        migrations.CreateModel(
            name='BonusSubscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bonus_level', models.CharField(choices=[('0', 'basic'), ('1', 'normal'), ('2', 'best')], default='0', max_length=10)),
                ('expire_at', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BonusSubscription2PaymentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('limit', models.FloatField(default=0)),
                ('limit_measurement', models.CharField(choices=[('times', 'times (usage counts)'), ('duration', 'duration (minutes)')], max_length=15)),
                ('bonus_subscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscription.BonusSubscription')),
                ('payment_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.PaymentType')),
            ],
        ),
    ]
