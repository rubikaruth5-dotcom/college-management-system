from django.urls import path

from .views import *

urlpatterns = [

    path(
        "login/",
        LoginView.as_view(),
        name="login"
    ),

    path(
        "logout/",
        LogoutView.as_view(),
        name="logout"
    ),

    path(
        "dashboard/",
        DashboardView.as_view(),
        name="dashboard"
    ),
    path(
        "students/",
        StudentListView.as_view(),
        name="students"
    ),

    path(
        "staff/",
        StaffListView.as_view(),
        name="staff"
    ),

    path(
        "courses/",
        CourseListView.as_view(),
        name="courses"
    ),

    path(
        "subjects/",
        SubjectListView.as_view(),
        name="subjects"
    ),
    path(
    "attendance/",
    AttendanceListView.as_view(),
    name="attendance"
    ),

    path(
    "notifications/",
    NotificationListView.as_view(),
    name="notifications"
    ),

    path(
    "sessions/",
    SessionListView.as_view(),
    name="sessions"
    ),

]