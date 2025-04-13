# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    maker = models.CharField(max_length=255, null=True, blank=True)
    price = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class My_Mag_Models(models.Model):

    #__My_Mag_Models_FIELDS__
    materials = models.CharField(max_length=255, null=True, blank=True)
    mu_r = models.CharField(max_length=255, null=True, blank=True)

    #__My_Mag_Models_FIELDS__END

    class Meta:
        verbose_name        = _("My_Mag_Models")
        verbose_name_plural = _("My_Mag_Models")



#__MODELS__END
