# Generated by Django 5.0.1 on 2024-01-14 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('actor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('sinopsis', models.TextField()),
                ('tags', models.CharField(max_length=350)),
                ('time_duration', models.CharField(max_length=10)),
                ('background_url', models.TextField()),
                ('director', models.CharField(max_length=250)),
                ('release_date', models.DateField()),
                ('is_hd', models.BooleanField()),
                ('is_movie', models.BooleanField()),
                ('is_tv_show', models.BooleanField()),
                ('actors', models.ManyToManyField(blank=True, to='actor.actor')),
            ],
            options={
                'db_table': 'table',
            },
        ),
    ]
