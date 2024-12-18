from rest_framework import serializers
from courses.models import Lesson

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'course', 'video_url', 'content', 'order']
