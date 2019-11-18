from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have a email")
        user = self.model(email=self.normalize_email(email),
        **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_staffuser(self, email, password, location, **extra_fields):
        user = self.create_user(email, password)
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        
        return user
class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    location = models.CharField(max_length=255, default="Karachi")

    objects = UserManager()
    USERNAME_FIELD = 'email'
    
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def staff(self):
        return self.is_staff
    @property
    def admin(self):
        return self.is_admin
    @property
    def active(self):
        return self.is_active