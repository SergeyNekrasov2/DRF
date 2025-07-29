from rest_framework import serializers

from study.models import Course, Lesson


class LessonSerializers(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializers(serializers.ModelSerializer):
    lessons = LessonSerializers(many=True, read_only=True)

    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializers(serializers.ModelSerializer):
    course_count_lessons = serializers.SerializerMethodField()
    lessons = LessonSerializers(many=True, read_only=True)

    def get_course_count_lessons(self, course):
        return course.lessons.count()

    class Meta:
        model = Course
        fields = (
            "title",
            "description",
            "course_count_lessons",
            "lessons",
        )
