# models/otp.py
from django.db import models
from django.conf import settings
from django.utils.timezone import now, timedelta
import random
from .profile import  BaseModel
from django.utils.translation import gettext_lazy as _

class OTP(BaseModel):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='otp'
    )
    otp_code = models.CharField(max_length=6, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(_('Expires At'))

    def generate_otp(self):
        self.otp_code = f"{random.randint(100000, 999999)}"
        self.created_at = now()
        self.expires_at = self.created_at + timedelta(minutes=2)
        self.save()

    def is_valid(self):
        return now() <= self.expires_at