from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from .models import *


class LoginView(View):

    def get(self, request):
        return render(request, "login.html")

    def post(self, request):

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("dashboard")

        return render(
            request,
            "login.html",
            {
                "error": "Invalid username or password"
            }
        )


class LogoutView(View):

    def get(self, request):

        logout(request)

        return redirect("login")


class DashboardView(LoginRequiredMixin, TemplateView):

  template_name = "dashboard.html"

  login_url = "/login/"

  def get_context_data(self, **kwargs):

    context = super().get_context_data(**kwargs)

    context["total_students"] = Student.objects.count()

    context["total_staff"] = Staff.objects.count()

    context["total_courses"] = Course.objects.count()

    context["total_subjects"] = Subject.objects.count()

    context["total_sessions"] = Session.objects.count()

    context["total_attendance"] = Attendance.objects.count()

    context["total_notifications"] = Notification.objects.count()

    context["recent_students"] = Student.objects.all()[:10]

    return context
  
class StudentListView(LoginRequiredMixin, TemplateView):

    template_name = "students.html"

    login_url = "/login/"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["students"] = Student.objects.all()

        return context


class StaffListView(LoginRequiredMixin, TemplateView):

    template_name = "staff.html"

    login_url = "/login/"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["staffs"] = Staff.objects.all()

        return context


class CourseListView(LoginRequiredMixin, TemplateView):

    template_name = "courses.html"

    login_url = "/login/"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["courses"] = Course.objects.all()

        return context


class SubjectListView(LoginRequiredMixin, TemplateView):

    template_name = "subjects.html"

    login_url = "/login/"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["subjects"] = Subject.objects.all()

        return context

class AttendanceListView(LoginRequiredMixin, TemplateView):

    template_name = "attendance.html"

    login_url = "/login/"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["attendances"] = Attendance.objects.all()

        return context

class NotificationListView(LoginRequiredMixin, TemplateView):

    template_name = "notifications.html"

    login_url = "/login/"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["notifications"] = Notification.objects.all()

        return context


class SessionListView(LoginRequiredMixin, TemplateView):

    template_name = "sessions.html"

    login_url = "/login/"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["sessions"] = Session.objects.all()

        return context