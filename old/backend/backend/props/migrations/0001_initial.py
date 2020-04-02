# Generated by Django 2.2.4 on 2019-12-04 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Props',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name', max_length=250, verbose_name='Name')),
                ('name_ru', models.CharField(help_text='Name', max_length=250, null=True, verbose_name='Name')),
                ('name_en', models.CharField(help_text='Name', max_length=250, null=True, verbose_name='Name')),
                ('alias', models.CharField(help_text='Alias', max_length=250, verbose_name='Alias')),
                ('type', models.CharField(choices=[('one', 'one'), ('many', 'many')], default='one', max_length=4, verbose_name='Type')),
                ('for_man', models.BooleanField(default=False, help_text='Show in the man form', verbose_name='Show in the man form')),
                ('for_woman', models.BooleanField(default=False, help_text='Show in the woman form', verbose_name='Show in the woman form')),
            ],
            options={
                'verbose_name': 'User property',
                'verbose_name_plural': 'User properties',
            },
        ),
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name', max_length=250, verbose_name='Name')),
                ('name_ru', models.CharField(help_text='Name', max_length=250, null=True, verbose_name='Name')),
                ('name_en', models.CharField(help_text='Name', max_length=250, null=True, verbose_name='Name')),
                ('prop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='props.Props')),
            ],
            options={
                'verbose_name': 'User property value',
                'verbose_name_plural': 'User property values',
            },
        ),
        migrations.CreateModel(
            name='Value2User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='props.Props')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.UserProfile')),
                ('value', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='props.Value')),
            ],
        ),
    ]
