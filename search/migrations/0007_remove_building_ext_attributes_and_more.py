# Generated by Django 5.0.6 on 2024-06-02 06:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0006_alter_teacher_department_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='building',
            name='ext_attributes',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='ext_attributes',
        ),
        migrations.RemoveField(
            model_name='department',
            name='ext_attributes',
        ),
        migrations.CreateModel(
            name='BuildingExtAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('value', models.CharField(blank=True, max_length=255, null=True)),
                ('Building', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='ext_attributes', to='search.building')),
            ],
            options={
                'db_table': 'building_ext_attributes',
                'unique_together': {('name', 'value')},
            },
        ),
        migrations.CreateModel(
            name='DepartmentExtAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('value', models.CharField(blank=True, max_length=255, null=True)),
                ('department', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='ext_attributes', to='search.department')),
            ],
            options={
                'db_table': 'department_ext_attributes',
                'unique_together': {('name', 'value')},
            },
        ),
        migrations.CreateModel(
            name='TeacherExtAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('value', models.CharField(blank=True, max_length=255, null=True)),
                ('teacher', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='ext_attributes', to='search.teacher')),
            ],
            options={
                'db_table': 'teachers_ext_attributes',
                'unique_together': {('name', 'value')},
            },
        ),
        migrations.DeleteModel(
            name='ExtAttribute',
        ),
    ]
