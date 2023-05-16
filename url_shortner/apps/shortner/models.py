from django.db import models
from url_shortner.common.models import TimeStampedModel


class Shortner(TimeStampedModel):
    original_url = models.URLField()
    short_url = models.CharField(max_length=10, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.original_url}-{self.short_url}"
