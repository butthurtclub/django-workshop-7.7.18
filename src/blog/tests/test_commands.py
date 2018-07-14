from django.test import TestCase
from django.core.management import call_command

from blog import models
from .mixins import CreateMixin


class TestDeleteAllCommand(TestCase, CreateMixin):
    def test_command(self):
        self._create_objects()
        self.assertEqual(models.Category.objects.count(), 1)
        self.assertEqual(models.Article.objects.count(), 1)
        self.assertEqual(models.Tag.objects.count(), 1)

        call_command('blog_delete_all')

        self.assertEqual(models.Category.objects.count(), 0)
        self.assertEqual(models.Article.objects.count(), 0)
        self.assertEqual(models.Tag.objects.count(), 0)