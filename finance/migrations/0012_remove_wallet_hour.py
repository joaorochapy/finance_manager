# Generated by Django 4.1 on 2022-10-06 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0011_wallet_hour_alter_wallet_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wallet',
            name='hour',
        ),
    ]
