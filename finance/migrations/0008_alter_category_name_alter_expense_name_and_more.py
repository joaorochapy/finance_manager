# Generated by Django 4.1 on 2022-09-12 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0007_alter_extramoney_options_expense_wallet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='extramoney',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Dinheiro Extra'),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nome'),
        ),
    ]
