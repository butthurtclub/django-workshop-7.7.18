from django.db import models


class BaseModel(models.Model):
    created = models.DateTimeField(
        auto_now=True
    )

    updated = models.DateTimeField(
        null=True,
        blank=True
    )

    class Meta:
        abstract = True
