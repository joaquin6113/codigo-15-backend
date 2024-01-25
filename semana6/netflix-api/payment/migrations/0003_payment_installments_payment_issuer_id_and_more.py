# Generated by Django 5.0.1 on 2024-01-18 04:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_payment_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='installments',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(36)]),
        ),
        migrations.AddField(
            model_name='payment',
            name='issuer_id',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='payment',
            name='payer_document_number',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='payment',
            name='payer_document_type',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='payment',
            name='payer_email',
            field=models.EmailField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_method_id',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='payment',
            name='token',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
