from rest_framework import serializers

from search.models import Building, Department, Teacher, DepartmentExtAttribute, BuildingExtAttribute, TeacherExtAttribute


class ExtAttributeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    value = serializers.CharField(max_length=255)


class ShortDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name']
        read_only_fields = ['name']

class DepartmentSerializer(serializers.ModelSerializer):
    buildings = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    teachers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    ext_attributes = ExtAttributeSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = Department
        fields = ['id', 'name', 'buildings', 'teachers', 'ext_attributes']
        read_only_fields = ['name']



class BuildingSerializer(serializers.ModelSerializer):
    departments = DepartmentSerializer(many=True, read_only=True)
    ext_attributes = ExtAttributeSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = Building
        fields = ['id', 'name', 'address', 'departments', 'ext_attributes']
        read_only_fields = ['name', 'address']


class TeacherSerializer(serializers.ModelSerializer):
    department = ShortDepartmentSerializer(read_only=True)
    ext_attributes = ExtAttributeSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Teacher
        fields = ['id', 'fullname', 'department', 'ext_attributes']
        read_only_fields = ['fullname']
