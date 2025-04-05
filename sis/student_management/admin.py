from django.contrib import admin
from .models import Student, Course, Enrollment, Instructor, Assignment, Attendance

# Registering models to Django Admin
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Instructor)
admin.site.register(Assignment)
admin.site.register(Attendance)
