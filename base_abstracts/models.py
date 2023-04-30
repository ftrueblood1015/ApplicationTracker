from django.db import models
from uuid import uuid4
import datetime


# Create your models here.
class BaseInfo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    description = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = f"Verbose Not Set".format(__name__)
        verbose_name_plural = f"Verbose Plural Not Set".format(__name__)
        abstract = True

    def __str__(self):
        return f'{self.description}'


class TrackingModel(BaseInfo):
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)
    creator = models.IntegerField()
    last_updater = models.IntegerField()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.id is None:
            self.created_time = datetime.datetime.now()
        self.last_updated_time = datetime.datetime.now()
        return super(TrackingModel, self).save(*args, **kwargs)
