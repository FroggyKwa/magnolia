# Generated by Django 5.0.6 on 2024-05-31 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_department_ext_attributes'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='ext_attributes',
            field=models.ManyToManyField(blank=True, related_name='buildings', to='search.extattribute'),
        ),
    ]
