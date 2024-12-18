from django.db import models
from .profile import  BaseModel
from django.utils.translation import gettext_lazy as _


class Student(BaseModel):
    profile = models.OneToOneField(
        'Profile', on_delete=models.CASCADE, related_name='student'
    )
    learning_goals = models.TextField(_('Learning Goals'), blank=True)

    def __str__(self):
        return f"Student: {self.profile.user.email}"
