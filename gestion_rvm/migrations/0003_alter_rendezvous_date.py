# Generated by Django 5.0 on 2024-05-12 16:24

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_rvm', '0002_remove_rendezvous_date_heure_remove_rendezvous_notes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rendezvous',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
