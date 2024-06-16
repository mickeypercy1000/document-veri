import uuid
from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from authentication.managers import CustomUserManager


class User(AbstractBaseUser):

    id = models.CharField(
        _("id"),
        max_length=50,
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
    )
    email = models.EmailField(_("Email"), unique=True, blank=True, null=True)
    business_name = models.CharField(_("Business Name"), max_length=255, unique=True, blank=True, null=True)
    phone = models.CharField(_("Phone"), max_length=10, unique=True, blank=True, null=True)
    firstname = models.CharField(_("First Name"), max_length=255, blank=True, null=True)
    lastname = models.CharField(_("Last Name"), max_length=255, blank=True, null=True)
    otp = models.CharField(_("OTP"), max_length=8, blank=True, null=True)
    otp_verified = models.BooleanField(_("OTP Verified"), default=False)
    country = models.CharField(_("Country"), max_length=255, blank=True, null=True) # include package for countries
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ["business_name", "phone", "firstname", "lastname", "country"]

    class Meta:
        ordering = ("-created_at",)
    
    def __str__(self):
        return f"{self.firstname} | {self.lastname} | {str(self.email)}"

    def get_email(self):
        return self.email

    def get_fullname(self):
        return f"{self.firstname} {self.lastname}"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class UserOTP(models.Model):
    otp = models.CharField(max_length=8, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user} {self.otp}"

    