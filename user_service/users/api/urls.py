from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.auth_views import RegisterView, LoginView, LogoutView
from .views.user_views import CurrentUserView, UserViewSet
from .views.profile_views import ProfileView
from .views.otp_views import GenerateOTPView, VerifyOTPView
from .views import InstructorDetailView

router = DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('otp/generate/', GenerateOTPView.as_view(), name='generate-otp'),
    path('otp/verify/', VerifyOTPView.as_view(), name='verify-otp'),
    path('api/users/instructors/<int:instructor_id>/', InstructorDetailView.as_view(), name='instructor-detail'),
    path('', include(router.urls)),
    
]
