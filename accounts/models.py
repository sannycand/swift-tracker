from uuid import uuid4

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.core.urlresolvers import reverse


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **kwargs):
        
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, username=email)
        user.set_password(password)
        user.save()
        
        return user

    def create_superuser(self, email, password, **kwargs):

        user = self.create_user(email, password, **kwargs)
        user.position = 'management'
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):

    MALE = "m"
    FEMALE = "f"
    GENDER = (
        (MALE, "Male"),
        (FEMALE, "Female")
    )

    DEVELOPER = "developer"
    DESIGNER = "designer"
    MANAGEMENT = "management"
    POSITION = (
        (DEVELOPER, "Developer"),
        (DESIGNER, "Designer"),
        (MANAGEMENT, "Management")
    )

    email = models.EmailField(max_length=200, unique=True)
    username = models.CharField(max_length=200, unique=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER, default=MALE)
    position = models.CharField(max_length=35, choices=POSITION, default=DEVELOPER)
    profile_photo = models.ImageField(upload_to='users/', null=True, blank=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()
    
    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return "{first_name} {last_name}".format(
            first_name=self.first_name,
            last_name=self.last_name
        )

    def get_short_name(self):
        return self.first_name


class Invitation(models.Model):
    
    DEVELOPER = "developer"
    DESIGNER = "designer"
    MANAGEMENT = "management"
    POSITION = (
        (DEVELOPER, "Developer"),
        (DESIGNER, "Designer"),
        (MANAGEMENT, "Management")
    )

    email = models.EmailField(max_length=225)
    position = models.CharField(max_length=35, choices=POSITION, default=DEVELOPER)
    key = models.CharField(max_length=32, null=True, blank=True)
    is_used = models.BooleanField(default=False)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return '{}-{}'.format(self.email, self.position)

    def save(self, *args, **kwargs):
        if not self.id:
            self.key = self._generate_key()
        return super(Invitation, self).save(*args, **kwargs)

    def _generate_key(self):
        return uuid4().hex

