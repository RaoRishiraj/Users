from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin #TestDriven.io
from django.db import models 
import uuid

class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin): #Provide Pass field, last_login. Permissions like superuser and relationships. 
    id=models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True) 
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=25)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) #TRUE: can access admin panel 
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    ROLE_CHOICES = (#                                                   Anyone can login as either admin or staff
            ('administrator', 'Administrator'),
            ('staff', 'Staff')
        )
    role = models.CharField(max_length=25, choices=ROLE_CHOICES, default='staff')
    def __str__(self):
        return self.email #returns printable string when we print user