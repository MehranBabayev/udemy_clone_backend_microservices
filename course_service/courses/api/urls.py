from django.urls import path
from .views import UserServiceDataAPIView, CourseDetailView, CourseWithLessonsView

urlpatterns = [
    path('courses/<int:course_id>/', CourseDetailView.as_view(), name='course-detail'),
    path('courses/<int:course_id>/lessons/', CourseWithLessonsView.as_view(), name='course-lessons'),
    path('external-users/', UserServiceDataAPIView.as_view(), name='external-user-data'),
]
