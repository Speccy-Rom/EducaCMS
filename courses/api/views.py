from rest_framework import generics, viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from ..models import Subject, Course
from rest_framework.response import Response
from .serializers import CourseSerializer, SubjectSerializer, CourseWithContentsSerializer
from rest_framework.decorators import action
from .permissions import IsEnrolled


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

    @action(methods=['post'],
            detail=[BasicAuthentication],
            permission_classes=[IsAuthenticated])
    def enroll(self, request, *args, **kwargs):
        """

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        course = self.get_object()
        course.students.add(request.user)
        return Response({'enrolled': True})

    @action(methods=['get'],
            detail=CourseWithContentsSerializer,
            authentication_classes=[BasicAuthentication],
            permission_classes=[IsAuthenticated,
                                IsEnrolled])
    def contents(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
