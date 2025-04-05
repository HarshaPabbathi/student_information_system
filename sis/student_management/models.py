from django.db import models

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)  # Explicitly set primary key
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    email = models.EmailField(unique=True, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    enrollment_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "students"  # Ensure Django uses this exact table name


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)  # Match MySQL primary key
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=20, unique=True)
    description = models.TextField(null=True, blank=True)
    credits = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "courses"  # Explicitly set the table name

class Enrollment(models.Model):
    enrollment_id = models.AutoField(primary_key=True)
    student_id = models.IntegerField(null=True)
    course_id = models.IntegerField(null=True)
    enrollment_date = models.DateField(null=True)
    grade = models.CharField(max_length=5, null=True)

    class Meta:
        db_table = "enrollments"  # Match the actual MySQL table name


class Instructor(models.Model):
    instructor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=100, unique=True, null=True)
    phone = models.CharField(max_length=15, null=True)
    department = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = "instructors"  # Match MySQL table name

class Assignment(models.Model):
    assignment_id = models.AutoField(primary_key=True)
    course_id = models.IntegerField(null=True)
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    due_date = models.DateField(null=True)

    class Meta:
        db_table = "assignments"  # This tells Django to use "assignments" instead of "student_management_assignment"

class Attendance(models.Model):
    attendance_id = models.AutoField(primary_key=True)
    student_id = models.IntegerField(null=True)
    course_id = models.IntegerField(null=True)
    attendance_date = models.DateField(null=True)
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent'), ('Late', 'Late')])

    class Meta:
        db_table = "attendance"  # Ensure Django uses the correct table name
