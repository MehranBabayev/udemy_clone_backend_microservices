from django.db import models
from .profile import Profile, BaseModel
from django.utils.translation import gettext_lazy as _


class Instructor(BaseModel):
    profile = models.OneToOneField(
        'Profile', on_delete=models.CASCADE, related_name='instructor'
    )
    total_students = models.PositiveIntegerField(_('Total Students'), default=0)
    total_reviews = models.PositiveIntegerField(_('Total Reviews'), default=0)
    average_rating = models.DecimalField(_('Average Rating'), max_digits=3, decimal_places=2, default=0.0)
    earnings = models.DecimalField(_('Earnings'), max_digits=10, decimal_places=2, default=0.0)
    specializations = models.TextField(_('Specializations'), blank=True)
    experience_years = models.PositiveIntegerField(_('Years of Experience'), default=0)

    def __str__(self):
        return f"Instructor: {self.profile.user.email}"
