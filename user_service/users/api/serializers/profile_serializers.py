from rest_framework import serializers
from users.models.profile import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'avatar', 'headline', 'bio', 'language', 'website', 
            'location', 'social_links', 'is_instructor'
        )
        read_only_fields = ('is_instructor',)
