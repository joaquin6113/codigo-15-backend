# Generated by Django 5.0.1 on 2024-01-15 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_client_payment_day_client_subsription'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='subsription',
            new_name='subscription',
        ),
    ]