from django.db import models


class Building(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    departments = models.ManyToManyField(to="Department", related_name="buildings", blank=True)

    def __repr__(self):
        return self.name

    class Meta:
        db_table = 'buildings'


class Department(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __repr__(self):
        return self.name

    class Meta:
        db_table = 'departments'


class Teacher(models.Model):
    fullname = models.CharField(max_length=64, blank=True, null=True)
    department = models.ForeignKey(Department, related_name='teachers', on_delete=models.CASCADE, blank=True, null=True)

    def __repr__(self):
        return self.fullname

    class Meta:
        db_table = 'teachers'


class TeacherExtAttribute(models.Model):
    teacher = models.ForeignKey(Teacher, related_name='ext_attributes', on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)

    def __repr__(self):
        return f'{self.name} - {self.value}'

    class Meta:
        db_table = 'teachers_ext_attributes'
        unique_together = (('name', 'value'),)


class DepartmentExtAttribute(models.Model):
    department = models.ForeignKey(Department, related_name='ext_attributes', on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)

    def __repr__(self):
        return f'{self.name} - {self.value}'

    class Meta:
        db_table = 'department_ext_attributes'
        unique_together = (('name', 'value'),)


class BuildingExtAttribute(models.Model):
    Building = models.ForeignKey(Building, related_name='ext_attributes', on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)

    def __repr__(self):
        return f'{self.name} - {self.value}'

    class Meta:
        db_table = 'building_ext_attributes'
        unique_together = (('name', 'value'),)
