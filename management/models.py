from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):

    name = models.CharField(max_length=100)

    description = models.TextField(blank=True)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering=["id"]


class Subject(models.Model):

    name = models.CharField(max_length=100)

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="subjects"
    )

    def __str__(self):
        return self.name

    class Meta:
            ordering=["id"]
    


class Staff(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=15)

    address = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
            ordering=["id"]
    


class Student(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=15)

    address = models.TextField(blank=True)

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="students"
    )

    def __str__(self):
        return self.name

    class Meta:
            ordering=["id"]
    


class Session(models.Model):

    session_start = models.DateField()

    session_end = models.DateField()

    def __str__(self):
        return f"{self.session_start} - {self.session_end}"

    class Meta:
            ordering=["id"]
    


class Attendance(models.Model):

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE
    )

    date = models.DateField()

    status = models.BooleanField(
        default=False
    )

    def __str__(self):
        return f"{self.student.name} - {self.date}"

    class Meta:
            ordering=["id"]
    


class Notification(models.Model):

    title = models.CharField(
        max_length=200
    )

    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    is_read = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.title

    class Meta:
            ordering=["id"]
    
