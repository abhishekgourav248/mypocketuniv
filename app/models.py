from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, email, password, username, **other_fields):
        if not email:
            raise ValueError("Email is mandetory")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **other_fields)
        user.set_password(password)
        user.save()

    def create_superuser(self, email, password, username, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_faculty', False)
        other_fields.setdefault('is_student', False)

        if other_fields.get('is_staff') is not True:
            raise ValueError('set is_staff= True for superuser')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('set is_superuser=True for superuser')
        if other_fields.get('is_active') is not True:
            raise ValueError('set is_active=True For user to be able to login')

        return self.create_user(email, password, username, **other_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        max_length=60, verbose_name='email', primary_key=True)
    username = models.CharField(
        max_length=60, verbose_name='username', unique=True,blank=True)
    start_date = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)  # mandetory for superuser
    is_superuser = models.BooleanField(
        default=False)  # mandetory for superuser
    is_active = models.BooleanField(default=True)  # mandetory for login
    # to signify a user being a Faculty only
    is_faculty = models.BooleanField(default=False)
    # to signify a user being a student only
    is_student = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    def __str__(self):
        return self.email


class Session(models.Model):
    id = models.AutoField(primary_key=True)
    session_start = models.DateField()
    session_end = models.DateField()
    session_name = models.CharField(max_length=20, help_text='example 2021-24')

    def __str__(self):
        return self.session_name


class Department(models.Model):
    id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.department_name


class Semester(models.Model):
    id = models.AutoField(primary_key=True)
    semester_name = models.CharField(max_length=30)
    session_id = models.ForeignKey(Session, on_delete=models.CASCADE)

    def __str__(self):
        return self.semester_name


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course_name


class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject_name


class Faculty(models.Model):
    id = models.AutoField(primary_key=True)
    faculty = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_image = models.ImageField(blank=True, null=True)
    address_line = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    State = models.CharField(max_length=50)


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Subject, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_image = models.ImageField(blank=True, null=True)
    address_line = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
