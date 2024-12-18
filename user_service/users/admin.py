# admin.py
from django.contrib import admin
from .models import CustomUser, OTP, Profile, Instructor, Student


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'is_active')
    search_fields = ('email', 'full_name')


@admin.register(OTP)
class OTPAdmin(admin.ModelAdmin):
    list_display = ('user', 'otp_code', 'created_at')
    readonly_fields = ('otp_code', 'created_at')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'location')


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('profile', 'total_students', 'average_rating')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('profile',)
