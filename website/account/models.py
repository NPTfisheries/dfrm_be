from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from PIL import Image


class UserManager(BaseUserManager):

    use_in_migration = True

    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        if not first_name:
            raise ValueError('First name is required')
        if not last_name:
            raise ValueError('Last name is required')
        
        self.validate_password(password)

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        self.validate_password(password)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')

        return self.create_user(email, password, **extra_fields)
    
class User(AbstractUser):

    username = None
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.EmailField(max_length=100, unique=True)
    # date_joined = models.DateTimeField(auto_now_add=True)
    # is_admin = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=True)
    # is_staff = models.BooleanField(default=False)
    # is_superuser = models.BooleanField(default=False)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.first_name + " " + self.last_name


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, help_text = "User name", related_name='user_profiles', verbose_name="User Name")
    #work_phone = PhoneField("Work Phone", null=True, blank=True)
    #mobile_phone = PhoneField("Mobile Phone", null=True, blank=True)
    city = models.CharField("City", null = True, blank = True, max_length=50)
    state = models.CharField("State", null = True, blank = True, max_length=50)
    bio = models.TextField(null = True, blank=True, verbose_name="Biography")   
    avatar = models.ImageField("Profile Picture", upload_to='images/profile/', default='images/profile/P7160105_fix.JPG') 

    class Meta:
        ordering = ['user__first_name', 'user__last_name']

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.avatar.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.avatar.path)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name