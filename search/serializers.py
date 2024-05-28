from rest_framework import serializers

from search.models import Building, Department, Teacher


class DepartmentSerializer(serializers.ModelSerializer):
    buildings = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    teachers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Department
        fields = ['id', 'name', 'buildings', 'teachers']
        read_only_fields = ['name']



class BuildingSerializer(serializers.ModelSerializer):
    departments = DepartmentSerializer(many=True, read_only=True)
    class Meta:
        model = Building
        fields = ['id', 'name', 'address', 'departments']
        read_only_fields = ['name', 'address']


class TeacherSerializer(serializers.ModelSerializer):
    departments = DepartmentSerializer(many=True, read_only=True)
    class Meta:
        model = Teacher
        fields = ['id', 'fullname', 'departments']
        read_only_fields = ['fullname']
