from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Profile(BaseModel):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile'
    )
    avatar = models.ImageField(_('Avatar'), upload_to='avatars/', blank=True, null=True)
    headline = models.CharField(_('Headline'), max_length=60, blank=True)
    bio = models.TextField(_('Biography'), blank=True)
    language = models.CharField(_('Language'), max_length=50, blank=True, default='English (US)')
    website = models.URLField(_('Website'), blank=True)
    location = models.CharField(_('Location'), max_length=100, blank=True)
    social_links = models.JSONField(_('Social Links'), default=dict, blank=True)
    is_instructor = models.BooleanField(_('Is Instructor'), default=False)

    def __str__(self):
        return self.user.email