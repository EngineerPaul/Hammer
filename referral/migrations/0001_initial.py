# Generated by Django 4.0.3 on 2022-03-20 17:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hammer_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField(unique=True, validators=[django.core.validators.MinValueValidator(89000000000), django.core.validators.MaxValueValidator(89999999999)], verbose_name='phone')),
                ('personal_code', models.CharField(max_length=6, unique=True, verbose_name='personal_code')),
                ('referral_code', models.CharField(blank=True, max_length=6, null=True, verbose_name='referral_code')),
            ],
        ),
    ]