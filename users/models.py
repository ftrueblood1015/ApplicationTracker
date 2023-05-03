from django.contrib.auth.models import User
from django.db import models

from base_abstracts.models import TrackingModel
from users.model_utils import SecurityRuleCategories


# Create your models here.
class AdditionalUserInfo(TrackingModel):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    phone_number = models.CharField(max_length=12)

    class Meta:
        verbose_name = 'Additional User Info'
        verbose_name_plural = 'Additional Users Info'


class SecurityRule(TrackingModel):
    category = models.CharField(max_length=255, choices=[(x.value, x.name) for x in SecurityRuleCategories.all()])

    class Meta:
        verbose_name = 'Security Rule'
        verbose_name_plural = 'Security Rules'


class UserSecurityRule(TrackingModel):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    security_rule = models.ForeignKey(SecurityRule, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'User Security Rule'
        verbose_name_plural = 'User Security Rules'
