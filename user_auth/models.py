from django.db import models
from django.contrib.auth.models import AbstractUser#, UserManager
from .managers import UserManager

# Create your models here.
class User(AbstractUser):
    username = None#models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    # first_name = models.CharField(max_length=255)
    # last_name = models.CharField(max_length=255)
    user_verification = models.BooleanField(default=False) #initially this field is false but will se chan
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False) # a admin user; non super-user
    is_admin = models.BooleanField(default=False)
    is_institution = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    document = models.FileField(null=True, upload_to='useruploads/')



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] #emaila nd password are required fields and first name and last name is inherited from the user creation model

    #instanciate the usermanager object
    object = UserManager()

    

    def get_full_name(self):
        # The user is identified by their email address
        return self.email
    
    def get_name(self):
        user = UserDetail.objects.get(user=self.id)
        return user.first_name + user.last_name

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    # def has_perm(self, perm, obj=None):
    #     "Does the user have a specific permission?"
    #     # Simplest possible answer: Yes, always
    #     return True
    #
    # def has_module_perms(self, app_label):
    #     "Does the user have permissions to view the app `app_label`?"
    #     # Simplest possible answer: Yes, always
    #     return True
    #
    # def email_user(self, subject, message, from_email=None, **kwargs):
    #     send_mail(subject, message, from_email, [self.email], **kwargs)

    #
    @property
    def username(self):
        
        return self.email.split('@')[0]
    # @property
    # def is_admin(self):
    #     "Is the user a admin member?"
    #     return self.is_admin
    #
    # @property
    # def is_active(self):
    #     "Is the user active?"
    #     return self.is_active


class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, default='S-sewa')
    last_name = models.CharField(max_length=255, default='User')
    contact = models.CharField(max_length=10, null=False, default='N/A')
    height = models.FloatField('Height in Ft.', null=False, default='1')
    weight = models.FloatField(' Weight in Kg', null=False, default='1')
    dob= models.DateField(null=False, default='2000-01-01')
    profile_pic = models.ImageField(upload_to='profilepic/', null=False)

    def __str__(self):
        return self.user.email
    
    def get_age(self):
        from datetime import date
        today = date.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
    
    def get_bmi(self):
        ht = 0.3048 * self.height
        bmi = self.weight / (ht**2)
        return round(bmi,2)
    
