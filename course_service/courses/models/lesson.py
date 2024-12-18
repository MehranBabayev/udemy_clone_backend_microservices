from django.db import models
from django.utils.translation import gettext_lazy as _

class Lesson(models.Model):
    title = models.CharField(_('Lesson Title'), max_length=255)
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE, related_name='lessons')
    video_url = models.URLField(_('Video URL'), blank=True, null=True)
    content = models.TextField(_('Content'), blank=True)
    order = models.PositiveIntegerField(_('Order'), default=0)

    def __str__(self):
        return f"{self.course.title} - {self.title}"
