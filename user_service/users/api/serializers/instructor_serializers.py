from rest_framework import serializers
from users.models.instructor import Instructor

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = (
            'total_students', 'total_reviews', 'average_rating', 
            'earnings', 'specializations', 'experience_years'
        )
