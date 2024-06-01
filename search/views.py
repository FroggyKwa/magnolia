from django.db.models import QuerySet, Q
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions
from rest_framework.response import Response

from search.models import Building, Department, Teacher
from search.serializers import BuildingSerializer, DepartmentSerializer, TeacherSerializer


class BuildingViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'head', 'options', 'trace']
    queryset = Building.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['departments__id']
    serializer_class = BuildingSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, pk=None, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        building = get_object_or_404(queryset, pk=pk)
        return Response(self.get_serializer(building).data)


class DepartmentViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'head', 'options', 'trace']
    queryset = Department.objects.prefetch_related('teachers', 'buildings').all()
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['buildings__id', 'name']
    serializer_class = DepartmentSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, pk=None, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        department = get_object_or_404(queryset, pk=pk)
        return Response(self.get_serializer(department).data)


class TeacherViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'head', 'options', 'trace']
    queryset = Teacher.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['department__id']
    serializer_class = TeacherSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, pk=None, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        teacher = get_object_or_404(queryset, pk=pk)
        return Response(self.get_serializer(teacher).data)


class SearchViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        query = self.request.query_params.get('query', '')
        if not query:
            result_teachers = Teacher.objects.all()
            result_departments = Department.objects.all()
            result_buildings = Building.objects.all()
        else:
            result_teachers = Teacher.objects.none()
            result_departments = Department.objects.none()
            result_buildings = Building.objects.none()
            for value in query.split(';'):
                result_teachers = Teacher.objects.filter(fullname__icontains=value)
                result_departments = Department.objects.filter(name__icontains=value)
                result_buildings = Building.objects.filter((Q(name__icontains=value) | Q(address__icontains=value)))

        department_filter = self.request.query_params.get('department__name', '')
        result_teachers = result_teachers.filter(department__name__icontains=department_filter).distinct()
        result_departments = result_departments.filter(name__icontains=department_filter).distinct()
        return Response(
            {
                "teachers": TeacherSerializer(result_teachers, many=True).data,
                "buildings": BuildingSerializer(result_buildings, many=True).data,
                "departments": DepartmentSerializer(result_departments, many=True).data
            }
        )
