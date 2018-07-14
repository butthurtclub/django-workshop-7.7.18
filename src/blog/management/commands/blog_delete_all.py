from django.core.management.base import BaseCommand
from blog import models


class Command(BaseCommand):
    def handle(self, *args, **options):
        models.Category.objects.all().delete()
        models.Tag.objects.all().delete()
        models.Article.objects.all().delete()
