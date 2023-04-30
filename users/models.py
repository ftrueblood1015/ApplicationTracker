from django.contrib.auth.models import User
from django.db import models

from base_abstracts.models import TrackingModel


# Create your models here.
class AdditionalUserInfo(TrackingModel):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    phone_number = models.CharField(max_length=12)

    class Meta:
        verbose_name = 'Additional User Info'
        verbose_name_plural = 'Additional Users Info'
