# Generated by Django 5.0.6 on 2024-05-26 14:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='departments',
            field=models.ManyToManyField(blank=True, related_name='building', to='search.department'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to='search.department'),
        ),
    ]
