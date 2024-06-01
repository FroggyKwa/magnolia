from rest_framework import serializers

from search.models import Building, Department, Teacher, ExtAttribute


class ExtAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtAttribute
        fields = ['id', 'name', 'value']


class ShortDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name']
        read_only_fields = ['name']

class DepartmentSerializer(serializers.ModelSerializer):
    buildings = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    teachers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    ext_attributes = ExtAttributeSerializer(many=True, read_only=True)
    class Meta:
        model = Department
        fields = ['id', 'name', 'buildings', 'teachers', 'ext_attributes']
        read_only_fields = ['name']



class BuildingSerializer(serializers.ModelSerializer):
    departments = DepartmentSerializer(many=True, read_only=True)
    ext_attributes = ExtAttributeSerializer(many=True, read_only=True)
    class Meta:
        model = Building
        fields = ['id', 'name', 'address', 'departments', 'ext_attributes']
        read_only_fields = ['name', 'address']


class TeacherSerializer(serializers.ModelSerializer):
    department = ShortDepartmentSerializer(read_only=True)
    ext_attributes = ExtAttributeSerializer(many=True, read_only=True)

    class Meta:
        model = Teacher
        fields = ['id', 'fullname', 'department', 'ext_attributes']
        read_only_fields = ['fullname']
