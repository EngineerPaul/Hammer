# Generated by Django 4.0.3 on 2022-03-22 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('referral', '0002_user_confirm_code_user_personal_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]