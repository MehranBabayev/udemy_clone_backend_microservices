from django.db import models
from django.utils.translation import gettext_lazy as _
import requests

class Course(models.Model):
    title = models.CharField(_('Course Title'), max_length=255)
    description = models.TextField(_('Description'))
    instructor_id = models.IntegerField(_('Instructor ID'))  # Ссылка на инструктора по его ID
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, related_name='courses')
    price = models.DecimalField(_('Price'), max_digits=10, decimal_places=2, default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(_('Is Published'), default=False)

    def __str__(self):
        return self.title
    

    def get_instructor(self):
        # Запрос к другому микросервису (User Service)
        response = requests.get(f'http://user_service/api/users/{self.instructor_id}')
        if response.status_code == 200:
            # Возвращаем имя пользователя
            return response.json().get('username', 'Instructor not found')
        return 'Instructor not found'
