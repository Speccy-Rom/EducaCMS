from rest_framework import generics
from ..models import Subject
from .serializers import SubjectSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Course
from rest_framework import viewsets
from .serializers import CourseSerializer


class SubjectListView(generics.ListAPIView):
    """Вывод subject"""
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveAPIView):
    """"""
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    """блок обработчика"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
