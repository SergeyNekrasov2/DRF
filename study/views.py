from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets
from study.models import Course, Lesson
from study.serializers import (CourseDetailSerializers,
                               CourseSerializers,
                               LessonSerializers)
from users.permissions import IsModerDRF, IsOwnerDRF


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializers
    queryset = Course.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return CourseDetailSerializers
        return CourseSerializers

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = (~IsModerDRF,)
        elif self.action in ["update", "retrieve"]:
            self.permission_classes = (IsModerDRF | IsOwnerDRF,)
        elif self.action == "destroy":
            self.permission_classes = (~IsModerDRF | IsOwnerDRF,)
        return super().get_permissions()


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializers


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
