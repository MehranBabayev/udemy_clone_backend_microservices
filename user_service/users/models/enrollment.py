from django.db import models
from .profile import BaseModel
from django.utils.translation import gettext_lazy as _


class Enrollment(BaseModel):
    student = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='enrollments')
    course_id = models.IntegerField(_('Course ID'))
    progress = models.DecimalField(_('Progress'), max_digits=5, decimal_places=2, default=0.0)
    start_date = models.DateField(_('Start Date'), auto_now_add=True)
    end_date = models.DateField(_('End Date'), null=True, blank=True)
    status = models.CharField(_('Status'), max_length=20, choices=[
        ('active', _('Active')),
        ('completed', _('Completed')),
        ('dropped', _('Dropped'))
    ], default='active')

    def __str__(self):
        return f"{self.student.profile.user.email} - Course ID: {self.course_id}"
