from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field is required.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('Student', 'Student'),
        ('Lecturer', 'Lecturer'),
        ('Formator', 'Formator'),
        ('Registrar', 'Registrar'),
        ('DVC Finance', 'DVC Finance'),
        ('Finance Administrator', 'Finance Administrator'),
        ('Secretary', 'Secretary'),
        ('The Rector', 'The Rector'),
        ('DVC Academics', 'DVC Academics'),
        ('HOD Language', 'HOD Language'),
        ('IT Administrator', 'IT Administrator'),
    )

    DEPARTMENT_CHOICES = (
        ('Philosophy', 'Philosophy'),
        ('Language', 'Language'),
        ('Psychology', 'Psychology'),
        ('Theology', 'Theology'),
    )

    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    MARITAL_CHOICES = (
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Priest', 'Priest'),
        ('Sister', 'Sister')
    )

    QUALIFICATIONS_CHOICES = [
        ('Degree', 'Degree'),
        ('Masters', 'Masters'),
        ('Doctor', 'Doctor'),
        ('Professor', 'Professor')
    ]

  
    

    username = None  # disable the username field
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=300, choices=ROLE_CHOICES, blank=True)
    school = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)
    marital_status = models.CharField(max_length=10, choices=MARITAL_CHOICES, blank=True)
    qualification = models.CharField(max_length=100, choices=QUALIFICATIONS_CHOICES, blank=True)
    rates = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # no username field anymore

    objects = CustomUserManager()

    def __str__(self):
        return self.email