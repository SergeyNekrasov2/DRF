from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


from course.models import Course
from course.serializers import CourseSerializer



class CourseViewSet(viewsets.ModelViewSet):

    serializer = CourseSerializer
    queryset = Course.objects.all()