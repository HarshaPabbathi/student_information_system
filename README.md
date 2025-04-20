# Student Information System (SIS)
## Overview
This is a **Django-based Student Information System (SIS)** designed to manage student-related data, including student profiles, courses, enrollments, instructors, assignments, and attendance. The application uses Django's ORM to interact with a MySQL database, with models explicitly mapped to corresponding database tables.
## Project Structure
The project includes the following key files in the student_management Django app:

- **'apps.py'**: Configures the student_management Django application, specifying the default auto field and app name.
- **'models.py'**: Defines the database models for the application, including:
    -'Student': Stores student details such as name, email, and enrollment date.
    Course: Manages course information like course name, code, and credits.
    Enrollment: Tracks student enrollments in courses, including grades.
    Instructor: Stores instructor details such as name, email, and department.
    Assignment: Manages course assignments with titles, descriptions, and due dates.
    Attendance: Records student attendance for courses with status (Present, Absent, Late).
- **'admin.py'**: Registers all models with the Django admin interface for easy management.
-**'views.py'**: Placeholder for view functions (currently empty, to be implemented).
-**'tests.py'**: Placeholder for unit tests (currently empty, to be implemented).
-**'manage.py'**: Django's command-line utility for running administrative tasks like migrations and server startup.

## **Setup Instructions**
### **Prerequisites**

    - **Python 3.8+**
    - **Django 3.2+**
    - **MySQL** (or another compatible database)
    - **Virtualenv** (recommended)

### **Installation**

1. **Clone the repository:**
   
        - **git clone <repository-url>**
        - **cd sis**
   
2.  **Set up a virtual environment:**

        - **python -m venv venv**
        - **source venv/bin/activate  # On Windows: venv\Scripts\activate**

3. **Install dependencies:**

        - **pip install django mysqlclient**

4. **Configure the database:**

        - **Update the DATABASES setting in sis/settings.py to match your MySQL database configuration:DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'your_database_name',
                'USER': 'your_database_user',
                'PASSWORD': 'your_database_password',
                'HOST': 'localhost',
                'PORT': '3306',
            }
        }**

5. **Run migrations:**

        - **python manage.py makemigrations**
        - **python manage.py migrate**

6.**Create a superuser (for admin access):**

       - **python manage.py createsuperuser**

7. **Run the development server:**
    
        - **python manage.py runserver**
        - **The application will be available at http://127.0.0.1:8000.**

8. **Access the admin interface:**
   
        - **Navigate to http://127.0.0.1:8000/admin and log in with the superuser credentials.**
        - **All models (Student, Course, etc.) are registered and can be managed here.**


## **Database Schema**
The models are mapped to the following MySQL tables (as specified in the Meta classes):

**students:** Student data

**courses:** Course data

**enrollments:** Enrollment records

**instructors:** Instructor data

**assignments:** Assignment details

**attendance:** Attendance records

Each model uses AutoField for primary keys to align with MySQL's auto-incrementing IDs.

## **Next Steps**

**Implement views:** Add logic in views.py to handle HTTP requests and render templates for user interaction.

**Create templates:** Design HTML templates for the front-end interface.

**Write tests:** Add unit tests in tests.py to ensure the reliability of the application.

**Add relationships:** Update models to include foreign key relationships (e.g., ForeignKey for student_id and course_id in Enrollment) for better data integrity.

**Enhance security:** Configure proper user authentication and authorization.

