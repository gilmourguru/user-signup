# from __future__ import unicode_literals

# from django.db import models
# from django.core.mail import send_mail
# from django.contrib.auth.models import PermissionsMixin
# from django.contrib.auth.base_user import AbstractBaseUser
# from django.utils.translation import ugettext_lazy as _

# from userSignup.signup.managers import UserManager

# # Create your models here.
# class MyUser(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(_('username'), unique=True, max_length=20)
#     password1 = models.CharField(_('password1'), max_length=20)
#     password2 = models.CharField(_('password2'), max_length=20)
#     email = models.CharField(_('email'), max_length=20)

#     objects = UserManager()

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['username', 'password1', 'password2']

#     class Meta:
#         verbose_name = _('user')
#         verbose_name_plural = _('users')