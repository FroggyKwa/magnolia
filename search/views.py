from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions
from rest_framework.response import Response

from search.models import Building, Department, Teacher
from search.serializers import BuildingSerializer, DepartmentSerializer, TeacherSerializer


class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['name', "address"]
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
    queryset = Department.objects.prefetch_related('teachers', 'buildings').all()
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['name']
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
    queryset = Teacher.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['fullname']
    serializer_class = TeacherSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, pk=None, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        teacher = get_object_or_404(queryset, pk=pk)
        return Response(self.get_serializer(teacher).data)
