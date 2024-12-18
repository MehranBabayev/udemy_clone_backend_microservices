from rest_framework import serializers
from users.models.otp import OTP

class OTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTP
        fields = ('otp_code', 'expires_at')
        read_only_fields = ('otp_code', 'expires_at')
