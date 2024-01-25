# Generated by Django 5.0.1 on 2024-01-15 23:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_rename_subsription_client_subscription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='payment_day',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(31)]),
        ),
    ]