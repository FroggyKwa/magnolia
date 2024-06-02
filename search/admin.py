from django.contrib import admin
from search.models import *

@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    pass

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass

@admin.register(TeacherExtAttribute)
class TeacherExtAttributeAdmin(admin.ModelAdmin):
    pass

@admin.register(BuildingExtAttribute)
class BuildingExtAttributeAdmin(admin.ModelAdmin):
    pass

@admin.register(DepartmentExtAttribute)
class DepartmentExtAttributeAdmin(admin.ModelAdmin):
    pass

