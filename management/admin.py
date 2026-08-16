from django.contrib import admin
from django.contrib import admin

from .models import *

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at")
    search_fields = ("name",)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "course")
    search_fields = ("name",)
    list_filter = ("course",)


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "phone")
    search_fields = ("name", "email")


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "email",
        "phone",
        "course",
    )
    search_fields = ("name", "email")
    list_filter = ("course",)


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "session_start",
        "session_end",
    )


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "student",
        "subject",
        "date",
        "status",
    )
    list_filter = ("date", "status", "subject")


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "created_at",
        "is_read",
    )
    search_fields = ("title", "message")
    list_filter = ("is_read",)