from django.db import models


class Building(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    departments = models.ManyToManyField(to="Department", related_name="buildings", blank=True)
    ext_attributes = models.ManyToManyField(to="ExtAttribute", related_name="buildings", blank=True)

    class Meta:
        db_table = 'buildings'

class Department(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    ext_attributes = models.ManyToManyField(to="ExtAttribute", related_name="departments", blank=True)

    class Meta:
        db_table = 'departments'


class Teacher(models.Model):
    fullname = models.CharField(max_length=64, blank=True, null=True)
    department = models.ForeignKey(Department, related_name='teachers', on_delete=models.CASCADE)
    ext_attributes = models.ManyToManyField(to="ExtAttribute", related_name="teachers", blank=True)

    class Meta:
        db_table = 'teachers'


class ExtAttribute(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    class Meta:
        db_table = 'ext_attributes'
        unique_together = (('name', 'value'),)
