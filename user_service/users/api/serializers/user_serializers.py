from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'full_name', 'is_active', 'is_email_verified', 'last_login_ip')
        read_only_fields = ('id', 'is_active', 'is_email_verified', 'last_login_ip')
