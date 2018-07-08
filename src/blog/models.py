from django.db import models
from core.models import BaseModel
from django.conf import settings
from ckeditor.fields import RichTextField


class Publication(BaseModel):
    title = models.CharField(
        max_length=100
    )

    def __str__(self):
        return f'{self.title}'

    class Meta:
        abstract = True


class Category(Publication):
    pass


class Tag(Publication):
    pass


class Article(Publication):

    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        related_name='articles',
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        to='Category',
        related_name='articles',
        on_delete=models.CASCADE
    )
    tags = models.ManyToManyField(
        to='Tag',
        related_name='articles',
        blank=True
    )
    image = models.ImageField(
        null=True,
        blank=True
    )
    content = RichTextField(
        null=False
    )
