# Generated by Django 4.1 on 2022-10-15 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0016_expense_status_alter_wallet_hour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='date_and_hour',
            field=models.DateTimeField(help_text='Use o seguinte formato: 15/06/2022 15:45', verbose_name='Data e hora'),
        ),
    ]
