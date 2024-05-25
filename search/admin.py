from django.contrib import admin
from models import *

@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    pass

@admin.register(Department)
class TeacherAdmin(admin.ModelAdmin):
    pass

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass

    