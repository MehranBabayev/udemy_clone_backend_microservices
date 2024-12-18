# courses/admin.py
from django.contrib import admin
from .models import Course, Lesson, Category
from django.utils.translation import gettext_lazy as _

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_instructor', 'category', 'price', 'is_published', 'created_at')
    search_fields = ('title',)
    list_filter = ('category', 'is_published')
    ordering = ('-created_at',)

    # Переопределение метода для отображения имени инструктора
    def get_instructor(self, obj):
        # Вызываем метод для получения инструктора
        return obj.get_instructor()  # Получаем имя инструктора через API
    get_instructor.short_description = _('Instructor')

# Регистрируем модель Lesson в админке
@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order', 'video_url')
    search_fields = ('title', 'course__title')
    list_filter = ('course',)
    ordering = ('course', 'order')

# Регистрируем модель Category в админке
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    search_fields = ('name',)
    list_filter = ('parent',)
